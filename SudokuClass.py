import pandas as pd
import math
import copy

class Sudoku:
    def __init__(self , data):
        self.data = data
        
    def writeFile(self):
        complete = pd.DataFrame(self.data)
        complete.to_csv("Answer.csv" , header = None , index = None)

    def isnan(self , num):
        try:
            return math.isnan(num)
        except:
            return False

    def blockchecker(self, num):
            if num == 0 or num == 1 or num == 2:
                return [0,1,2]

            elif num == 3 or num == 4 or num == 5:
                return[3,4,5]

            elif num == 6 or num == 7 or num == 8:
                return[6,7,8] 
 
    def Method1(self):
        linecount = -1
        numbercount = -1
        
        for line in self.data:
            linecount += 1
            numbercount = -1
            
            for number in line:
                numbercount += 1
                if True:

    # Removing the values of the number from the values possible for the number from a horizontal strip of 3 lines
                    pos = [[],[[0,1,2],[3,4,5],[6,7,8]]]
                    pos[0] = self.blockchecker(linecount)
                    pos[0].remove(linecount)
                    pos[1].remove(self.blockchecker(numbercount))



    #Checking for duplicates in the same strip
                    temppo = copy.deepcopy(pos)
                    for line in pos[0]:
                        duplicounter = -1
                        for num in self.data[line]:
                            duplicounter += 1               
                            if num == number:
                                temppo[0].remove(line)
                                temppo[1].remove(self.blockchecker(duplicounter))

                    pos = copy.deepcopy(temppo)

                    if len(pos[0]) == 1:
                        for i in pos[0]:
                            for l in pos[1]:
                                for g in l:
                                    checkVar = self.data[i][g]
                                    if not(self.isnan(self.data[i][g])):
                                        temppo[1][0].remove(g)
                        
                        pos = copy.deepcopy(temppo)
                        for hzline in pos[1][0]:
                            linecounter = 0
                            while linecounter < 9:
                                if self.data[linecounter][hzline] == number:
                                    pos[1][0].remove(hzline)

                                linecounter += 1

                        



                        if len(pos[1][0]) == 1 and len(pos[0]) == 1:
                            self.data[pos[0][0]][pos[1][0][0]] = number

    def Method2(self):
        checkVar = None
        tempdata = [[],[],[],[],[],[],[],[],[]]
        for i in self.data:
            tempdata[0].append(i[0])
            tempdata[1].append(i[1])
            tempdata[2].append(i[2])
            tempdata[3].append(i[3])
            tempdata[4].append(i[4])
            tempdata[5].append(i[5])
            tempdata[6].append(i[6])
            tempdata[7].append(i[7])
            tempdata[8].append(i[8])
        linecount = -1
        numbercount = -1
        
        for line in tempdata:
            linecount += 1
            numbercount = -1
            
            for number in line:
                numbercount += 1
                if True:

    # Removing the values of the number from the values possible for the number from a horizontal strip of 3 lines
                    pos = [[],[[0,1,2],[3,4,5],[6,7,8]]]
                    pos[0] = self.blockchecker(linecount)
                    pos[0].remove(linecount)
                    pos[1].remove(self.blockchecker(numbercount))



    #Checking for duplicates in the same strip
                    temppo = copy.deepcopy(pos)
                    for line in pos[0]:
                        duplicounter = -1
                        for num in tempdata[line]:
                            duplicounter += 1               
                            if num == number:
                                temppo[0].remove(line)
                                temppo[1].remove(self.blockchecker(duplicounter))

                    pos = copy.deepcopy(temppo)

                    if len(pos[0]) == 1:
                        for i in pos[0]:
                            for l in pos[1]:
                                for g in l:
                                    checkVar = tempdata[i][g]
                                    if not(self.isnan(tempdata[i][g])):
                                        temppo[1][0].remove(g)
                        
                        pos = copy.deepcopy(temppo)
                        for hzline in pos[1][0]:
                            linecounter = 0
                            while linecounter < 9:
                                if tempdata[linecounter][hzline] == number:
                                    pos[1][0].remove(hzline)

                                linecounter += 1

                        



                        if len(pos[1][0]) == 1 and len(pos[0]) == 1:
                            tempdata[pos[0][0]][pos[1][0][0]] = number
        self.data = [[],[],[],[],[],[],[],[],[]]

        for i in tempdata:
            self.data[0].append(i[0])
            self.data[1].append(i[1])
            self.data[2].append(i[2])
            self.data[3].append(i[3])
            self.data[4].append(i[4])
            self.data[5].append(i[5])
            self.data[6].append(i[6])
            self.data[7].append(i[7])
            self.data[8].append(i[8])   

    
    def Method3(self):
        linecount = -1
        for line in self.data:
            linecount += 1
            numbers = [1,2,3,4,5,6,7,8,9]
            for number in line:
                if not self.isnan(number):
                    numbers.remove(number)
            if len(numbers) == 1:
                numbercount = -1
                for number in line:
                    numbercount += 1
                    if self.isnan(number):
                        self.data[linecount][numbercount] = numbers[0]

    
    def Method4(self):
        tempdata = [[],[],[],[],[],[],[],[],[]]
        for i in self.data:
            tempdata[0].append(i[0])
            tempdata[1].append(i[1])
            tempdata[2].append(i[2])
            tempdata[3].append(i[3])
            tempdata[4].append(i[4])
            tempdata[5].append(i[5])
            tempdata[6].append(i[6])
            tempdata[7].append(i[7])
            tempdata[8].append(i[8])

        linecount = -1
        for line in tempdata:
            linecount += 1
            numbers = [1,2,3,4,5,6,7,8,9]
            for number in line:
                if not self.isnan(number):
                    numbers.remove(number)
            if len(numbers) == 1:
                numbercount = -1
                for number in line:
                    numbercount += 1
                    if self.isnan(number):
                        tempdata[linecount][numbercount] = numbers[0]


            self.data = [[],[],[],[],[],[],[],[],[]]

        for i in tempdata:
            self.data[0].append(i[0])
            self.data[1].append(i[1])
            self.data[2].append(i[2])
            self.data[3].append(i[3])
            self.data[4].append(i[4])
            self.data[5].append(i[5])
            self.data[6].append(i[6])
            self.data[7].append(i[7])
            self.data[8].append(i[8])

        
    def Method5(self):
        blocks = [[0,1,2],[3,4,5],[6,7,8]]
        for block in blocks:
            for blck in blocks:
                numbers  = [1,2,3,4,5,6,7,8,9]
                for i in block:
                    for n in blck:
                        if not self.isnan(self.data[i][n]):
                            numbers.remove(self.data[i][n])



                
    def Method6(self):
        linecount = -1
        numbers = [1,2,3,4,5,6,7,8,9]
        blocks = [[0,1,2],[3,4,5],[6,7,8]]
        for line in self.data:
            linecount += 1
            numbercount = -1
            for number in line:
                numbercount += 1
                if self.isnan(number):
                    numbers = [1,2,3,4,5,6,7,8,9]
                    for number2 in line:
                        if number2 in numbers:
                            numbers.remove(number2)
                    for lines in self.data:
                        if lines[numbercount] in numbers:
                            numbers.remove(lines[numbercount])
                    
                    for block in self.blockchecker(linecount):
                        for blk in self.blockchecker(numbercount):
                            if self.data[block][blk] in numbers:
                                numbers.remove(self.data[block][blk])


                    if len(numbers) == 1:
                        self.data[linecount][numbercount] = numbers[0]
