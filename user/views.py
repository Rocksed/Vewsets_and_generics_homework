from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from cool_school.serlizers import UserSerializer
from user.models import User


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


