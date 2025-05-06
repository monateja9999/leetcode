from typing import List
import uuid

import threading

lock = threading.Lock()

# Entity Classes
class Person:
    def __init__(self, person_id: str, name: str):
        self.person_id = person_id
        self.name = name

class Customer(Person):
    def create_package(self, size: str):
        package = Package(self, size)
        print(f"{self.name} created package {package.package_id} of size {size}")
        return package

class DeliveryAgent(Person):
    def deliver_package(self, locker_system, package):
        locker_system.assign_locker(package)
    
    def pickup_package(self, locker_system, package_id):
        locker_system.release_locker(package_id)

class Package:
    def __init__(self, customer: Customer, size: str):
        self.package_id = str(uuid.uuid4())[:8]
        self.customer = customer
        self.size = size

class Locker:
    def __init__(self, locker_id: str, size: str):
        self.locker_id = locker_id
        self.size = size
        self.occupied = False
        self.package = None

    def assign_package(self, package: Package):
        self.package = package
        self.occupied = True
        print(f"Package {package.package_id} assigned to Locker {self.locker_id}")

    def remove_package(self):
        print(f"Package {self.package.package_id} picked up from Locker {self.locker_id}")
        self.package = None
        self.occupied = False

# Core System
class LockerSystem:
    def __init__(self, lockers: List[Locker]):
        self.lockers = lockers
        self.package_map = {}

    def assign_locker(self, package: Package):
        for locker in self.lockers:
            if not locker.occupied and locker.size == package.size:
                locker.assign_package(package)
                self.package_map[package.package_id] = locker
                return
        print(f"No available locker for package {package.package_id}")

    def release_locker(self, package_id: str):
        if package_id in self.package_map:
            locker = self.package_map[package_id]
            locker.remove_package()
            del self.package_map[package_id]
        else:
            print("Invalid package ID or already picked up.")


if __name__ == "__main__":

    # Setup Lockers
    lockers = [
        Locker("L1", "small"),
        Locker("L2", "medium"),
        Locker("L3", "large")
    ]

    locker_system = LockerSystem(lockers)

    # Create People
    customer = Customer("C1", "Alice")
    agent = DeliveryAgent("D1", "Bob")

    # Customer creates a package
    pkg1 = customer.create_package("medium")

    # Agent delivers the package
    agent.deliver_package(locker_system, pkg1)

    # Customer requests pickup
    agent.pickup_package(locker_system, pkg1.package_id)