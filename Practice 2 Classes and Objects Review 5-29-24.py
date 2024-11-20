#Practice 2 Classes and Objects Review
#5/29/24

#1. The name of the class is ToDoList and the object is todo_list

#2. 20,2,3,21,4,5,6,22,4,5,6,23,13,14,16,17,18,19,24,7,8,9,10,25,7,8,11,12,26,13,14,16,17,18,19

#3. Getters and setter allow the user to keep set atrabutes when creatign logic later in the code and makes writing the code much more flexible.	
    # It's also easier to acess atrabutes and properties directly

#4.
    
class Package:
    def __init__(self, destination: str, weight: float, cost_per_ounce: float):
        self.destination = destination
        self.weight = weight
        self.cost_per_ounce = cost_per_ounce
        
    def getDestination(self):
        return self._destination
    def getWeight(self):
        return self._weight
    def getCost_per_ounce(self):
        return self._cost_per_ounce
    
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
    
    
    def total_cost(self):
        return self._weight * self._cost_per_ounce
    
    def __str__(self):
        return ("Package going to {} weighs {:.2f}; costs to ship = ${:.2f}".format(self._destination, self.weight, self.total_cost()))
    
##MAIN PROGRAM##

package1 = Package("New York", 8, 3)
package2 = Package("Boston", 5, 2)
package3 = Package("Tampa", 10, 4)
package4 = Package("Bristol", 3, 1)
package5 = Package("Chicago", 22, 10)
package6 = Package("Vermont", 4, 5)
print(package1)
print(package2)
print(package3)
print(package4)
print(package5)
print(package6)
        
    