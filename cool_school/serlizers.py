from rest_framework import serializers

from cool_school.models import Course, Lesson, Payment, Subscription
from cool_school.validators import ModelValidator

from user.serlizers import UserSerializer


class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Subscription

        fields = '__all__'
        read_only_fields = ('user', 'course')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [ModelValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.IntegerField(source='lesson_set.count.lesson', default=0, read_only=True)
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, obj):
        lessons = Lesson.objects.filter(course=obj)
        lesson_serializer = LessonSerializer(lessons, many=True)
        return lesson_serializer.data


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
