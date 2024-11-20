#Practice 3: Inheritance and Overloading Review
# 5/30/24

#parent class
class Package:
    def __init__(self, destination: str, weight: float, cost_per_ounce: float):
        self.destination = destination
        self.weight = weight
        self.cost_per_ounce = cost_per_ounce
    #getters   
    def getDestination(self):
        return self._destination
    def getWeight(self):
        return self._weight
    def getCost_per_ounce(self):
        return self._cost_per_ounce
    #setter
    def setDestination(self, destination: str):
        self._destination = destination
    def setWeight(self, weight: float):
        if weight > 0:
            self._weight = weight
        else:
            return("Weight must be greeater than 0")
    def setCost_per_ounce(self, cost_per_ounce: float):
        if cost_per_ounce > 0:
            self._cost_per_ounce = cost_per_ounce
        else:
            return("Cost per ounce must be grater than 0")
    
    destination = property(getDestination, setDestination)
    weight = property(getWeight, setWeight)
    cost_per_ounce = property(getCost_per_ounce, setCost_per_ounce)
    
    #methods
    #find total cost
    def total_cost(self):
        return self._weight * self._cost_per_ounce
    
    def __str__(self):
        return ("Package going to {} weighs {:.2f}; costs to ship = ${:.2f}".format(self._destination, self.weight, self.total_cost()))

#child class
class FastPackage(Package):
    def __init__(self, destination, weight, cost_per_ounce, days):
        super().__init__(destination, weight, cost_per_ounce)
        self.days = days
        self.setDays(days)

    #getters    
    def getDays(self):
        return self._days
    def getFee(self):
        return self._fee
    #setter
    def setDays(self, days: int):
        self._days = days
        if days == 1:
            self._fee = 10
        elif days == 2:
            self._fee = 8
        elif days == 3:
            self._fee = 5
        else:
            raise ValueError("Days must be 1, 2, or 3")
    def setFee(self, fee: float):
        self._fee = fee
        
    days = property(getDays, setDays)
    fee = property(getFee, setFee)
    #methods
    #overload total cost  
    def total_cost(self):
       return super().total_cost() + (self._fee * self._weight)
    #overload __str__
    def __str__(self):
        return ("Package going to {} weighs {:.2f}; costs to ship = ${:.2f}. This package will take {} day(s) to deliver.".format(self._destination, self.weight, self.total_cost(), self._days))
        
        
##MAIN PROGRAM##

#customer transaction
def main():
    PackageArray = []

    while True:
        print("1. Customer Transaction")
        print("2. End of day Report")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":           
            destination = input("1. Where is the package going?: ")
            package_type = input("2. What kind of package is it (regular or fast)?: ").lower()
            weight = float(input("3. What is the weight of your package?: "))
            cost_per_ounce= float(input("4. What is the cost per ounce?: "))
            if package_type == "fast":
                days = int(input("How many days do you want until the package arrives (1,2, or 3)?: "))
                package = FastPackage(destination, weight, cost_per_ounce, days)
            else:
                package = Package(destination, weight, cost_per_ounce)
            
            PackageArray.append(package)
            print("The cost to ship the package is ${:.2f}".format(package.total_cost()))
            print("")
         
        elif choice == "2":
            print("End of day report")
            PackageArray.sort(key=lambda x: x.total_cost(), reverse=True)
            for package in PackageArray:
                print(package)
            gross_cost= sum(pkg.total_cost() for pkg in PackageArray)
            print("Total cost for all packages: ${:.2f}".format(gross_cost))
            break
        else:
            print("Invalid choice, please try again")

        
main()

    
