#Program 1 Gymnastics
#Owen O'Neil
#05/20/24


def Score_Calculator():
    f= open('scores.csv','r')#read file holding text
    finalscores=[]
    names = []

    for line in f:
        line = line.rstrip("\n")#strip right most 
        line = line.split(",")
        newarray=[]#new array wihtout names
        for i in range(1, len(line)):
            newarray.append(float(line[i]))#adds numbers to new array excluding names   
            newarray.sort()#sorts new array 
        high = max(newarray)# although not neccisary- this finds max
        low = newarray[0]#although not neccisary- this finds min
        del newarray[0] #deletes lowest number
        del newarray[-1]#deletes highest number
        total = sum(newarray)#find sum
        average= total/len(newarray)#use sum to find average score 
        print("{} earned {:.4f}".format(line[0], average))
        finalscores.append(average)#put all averages into an array
        names.append(line[0])#give all names inot one array
        
    index = finalscores.index(max(finalscores))#find max of the averages array
    print("First place is {} with {:.4f} points".format(names[index],finalscores[index]))#use .format to implament the max average that corresponds with the name
    firstplace = finalscores[index]
    del finalscores[index]#deletes the max score to allow there to be a new max score for repeat or second place
    del names[index]#deletes corresponding name to allow the next max score to correspond with the next max score's name
    first_repeat_indexes = []#new array to allow repeats to be added into it for first place only
    for number in range(len(finalscores)):
        if finalscores[number] == firstplace:#if final score of first place has a repeat, it will add the number to the array
            first_repeat_indexes.append(number)
    for i in first_repeat_indexes: 
        print("First place is {} with {:.4f} points".format(names[index],finalscores[index]))#calls new max number and the new name corresponding to it
    
    index = finalscores.index(max(finalscores))#get new max score 
    print("Second place is {} with {:.4f} points".format(names[index],finalscores[index]))#use .format to implament the max average that corresponds with the name
    secondplace = finalscores[index]#give the max score a variable 
    del finalscores[index]#deletes the max score to allow there to be a new max score for repeat or third place
    del names[index]#deletes corresponding name to allow the next max score to correspond with the next max score's name
    second_repeat_indexes = []#new array to allow repeats to be added into it for second place only
    for number in range(len(finalscores)):
        if finalscores[number] == secondplace:#if final score of second place has a repeat, it will add the number to the array
            second_repeat_indexes.append(number)
    for i in second_repeat_indexes:
        print("Second place is {} with {:.4f} points".format(names[index],finalscores[index]))#calls new max number and the new name corresponding to it
    
    index = finalscores.index(max(finalscores))
    print("Third place is {} with {:.4f} points".format(names[index],finalscores[index]))#use .format to implament the max average that corresponds with the name
    thirdplace = finalscores[index]#give the max score a variable 
    del finalscores[index]#deletes the max score to allow there to be a new max score for repeat
    del names[index]#deletes corresponding name to allow the next max score to correspond with the next max score's name
    third_repeat_indexes = []#new array to allow repeats to be added into it for third place only
    for number in range(len(finalscores)):
        if finalscores[number] == thirdplace:#if final score of third place has a repeat, it will add the number to the array
            third_repeat_indexes.append(number)
    for i in third_repeat_indexes:
        print("Third place is {} with {:.4f} points".format(names[index],finalscores[index]))#calls new max number and the new name corresponding to it
    
    

Score_Calculator()#call subroutine




