from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from users.models import Profile
from users.api.serializers import UserSerializer, ProfileSerializer

User = get_user_model()


def home(request):
    return JsonResponse({"message": "helloworld"})


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # token = Token.objects.create(user=...)
    def get(self, request, format=None):
        content = {
            "user": str(request.user),  # `django.contrib.auth.User` instance.
            "auth": str(request.auth),  # None
        }
        return Response(content)
