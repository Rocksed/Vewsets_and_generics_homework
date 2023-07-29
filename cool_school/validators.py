from rest_framework import serializers


class ModelValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if 'youtube.com' not in value.get('video_link'):
            raise serializers.ValidationError('You can only add youtube.com links')
