#Program 2: Emulatig Circuts
#6/4/24
#Owen O'Neil

class Gate:#parent class
    def __init__(self, inputs):
        self.inputs = inputs
        
    def evaluate(self):
        return 0
    
    #Getter
    def get_inputs(self):
        return sefl._inputs
    #setter
    def set_inputs(self,newvalue):
        self._inputs = newvalue
    
#AND Gate
class AND(Gate):
    def __init__(self, inputs):
        super().__init__(inputs)#getting parent subclass
        
    def evaluate(self):        
        if self.inputs[0] == 1 and self.inputs[1] == 1:#if inputs are both 1 return 1 otherwise return 0
            return "1"
        else:
            return "0"
        
#OR Gate
class OR(Gate):
    def __init__(self, inputs):
        super().__init__(inputs)#getting parent subclass
        
    def evaluate(self):
        if self.inputs[0] == 0 and self.inputs[1] == 0:#if inputs are both 0 return 0 otherwise return 1
            return "0"
        else:
            return "1"    
        
#NOT Gate       
class NOT(Gate):
    def __init__(self, inputs):
        super().__init__(inputs)#getting parent subclass
        
    def evaluate(self):
        if self.inputs[0] == 0:#if the input is a 0 return 1 otherwise return 0 
            return "1"
        else:
            return "0"
        
#NAND Gate      
class NAND(Gate):
    def __init__(self, inputs):
        super().__init__(inputs)#getting parent subclass
        
    def evaluate(self):
        if self.inputs[0] == 0 and self.inputs[1] == 0:# if inputs are both 0 return 1 otherwise return 0 
            return "1"
        else:
            return "0"

#Circuit1 Gate
class Circuit1(Gate):
    def __init__(self, inputs):
        super().__init__(inputs)#getting parent subclass
        
    def evaluate(self):
        and1 = AND([self.inputs[0],self.inputs[1]])#create variable to allow different indexes to go into AND Gate subclass
        not1 = NOT([self.inputs[2]])#same here 
        if and1.evaluate() == "1":#if the product of the AND Gate class is 1 return 1 
            return "1"
        elif not1.evaluate() == "1":#if the product of the NOT Gate class is 1 return 1
            return "1"
        else:
            return "0"#otherwise return 0


class Circuit2(Gate):
    def __init__(self, inputs):
        super().__init__(inputs)#getting parent subclass
        
    def evaluate(self):
        and1 = AND([self.inputs[0], self.inputs[1]])#create variable to allow different indexes to go into AND Gate subclass
        and2 = AND([self.inputs[0], self.inputs[2]])#same here but givin differetn indexes than the first one 
        not1 = NOT([self.inputs[2]])#same here but for the NOT Gate
        if and1.evaluate() == "0" and not1.evaluate() == "1":#if the product of the AND Gate is 0 and the Product of the NOT Gate is 1 return 1
            return "1"
        elif and2.evaluate() == "1" and not1.evaluate() == "1":# if the product of the AND gate using a the 0 and 2 index is 1 and the NOT Gate is 1 return 1
            return "1"
        else:
            return "0"#otherwise return 0 
        
        
##Main PROGRAM##

and1 = AND([])#create a list for AND Gate 

print("AND Gate")
print("A B Out")
for i in  range(0,2):#for loop to create the arpopriate different 0 and 1 indexes 
    for j in range(0,2):
        and1.inputs = [i,j]#letter represent the indexes 
        print (i, j, and1.evaluate())#print the indexes along with the product
print()#space in between tables

or1 = OR([])#create list for OR Gate

print("OR Gate")
print("A B Out")
for i in  range(0,2):#for loop to create the arpopriate different 0 and 1 indexes
    for j in range(0,2):
        or1.inputs = [i,j]#letter represent the indexes 
        print (i, j, or1.evaluate())#Print the indexes along with the product
print()#space in between tables

listNOT1 = [1]#NOT gate only uses one input so no need for a for loop 
listNOT2 = [0]#same here

not1 = NOT(listNOT1)#put the list into the NOT Gate
not2 = NOT(listNOT2)#same here
print("NOT Gate")
print("A Out")
print("{} {}".format(listNOT1[0], not1.evaluate()))#print number used and product
print("{} {}".format(listNOT2[0], not2.evaluate()))#same here
print("B Out")
print("{} {}".format(listNOT1[0], not1.evaluate()))#same here 
print("{} {}".format(listNOT2[0], not2.evaluate()))#same here
print()#space in between tables

nand1 = NAND([])#create list for NAND Gate

print("NAND Gate")
print("A B Out")
for i in  range(0,2):
    for j in range(0,2):#for loop to create the arpopriate different 0 and 1 indexes
        nand1.inputs = [i,j]#letter represent the indexes 
        print (i, j, nand1.evaluate())#print the indexes along with the product 
print()#space in between tables


circuit1 = Circuit1([])#create a list for the Circuit1 Gate

print("Circuti1 Gate")
print("A B C Out")
for i in  range(0,2):
    for j in range(0,2):
        for k in range(0,2):#create a for loop to get the different 0, 1, and 2 index combinations
            circuit1.inputs = [i,j,k]#letter represent the indexes 
            print (i, j, k, circuit1.evaluate())#print all indexes along with product
print()#space in between tables


circuit2 = Circuit2([])#create a list for the Circuit2 Gate

print("Circuit2 Gate")
print("P Q R Out")
for i in  range(0,2):
    for j in range(0,2):
        for k in range(0,2):#create a for loop to get the different 0, 1, and 2 index combinations
            circuit2.inputs = [i,j,k]
            print (i, j, k, circuit2.evaluate())#print all indexes along with product




