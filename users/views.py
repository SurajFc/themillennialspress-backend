from news.baseclass import *
from .serializers import (
    UserCreateSerializer
)
from rest_framework.permissions import (
    AllowAny, IsAdminUser
)


class RegisterView(AbstractBaseClassApiView):
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer
    http_method_names = ('post', )
