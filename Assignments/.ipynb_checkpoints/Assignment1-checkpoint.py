class Multiply:
    def __init__(self):
        self.__numOne = int(input("Please Enter The First Number: "))
        self.__numTwo = int(input("Please Enter The Second Number: "))
        # self.__numOne = -981
        # self.__numTwo = 1234
        self.__negOne = False
        self.__negTwo = False
        
        if (self.__numOne < 0):
            self.__negOne = True
            self.__numOne = abs(self.__numOne)
        
        if (self.__numTwo < 0):
            self.__negTwo = True
            self.__numTwo = abs(self.__numTwo)
            
        
        self.__finalResult = []
        self.__lenOne = len(str(self.__numOne))
        self.__lenTwo = len(str(self.__numTwo))
        self.__strNumOne = str(self.__numOne)
        self.__strNumTwo = str(self.__numTwo)
        
    def LenCheck(self):
        if (self.__numOne < 0):
            self.__numOne = abs(self.__numOne)
        
        if (self.__numTwo < 0):
            self.__numTwo = abs(self.__numTwo)
        
        if (self.__lenOne % 2 != 0):
            self.__lenOne += 1
            self.__strNumOne = '0' + self.__strNumOne 


        if (self.__lenTwo % 2 != 0):
            self.__lenTwo += 1
            self.__strNumTwo = '0' + self.__strNumTwo 
                
    def DivideAndConquer(self):
        indexOne, indexTwo, shift, temp = 0, 0, 0, 0
        tempLenOne, tempLenTwo = self.__lenOne, self.__lenTwo
        
        print("Result: \n")
        for i in range( max(self.__lenOne, self.__lenTwo)//2 ):
            firstPair  = self.__strNumOne[indexOne : indexOne+2] #09
            shift = tempLenOne - len(firstPair)
            tempLenOne = shift
            
            for j in range( min(self.__lenOne, self.__lenTwo)//2 ):
                secondPair = self.__strNumTwo[indexTwo : indexTwo+2] #12
                

                shift += tempLenTwo - len(secondPair)
                tempLenTwo = tempLenTwo - len(secondPair)
                
                # print(firstPair, " ", secondPair)
                
                temp = str( int(firstPair) * int(secondPair) ) + ('0' * shift)
                print(f"{firstPair} X {secondPair} = {str( int(firstPair) * int(secondPair) ) + ('.' * shift)}")
                self.__finalResult.append(int(temp))
                indexTwo += 2
                shift = tempLenOne
                
                
            indexOne += 2
            indexTwo = 0
            tempLenTwo = self.__lenTwo
            
            
        
                
    def Result(self):
        result = sum(self.__finalResult)
        if ( (self.__negOne == True and self.__negTwo != True) or (self.__negOne != True and self.__negTwo == True) ):
            result *= -1
            if self.__negOne == True:
                self.__numOne *= -1
            else:
                self.__numTwo *= -1
        
        print(f"__________________\n{self.__numOne} X {self.__numTwo} = {result}")
        
        
        
obj = Multiply()
obj.LenCheck()
obj.DivideAndConquer()
obj.Result()