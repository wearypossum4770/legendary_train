<<<<<<< HEAD
from django.contrib.auth import get_user_model
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.api.serializers import ProfileSerializer, UserSerializer
from users.models import Profile
=======
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication

from users.models import Profile
from users.api.serializers import UserSerializer, ProfileSerializer
>>>>>>> 07b0ff3d47923f9eeeb106dff01ed70b8cf689f5

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

<<<<<<< HEAD
    queryset = User.objects.all().order_by("-date_joined")
=======
    queryset = User.objects.all()
>>>>>>> 07b0ff3d47923f9eeeb106dff01ed70b8cf689f5
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class UserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    # token = Token.objects.create(user=...)
    def get(self, request, format=None):
<<<<<<< HEAD
        print(request)
=======
>>>>>>> 07b0ff3d47923f9eeeb106dff01ed70b8cf689f5
        content = {
            "user": str(request.user),  # `django.contrib.auth.User` instance.
            "auth": str(request.auth),  # None
        }
        return Response(content)
