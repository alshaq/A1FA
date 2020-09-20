#created by Orlando Lewis founder of the future company Swerf Tech 
class FlightValidations():
    #initialzing the attributes of this class 

    def __init__(self,pName,pChoice):
        self.__pName= pName
        self.__choice= pChoice





    #creating a validation method for the main program. Validating if the user enters a correct name with alpha
    def valPassengerName(pName):
        
        valid= True
        while valid==True:
            if pName.isalpha() :
                
                break
            else:
                pName=input("\nYou have entered an invalid name , please enter your correct first\last name: ")

        return str(pName)



  #creating the accessors and mutators
    def setPassengername(self,pName):

        self.__pName= pName

    def getPassengerName(self):
        return self.__pName




    #creating a validation method for the main program.checking if the user enters the corresponding number for the menu
    def valPassengerchoice(pChoice):
        
        valid= True
        while valid==True:
            if pChoice.isdigit():
                
                break
            else:
                pName=input("\nYou have entered an valid choice: ")

        return pChoice


    #creating the accessors and mutators
    def setPassengerChoice(self,pName):

        self.__choice= pChoice





