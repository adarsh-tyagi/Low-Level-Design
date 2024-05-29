from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..services.ExpenseService import ExpenseService


@method_decorator(csrf_exempt, name='dispatch')
class ExpenseView(View):
    def get(self, request):
        group_id = request.GET.get('group_id')
        try:
            expenses = ExpenseService.get_expenses(group_id)
            return JsonResponse({'expenses': list(expenses.values())})
        except Exception as e:
            return JsonResponse({'error': str(e)})

    def post(self, request):
        group_id = request.POST.get('group_id')
        payment_made_by_user_id = request.POST.get('payment_made_by_user_id')
        total_amount = float(request.POST.get('total_amount'))
        no_of_users = int(request.POST.get('no_of_users'))
        users_own_money_list = request.POST.get('users_own_money_list')
        expense_type = request.POST.get('expense_type')
        expense_description = request.POST.get('expense_description', None)
        amount_list = request.POST.get('amount_list', '')
        try:
            users_own_money_list = [i.strip() for i in users_own_money_list.split(',') if i.strip()]
            amount_list = [float(i.strip()) for i in amount_list.split(',') if i.strip()]
            expense = ExpenseService.add_expense(group_id, payment_made_by_user_id, total_amount, no_of_users,
                                                 users_own_money_list, expense_type, expense_description, amount_list)
            return JsonResponse({'expense': 'Expense added successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
