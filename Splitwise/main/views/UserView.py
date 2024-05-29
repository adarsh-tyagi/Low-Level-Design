from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from ..services.UserService import UserService


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def post(self, request):
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserService.add_user(username, name, email, password)
            return JsonResponse({'user': 'User is created successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
