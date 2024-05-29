from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..services.BookTicketService import BookTicketService


@method_decorator(csrf_exempt, name='dispatch')
class BookTicketView(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        show_seats = request.POST.get('show_seat_ids')
        try:
            ticket = BookTicketService().book_ticket(user_id, show_seats)
            response = {"status": "SUCCESS", "ticket": ticket}
            return JsonResponse(response)
        except:
            response = {"status": "FAILED"}
            return JsonResponse(response)
