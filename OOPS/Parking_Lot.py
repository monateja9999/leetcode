class Vehicle:
    def __init__(self, vehicle_type: str, vehicle_number: str):
        self.vehicle_type = vehicle_type
        self.vehicle_number = vehicle_number

class ParkingSpot:
    def __init__(self, spot_id: int, spot_type: str):
        self.spot_id = spot_id
        self.spot_type = spot_type  # E.g., 'compact', 'large', 'motorcycle'
        self.is_occupied = False
        self.vehicle = None
    
    def park_vehicle(self, vehicle: Vehicle):
        if self.is_occupied:
            print(f"Parking spot {self.spot_id} is already occupied.")
        elif vehicle.vehicle_type != self.spot_type:
            print(f"Cannot park a {vehicle.vehicle_type} in a {self.spot_type} spot.")
        else:
            self.is_occupied = True
            self.vehicle = vehicle
            print(f"Vehicle {vehicle.vehicle_number} parked at spot {self.spot_id}.")
    
    def remove_vehicle(self):
        if not self.is_occupied:
            print(f"Parking spot {self.spot_id} is empty.")
        else:
            print(f"Vehicle {self.vehicle.vehicle_number} removed from spot {self.spot_id}.")
            self.is_occupied = False
            self.vehicle = None

class ParkingLot:
    def __init__(self, total_spots: int):
        self.parking_spots = []
        for i in range(total_spots):
            # Adding different types of spots as an example.
            spot_type = 'compact' if i % 2 == 0 else 'large'
            self.parking_spots.append(ParkingSpot(i, spot_type))
    
    def park_vehicle(self, vehicle: Vehicle):
        for spot in self.parking_spots:
            if not spot.is_occupied and vehicle.vehicle_type == spot.spot_type:
                spot.park_vehicle(vehicle)
                return
        print("No available spots for this vehicle.")
    
    def unpark_vehicle(self, vehicle_number: str):
        for spot in self.parking_spots:
            if spot.is_occupied and spot.vehicle.vehicle_number == vehicle_number:
                spot.remove_vehicle()
                return
        print("Vehicle not found in the parking lot.")

# Driver Code
if __name__ == "__main__":
    # Creating parking lot with 5 spots
    parking_lot = ParkingLot(5)

    # Creating vehicles
    vehicle1 = Vehicle("compact", "ABC123")
    vehicle2 = Vehicle("large", "XYZ456")
    vehicle3 = Vehicle("compact", "LMN789")

    # Park vehicles
    parking_lot.park_vehicle(vehicle1)
    parking_lot.park_vehicle(vehicle2)
    parking_lot.park_vehicle(vehicle3)

    # Unpark a vehicle
    parking_lot.unpark_vehicle("XYZ456")

    # Trying to park again after unpark
    parking_lot.park_vehicle(vehicle2)
