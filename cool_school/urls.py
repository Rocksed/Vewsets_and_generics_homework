from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from cool_school.views import LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentViewSet, CourseViewSet, SubscriptionListApiView, SubscriptionCreateApiView, \
    SubscriptionDestroyApiView

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'payments', PaymentViewSet, basename='payments')
urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/detail/<int:pk>', LessonListAPIView.as_view(), name='lesson_id'),
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/update/<int:pk>', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='lesson_delete'),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('subscription/', SubscriptionListApiView.as_view()),
                  path('subscription/create/<int:pk>/', SubscriptionCreateApiView.as_view()),
                  path('subscription/delete/<int:pk>/', SubscriptionDestroyApiView.as_view())
              ] + router.urls
