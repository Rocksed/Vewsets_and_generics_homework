from rest_framework import serializers

from cool_school.models import Course, Lesson, Payment
from user.models import User


class ModelValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if 'https://yotube.com/' not in value.get('video_link'):
            raise serializers.ValidationError('You can only add youtube.com links')


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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
