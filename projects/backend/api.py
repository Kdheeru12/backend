from rest_framework.views import APIView
import requests
from backend.serializers import UserSerializer
from rest_framework.response import Response
from user.models import User


class UserAPIView(APIView):
    def import_users(self):
        res = requests.get("https://jsonplaceholder.typicode.com/users")
        res = res.json()
        users_to_add = []
        for user in res:
            users_to_add.append(
                User(
                    name=user["name"],
                    email=user["email"],
                    website=user["website"],
                    username=user["username"],
                )
            )
        User.objects.bulk_create(users_to_add)

    def get(self, request, *args, **kwargs):
        users_count = User.objects.all().count()
        if users_count == 0:
            self.import_users()
        users = User.objects.all()
        data = UserSerializer(users, many=True).data
        return Response(data)
