# fuel cost calculator
class FuelCalculator:
    def __init__(self):
        self.distance = 0
        self.vehicle_mileage = 0
        self.fuel_price = 0

    def getDetails(self):
        self.distance = float(input("Enter Distance travelled (km): "))
        self.vehicle_mileage = float(input("Enter Vehicle mileage (km/L): "))
        self.fuel_price = float(input("Enter Fuel price (₹/L): "))

    def calculate_fuel_cost(self):
        calc = self.distance / self.vehicle_mileage
        cost = calc * self.fuel_price
        return calc, cost

    def display_results(self, fuel_required, fuel_cost):
        print("\n-----Fuel Calculator-----\n")
        print("\n Distance: ", self.distance)
        print("\n Vehicle mileage: ", self.vehicle_mileage)
        print("\n Fuel price: ", self.fuel_price)
        print("\n-------------------------------------\n")
        print("Fuel required: ", fuel_required)
        print("Fuel cost: ", fuel_cost)
l1 = FuelCalculator()
l1.getDetails()
fuel_required, fuel_cost = l1.calculate_fuel_cost()
l1.display_results(fuel_required, fuel_cost)
