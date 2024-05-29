from controllers.ParkingLotController import ParkingLotController
from strategies.findParkingSpotStrategies.FindParkingLotStrategyFactory import FindParkingLotStrategyFactory


class CommandController:
    @staticmethod
    def execute_commands():
        parking_tickets_storage = {}
        parking_lot = None
        while True:
            command = input("Enter command: \n")
            if command == "exit":
                break
            command_parts = command.split(" ")
            if command_parts[0] == "create_parking_lot":
                if parking_lot is None:
                    parking_lot = ParkingLotController.create_parking_lot(command_parts[1], int(command_parts[2]),
                                                                          int(command_parts[3]), int(command_parts[4]),
                                                                          int(command_parts[5]))
                else:
                    print("Parking lot already exists.")

            elif command_parts[0] == "add_parking_floor":
                if parking_lot:
                    ParkingLotController.add_parking_floor(parking_lot, int(command_parts[1]), int(command_parts[2]),
                                                           int(command_parts[3]))
                else:
                    print("Please create a parking lot first.")

            elif command_parts[0] == "add_parking_slot":
                if parking_lot:
                    ParkingLotController.add_parking_slot(parking_lot, int(command_parts[1]), command_parts[2],
                                                          int(command_parts[3]))
                else:
                    print("Please create a parking lot first.")

            elif command_parts[0] == "display_parking_lot":
                if parking_lot:
                    ParkingLotController.display_parking_lot(parking_lot)
                else:
                    print("Please create a parking lot first.")

            elif command_parts[0] == "display_free_slots":
                if parking_lot:
                    ParkingLotController.display_free_slots(parking_lot, command_parts[1])
                else:
                    print("Please create a parking lot first.")

            elif command_parts[0] == "display_free_count":
                if parking_lot:
                    ParkingLotController.display_free_count(parking_lot, command_parts[1])
                else:
                    print("Please create a parking lot first.")

            elif command_parts[0] == "display_occupied_slots":
                if parking_lot:
                    ParkingLotController.display_occupied_slots(parking_lot, command_parts[1])
                else:
                    print("Please create a parking lot first.")

            elif command_parts[0] == "park_vehicle":
                if parking_lot:
                    find_parking_spot_strategy = FindParkingLotStrategyFactory.get_find_parking_spot_strategy("closest")
                    ticket = ParkingLotController.park_vehicle(parking_lot, command_parts[1], command_parts[2],
                                                               command_parts[3], find_parking_spot_strategy)
                    parking_tickets_storage[ticket.get_ticket_id()] = ticket
                else:
                    print("Please create a parking lot first.")

            elif command_parts[0] == "unpark_vehicle":
                if parking_lot:
                    ticket = parking_tickets_storage.get(command_parts[1], None)
                    ParkingLotController.unpark_vehicle(parking_lot, ticket)
                else:
                    print("Please create a parking lot first.")

            else:
                print("Invalid command. Please try again.")
