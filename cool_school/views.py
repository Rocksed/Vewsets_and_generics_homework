from rest_framework import viewsets, generics
from rest_framework import filters as drf_filters
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from cool_school.models import Course, Lesson, Payment, Subscription
from cool_school.pagination import MyPagination
from cool_school.permissions import UserOrStuff
from cool_school.serlizers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [AllowAny]
    pagination_class = MyPagination


class LessonCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


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
