from models.Ticket import Ticket


class TicketRepository:
    @staticmethod
    def create_ticket(parking_lot, floor, spot, vehicle):
        ticket = Ticket(parking_lot.parking_lot_name, floor.position, spot.position, vehicle)
        return ticket
