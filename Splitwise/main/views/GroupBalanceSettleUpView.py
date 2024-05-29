from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..services.GroupBalanceSettleUpService import GroupBalanceSettleUpService


@method_decorator(csrf_exempt, name='dispatch')
class GroupBalanceView(View):
    def get(self, request):
        group_id = request.GET.get('group_id')
        user_id = request.GET.get('user_id', None)
        try:
            balance_statements = GroupBalanceSettleUpService().get_group_balance_for_user(group_id, user_id)
            return JsonResponse({'balance_statements': balance_statements})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@method_decorator(csrf_exempt, name='dispatch')
class GroupSettleUpView(View):
    def post(self, request):
        group_id = request.POST.get('group_id')
        try:
            transactions = GroupBalanceSettleUpService().settle_up_group_balance(group_id)
            return JsonResponse({'transactions': transactions})
        except Exception as e:
            return JsonResponse({'error': str(e)})
