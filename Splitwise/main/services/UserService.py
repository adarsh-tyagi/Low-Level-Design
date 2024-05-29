from ..models.User import User
from django.db.models import Q


class UserService:
    @staticmethod
    def add_user(username, name, email, password):
        user = User.objects.filter(Q(username=username) | Q(email=email))
        if user:
            raise Exception('User already exists with given username or email')
        user = User(username=username, name=name, email=email, password=password)
        user.save()
        return user
