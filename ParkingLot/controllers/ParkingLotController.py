from models.ParkingFloor import ParkingFloor
from models.VehicleType import VehicleType
from models.ParkingLot import ParkingLot
from models.SlotStatus import SlotStatus
from models.Vehicle import Vehicle
from repositories.ParkingSlotRepository import ParkingSlotRepository
from repositories.TicketRepository import TicketRepository
from exceptions.InvalidTicketException import InvalidTicketException


class ParkingLotController:
    @staticmethod
    def create_parking_lot(parking_lot_name, parking_floors_count, bike_slots_count, car_slots_count, truck_slots_count):
        parking_floors = []
        for floor in range(parking_floors_count):
            curr_floor = ParkingLotController.create_parking_floor(bike_slots_count, car_slots_count, truck_slots_count)
            curr_floor.position = floor + 1
            parking_floors.append(curr_floor)
        print(f"Created a parking lot of {parking_floors_count} floors having {bike_slots_count} bike slots, "
              f"{car_slots_count} car slots and {truck_slots_count} truck slots on each floor.")
        return ParkingLot(parking_lot_name, parking_floors)

    @staticmethod
    def create_parking_floor(bike_slots_count, car_slots_count, truck_slots_count):
        all_parking_slots = []
        all_parking_slots.extend(ParkingSlotRepository.create_slots(VehicleType.BIKE.name, bike_slots_count))
        all_parking_slots.extend(ParkingSlotRepository.create_slots(VehicleType.CAR.name, car_slots_count))
        all_parking_slots.extend(ParkingSlotRepository.create_slots(VehicleType.TRUCK.name, truck_slots_count))
        for slot_num in range(len(all_parking_slots)):
            all_parking_slots[slot_num].position = slot_num + 1
        return ParkingFloor(all_parking_slots)

    @staticmethod
    def add_parking_floor(parking_lot, bike_slots_count, car_slots_count, truck_slots_count):
        parking_lot.parking_floors.append(ParkingLotController.create_parking_floor(bike_slots_count, car_slots_count,
                                                                                    truck_slots_count))
        print(f"Added a floor to the parking lot having {bike_slots_count} bike slots, {car_slots_count} car slots "
              f"and {truck_slots_count} truck slots.")
        return parking_lot

    @staticmethod
    def add_parking_slot(parking_lot, parking_floor, slot_type, slots_count):
        parking_lot.parking_floors[parking_floor].extend(ParkingSlotRepository.create_slots(slot_type, slots_count))
        print(f"Added {slots_count} {slot_type} slots to floor no. {parking_floor}.")
        return parking_lot

    @staticmethod
    def display_parking_lot(parking_lot):
        parking_lot.display()

    @staticmethod
    def get_slots_data(parking_lot, vehicle_type):
        slots_data = {}
        for floor in parking_lot.parking_floors:
            slots_data[floor.position] = {'free_slots': [], 'occupied_slots': []}
            for slot in floor.parking_slots:
                if slot.slot_type == vehicle_type:
                    if slot.slot_status == SlotStatus.AVAILABLE.name:
                        slots_data[floor.position]['free_slots'].append(slot.position)
                    elif slot.slot_status == SlotStatus.PARKED.name:
                        slots_data[floor.position]['occupied_slots'].append(slot.position)
        return slots_data

    @staticmethod
    def display_free_slots(parking_lot, vehicle_type):
        slots_data = ParkingLotController.get_slots_data(parking_lot, vehicle_type)
        for floor, slots in slots_data.items():
            print(f"Free slots for {vehicle_type} on floor no. {floor}: {slots['free_slots']}.")

    @staticmethod
    def display_free_count(parking_lot, vehicle_type):
        slots_data = ParkingLotController.get_slots_data(parking_lot, vehicle_type)
        for floor, slots in slots_data.items():
            print(f"No. of free slots for {vehicle_type} on floor no. {floor}: {len(slots['free_slots'])}.")

    @staticmethod
    def display_occupied_slots(parking_lot, vehicle_type):
        slots_data = ParkingLotController.get_slots_data(parking_lot, vehicle_type)
        for floor, slots in slots_data.items():
            print(f"Occupied slots for {vehicle_type} on floor no. {floor}: {slots['occupied_slots']}.")

    @staticmethod
    def park_vehicle(parking_lot, vehicle_type, vehicle_registration_number, vehicle_color, find_parking_spot_strategy):
        vehicle = Vehicle(vehicle_type, vehicle_registration_number, vehicle_color)
        parking_floor, parking_spot = find_parking_spot_strategy.find_parking_spot(parking_lot, vehicle_type)
        if parking_floor and parking_spot:
            parking_spot.slot_status = SlotStatus.PARKED.name
            parking_spot.vehicle = vehicle
            parking_ticket = TicketRepository.create_ticket(parking_lot, parking_floor, parking_spot, vehicle)
            print(f"Parked the vehicle. This is your ticket id: {parking_ticket.get_ticket_id()}.")
            return parking_ticket
        else:
            print("Parking Lot is full. Please try again later.")

    @staticmethod
    def unpark_vehicle(parking_lot, ticket):
        if ticket:
            floor_number, slot_number = ticket.floor_number, ticket.slot_number
            if (floor_number > len(parking_lot.parking_floors) or
                    slot_number > len(parking_lot.parking_floors[floor_number - 1].parking_slots)):
                raise InvalidTicketException("Invalid Ticket")
            else:
                parking_floor = parking_lot.parking_floors[floor_number - 1]
                parking_spot = parking_floor.parking_slots[slot_number - 1]
                if parking_spot.slot_status == SlotStatus.PARKED.name:
                    parking_spot.slot_status = SlotStatus.AVAILABLE.name
                    parking_spot.vehicle = None
                else:
                    raise InvalidTicketException("Invalid Ticket")
                print("Unparked the vehicle.")
        else:
            print("No ticket found, Please show the ticket to unpark the vehicle.")

