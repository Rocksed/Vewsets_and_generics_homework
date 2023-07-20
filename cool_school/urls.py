from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from cool_school.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, PaymentViewSet

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'payments', PaymentViewSet, basename='payments')
urlpatterns = [
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:id>/', LessonListAPIView.as_view(), name='lesson_pk'),
                  path('create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + router.urls
