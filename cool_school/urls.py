from django.urls import path
from rest_framework.routers import DefaultRouter

from cool_school.views import CourseViewSet, LessonListView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
                  path('lesson/', LessonListView.as_view(), name='lesson_list'),
              ] + router.urls
