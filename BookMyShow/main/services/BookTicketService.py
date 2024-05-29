from django.db import transaction
from ..services.TicketPriceCalculatorService import TicketPriceCalculatorService
from ..models.ShowSeat import ShowSeat
from ..models.Ticket import Ticket
from ..models.ShowSeatStatus import ShowSeatStatus
from ..models.User import User
from ..models.TicketStatus import TicketStatus


class BookTicketService:
    @transaction.atomic
    def book_ticket(self, user_id, show_seat_ids):
        show_seats = ShowSeat.get_all_seats_by_ids(show_seat_ids)
        user = User.objects.get(id=user_id)
        for show_seat in show_seats:
            if show_seat.show_seat_status != ShowSeatStatus.AVAILABLE.name:
                raise Exception("Seat is not available")

        show = show_seats[0].show

        for show_seat in show_seats:
            show_seat.show_seat_status = ShowSeatStatus.LOCKED.name
            show_seat.save()

        ticket = Ticket()
        ticket.ticket_status = TicketStatus.PENDING.name
        ticket.show = show
        ticket.show_seat = show_seats
        ticket.price = TicketPriceCalculatorService().ticket_price()
        ticket.booked_by = user
        ticket.save()
        return ticket
