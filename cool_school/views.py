import stripe
from rest_framework import viewsets, generics
from rest_framework import filters as drf_filters
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from cool_school.models import Course, Lesson, Payment, Subscription
from cool_school.pagination import MyPagination
from cool_school.serlizers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from config.settings import STRIPE_API_KEY
from cool_school.tasks import send_updated_email


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination

    def update(self, request, *args, **kwargs):
        send_updated_email.delay(kwargs['pk'])

        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    pagination_class = MyPagination


class LessonCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class PaymentFilter(filters.FilterSet):
    class Meta:
        model = Payment
        fields = {
            'course': ['exact'],
            'lesson': ['exact'],
            'payment_method': ['exact'],
        }


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [drf_filters.OrderingFilter, filters.DjangoFilterBackend]
    ordering_fields = ['payment_date']
    filterset_class = PaymentFilter


class SubscriptionListApiView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionCreateApiView(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):
        course = Course.objects.get(pk=self.kwargs.get('pk'))
        user = self.request.user
        instance = Subscription.objects.create(user=user, course=course)
        instance.save()


class SubscriptionDestroyApiView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class UserCourseSubscriptionViewSet(viewsets.ViewSet):

    @action(detail=True, methods=['post'])
    def subscribe(self, request, pk=None):
        try:
            # Получить информацию о курсе
            payment = Payment.objects.get(pk=pk)
            course = Course.objects.get(pk=pk)
            course_title = course.title
            course_price = payment.amount

            # Создать платежное намерение в Stripe
            stripe.api_key = STRIPE_API_KEY
            payment_intent = stripe.PaymentIntent.create(
                amount=course_price,
                currency="usd",
                payment_method_types=["card"],
                description=f"Subscription to {course_title}",
                metadata={"course_id": course.id},
            )

            return Response({"client_secret": payment_intent.client_secret}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['get'])
    def get_payment(self, request, pk=None):
        try:

            course = Course.objects.get(pk=pk)

            stripe.api_key = STRIPE_API_KEY
            payment_intent_id = course.payment_intent_id
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

            return Response({"payment_intent": payment_intent}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
