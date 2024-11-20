#Program 3: Bears and Fish
#6/12/24
#Owen O'Neil

import random
import abc
class Animal(metaclass = abc.ABCMeta):# Animal class with the abstracte method
    def __init__(self):
        self.strength = random.randint(1, 5)#randomize the strength
        self.isFemale = random.randint(0, 1)#randomize if its a female
        self.death_count = 0

    #getters
    def getStrength(self):
        return self.strength
    def getIsFemale(self):
        return self.isFemale
    def getDeath_count(self):
        return self.death_count
    #setters
    def setStrength(self, newvalue):
        self.strength = newvalue

    def setIsFemale(self, newvalue):
        self.isFemale = newvalue

    def setDeath_count(self, newvalue):
        self.death_count = newvalue

    _strength = property(getStrength, setStrength)
    _isFemale = property(getIsFemale, setIsFemale)
    _death_count = property(getDeath_count, setDeath_count)

    @abc.abstractmethod
    def move(self): #use abstractmethod for move
        pass

    def increase_death_count(self):#increase deathcount.(Not used in main code)
        self.death_count += 1

    def __eq__(self, other):#overide equal function
        return self.isFemale == other.isFemale

    def __gt__(self, other):#overide greater than function
        return self.strength > other.strength

class Bear(Animal): #Bear class
    def __init__(self):
        super().__init__()#get Animal __init__

    def Fight(self, other): #bear fight method
        if self.strength > other.strength:
            return True
        else:
            return False
    def Eat(self, other): #bear eat method
        if str(other) == "F" and not other.Flee(): #bear can eat the fish if the flee method returns false
            return True
        else:
            return False

    def Mate(self):#bear mate method
        return Bear() #return 1 bear object

    def move(self):#determine bear method
        return random.choice([-1,1]) #randomly choose if the bear will move forwards one or backwards one

    def __str__(self): #"B" represents a bear method on the River array
        return ("B")


class Fish(Animal): #Fish class
    def __init__(self):
        super().__init__() #get Animal __init__

    def Fight(self, other): #fish fight method
        if self.strength > other.strength: #increasing the death count depending on strength
            self.death_count += 1
        else:
            other.death_count += 1

    def Mate(self): #fish mate method
        return [Fish(), Fish(), Fish()] #return an array with 3 fish objects

    def Flee(self): #fish flee method
        return random.uniform(0,1) >= 0.8 #randomly chose if the fish will escape or not

    def move(self): #fish move method
        return random.choice([-1, 1]) #randomly chooses if the fish will move forward one or backward one

    def __str__(self):
        return ("F") # "F" represents a fish object on the River array

##MAIN PROGRAM##
River = [] #River array
count = 0 #count how many times a element is placed
RiverCount = 0#count how many times the River simulation will run
while count < 50: #stop adding elements after 50
    RanNum = random.randint(1, 10)#randomly chose a number to determine what element will be places
    if RanNum == 1: #if 1, add a bear element
        River.append(Bear())
    elif RanNum == 2 or RanNum == 3 or RanNum == 4 or RanNum == 5: #if 2,3,4,5, add a fish element
        River.append(Fish())
    else:
        River.append("_")# otherwise add a space element
    count += 1
for animal in River:
    print(str(animal), end ="")
print()
while RiverCount < 100:
    for i in range(len(River)):
        if str(River[i]) != "_" and River[i].death_count >= 5: #replace index with space if it isnt already a space and the deathcount is greaterthan equal to 5
            River[i] = "_"
        if str(River[i]) == "B": #if the current index is "B"
            shift = River[i].move() #determine if it will move +1 or -1
            if shift == -1:
                if i-1 >= 1 and str(River[i-1]) == "B": #if -1 and there is another space to the left in the array and there is a bear
                    if River[i-1].isFemale == 0: #if its not female, the 2 bears fight
                        if River[i].Fight(River[i-1]):#if fight = true
                            River[i-1] = River[i]
                            River[i]  = "_"#re define the indexes
                        else:
                            River[i] = River[i-1] #if false re define the indexes
                            River[i-1] = "_"
                    else:
                        B_child = River[i].Mate() #If female = true, mate the 2 bears and create a bear object in a random empty space in the river array
                        possible_places = []
                        k = 0
                        while k < len(River):
                            if str(River[k]) == "_":
                                possible_places.append(k) #add the index of the empty space to the possible place array
                            k += 1 #do it for the length of the River array
                        if len(possible_places) >= 1: #if there is a empty space avalible add the bear object to the array
                            New_index = random.choice(possible_places)
                            River[New_index] = B_child


                elif i-1 >= 1 and str(River[i-1]) == "F": #if the space to the right is a fish eat the fish if
                    if River[i].Eat(River[i-1]): #if the fish doesnt escape eat it and re define the indexes
                        River[i-1] = River[i]
                        River[i] = "_"



            else:
                if i+1 <= 49 and str(River[i+1]) == "B": #same thing if there is a bear but if it is +1
                    if River[i+1].isFemale == 0:
                        if River[i].Fight(River[i+1]):
                            River[i+1] = River[i]
                            River[i]  = "_"
                        else:
                            River[i] = River[i+1]
                            River[i+1] = "_"

                    else:
                        B_child = River[i].Mate()
                        possible_places = []
                        k = 0
                        while k < len(River):
                            if str(River[k]) == "_":
                                possible_places.append(k)
                            k += 1
                        if len(possible_places) >= 1:
                            New_index = random.choice(possible_places)
                            River[New_index] = B_child
                        #find the places in the river where there is "_"
                        #put those places in the possible_places array- .append(possible_places)
                        #use random choice to get a random index in the possible_places array
                        #using that index, swap "_" with B_child
                        #do this once

                elif i+1 <= 49 and str(River[i+1]) == "F":#same thing as before but if the fish is +1 index forward
                    if River[i].Eat(River[i+1]):
                        River[i+1] = River[i]
                        River[i] = "_"

        elif str(River[i]) == "F": #if the current index is female
            shift = River[i].move()#call the move method to determine where it will move
            if shift == -1: #if shift is -1
                if i-1 >= 1 and str(River[i-1]) == "B": #if there is bear, call flee method
                    if not River[i].Flee():#if not flee method, fish dies and replace index with space
                        River[i] = "_"

                elif i-1 >= 1 and str(River[i-1]) == "F": #if index to the left is a fish
                    if River[i].isFemale == 0:#if fish is a male fight but don't kill them
                        River[i].Fight(River[i-1])

                    else: #if female mate with fish
                        k = 0
                        F_child = River[i].Mate()#fish mate mehod with and array of 3 fish objects
                        possible_places = []#possible places array
                        while k < len(River):
                            if str(River[k]) == "_":
                                possible_places.append(k) #add all of the space indexes to the possible places array
                            k += 1
                        if len(possible_places) >= 3: #for the 3 fish objects in the array, get a index at random and replace it with a fish object
                            New_index = random.choice(possible_places)
                            River[New_index] = F_child[0]
                            New_index = random.choice(possible_places)
                            River[New_index] = F_child[1]
                            New_index = random.choice(possible_places)
                            River[New_index] = F_child[2]


            else:
                if i+1 <= 49 and str(River[i+1]) == "B": #same thing as the -1 but if the bear is +1 index
                    if not River[i].Flee():
                        River[i] = "_"

                elif i+1 <= 49 and str(River[i+1]) == "F":#same thing as the -1 but if the fish is +1 index
                    if River[i].isFemale == 0:
                        River[i].Fight(River[i+1])
                    else:
                        k = 0
                        F_child = River[i].Mate()
                        possible_places = []
                        while k < len(River):
                            if str(River[k]) == "_":
                                possible_places.append(k)
                            k += 1
                        if len(possible_places) >= 3:
                            New_index = random.choice(possible_places)
                            River[New_index] = F_child[0]
                            New_index = random.choice(possible_places)
                            River[New_index] = F_child[1]
                            New_index = random.choice(possible_places)
                            River[New_index] = F_child[2]

    RiverCount += 1 #add 1 to the Rivercount to eventually end the while loop
    for animal in River:
        print(str(animal), end="") #pring the animals next to eachother
    print()#print the new River
















