class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def get_license_plate(self):
        return self.license_plate

    def get_vehicle_type(self):
        return self.vehicle_type


class ParkingLevel:
    def __init__(self, level_number, total_spaces):
        self.level_number = level_number
        self.total_spaces = total_spaces
        self.remaining_spaces = total_spaces.copy()
        self.vehicle_list = []

    def get_total_spaces(self):
        return self.total_spaces

    def get_remaining_spaces(self):
        return self.remaining_spaces

    def find_vehicle(self, license_plate):
        return any(vehicle.get_license_plate() == license_plate for vehicle in self.vehicle_list)

    def add_vehicle(self, vehicle):
        vehicle_type = vehicle.get_vehicle_type()
        if self.remaining_spaces.get(vehicle_type, 0) > 0:
            self.vehicle_list.append(vehicle)
            self.remaining_spaces[vehicle_type] -= 1
            return True
        return False

    def remove_vehicle(self, license_plate):
        for vehicle in self.vehicle_list:
            if vehicle.get_license_plate() == license_plate:
                self.vehicle_list.remove(vehicle)
                self.remaining_spaces[vehicle.get_vehicle_type()] += 1
                return True
        return False


class ParkingGarage:
    def __init__(self, levels):
        self.levels = levels

    def get_total_spaces(self):
        total_spaces = {'Normal': 0, 'Compact': 0, 'Oversize': 0}
        for level in self.levels:
            for vehicle_type in total_spaces.keys():
                total_spaces[vehicle_type] += level.get_total_spaces().get(vehicle_type, 0)
        return total_spaces

    def get_remaining_spaces(self):
        remaining_spaces = {'Normal': 0, 'Compact': 0, 'Oversize': 0}
        for level in self.levels:
            for vehicle_type in remaining_spaces.keys():
                remaining_spaces[vehicle_type] += level.get_remaining_spaces().get(vehicle_type, 0)
        return remaining_spaces

    def find_vehicle(self, license_plate):
        for level in self.levels:
            if level.find_vehicle(license_plate):
                return f"Vehicle ({license_plate}) is parked on level {level.level_number}."
        return f"No vehicle with license plate {license_plate} found."

    def add_vehicle(self, vehicle):
        for level in self.levels:
            if level.add_vehicle(vehicle):
                return f"Vehicle ({vehicle.get_license_plate()}) added to level {level.level_number}."
        return f"No available space for vehicle ({vehicle.get_license_plate()})."

    def remove_vehicle(self, license_plate):
        for level in self.levels:
            if level.remove_vehicle(license_plate):
                return f"Vehicle ({license_plate}) was removed from level {level.level_number}."
        return f"No vehicle with license plate {license_plate} found."

    def print_garage(self):
        total_spaces = self.get_total_spaces()
        print("Total Spaces")
        print(f"Normal ({total_spaces['Normal']}) Compact ({total_spaces['Compact']}) Oversize ({total_spaces['Oversize']})\n")

        print("Remaining Spaces")
        for level in self.levels:
            remaining_spaces = level.get_remaining_spaces()
            print(
                f"Level {level.level_number}: Normal ({remaining_spaces['Normal']}) "
                f"Compact ({remaining_spaces['Compact']}) Oversize ({remaining_spaces['Oversize']})"
            )
        print("\nVehicles:")
        for level in self.levels:
            for vehicle in level.vehicle_list:
                print(
                    f"{vehicle.get_vehicle_type()} vehicle ({vehicle.get_license_plate()}) is parked on level {level.level_number}."
                )


lvl1 = ParkingLevel(1, {'Normal': 4, 'Compact': 1, 'Oversize': 2})
lvl2 = ParkingLevel(2, {'Normal': 3, 'Compact': 1, 'Oversize': 1})
lvl3 = ParkingLevel(3, {'Normal': 3, 'Compact': 2, 'Oversize': 2})

garage = ParkingGarage([lvl1, lvl2, lvl3])


vehicle1 = Vehicle("EDL6776", "Compact")
vehicle2 = Vehicle("BLB9665", "Normal")
vehicle3 = Vehicle("PHE9858", "Compact")
vehicle4 = Vehicle("MEI3923", "Compact")
vehicle5 = Vehicle("NDL2511", "Compact")

garage.add_vehicle(vehicle1)
garage.add_vehicle(vehicle2)
garage.add_vehicle(vehicle3)
garage.add_vehicle(vehicle4)
garage.add_vehicle(vehicle5)

garage.print_garage()

print("\n" + garage.find_vehicle("NDL2511"))

print("\n" + garage.remove_vehicle("NDL2511"))

garage.print_garage()