#created by Orlando Lewis founder of the future company Swerf Tech 
class FlightInfo:
    #initialzing the attributes of this class 
    def __init__(self,fname,destination,ftime,fgate):
        self.__destination=destination
        self.__fname=fname
        self.__ftime=ftime
        self.__fgate=fgate



    #creating the accessors and mutators
    def getDestination(self):
        return self.__destination
    def setDestination(self,destination):
        self.__destination= destination



    def getFlightName(self):
        return self.__fname
    def setFlightName(self,fname):
        self.__fname= fname



    def getFlightTime(self):
        return self.__ftime
    def setFlightTime(self,ftime):
        self.__ftime=ftime



    def getFlightGate(self):
        return self.__fgate
    def setFlightGate(self,fgate):
        self.__fgate=fgate






#creating a subclass of the FlightInfo class
class PassengerInfo(FlightInfo):
    #initializing the attributes 
    def __init__(self,pname,tnum,fname,destination,ftime,fgate,seat):
        FlightInfo.__init__(self,fname,destination,ftime,fgate)


        self.__pname=pname
        self.__tnum= tnum
        self.__seat= seat
      


    #creating the accessors and mutators
    def getPassengerName(self):
        return self.__pname

    def setPassengername(self,pname):
        self.__pname = pname



    def getTicketNumber(self):
        return self.__tnum

    def setTicketNumber(self,tnum):
        self.__tnum = tnum 


    def getSeat(self):
        return self.__seat

    def setTicketNumber(self,seat):
        self.__seat=seat
    
    
    
  #creating a subclass of the PassengerInfo class  
class NewPassengerInfo(PassengerInfo):

      def __init__(self,pname,tnum,fname,destination,ftime,fgate,seat):
       
        #initialzing the attributes of this class
        PassengerInfo.__init__(self,pname,tnum,fname,destination,ftime,fgate,seat)


        #creating the accessors and mutators
        def getSeat(self):
            return self.__seat

        def setSeat(self,seat):
            self.__seat ='Standby' #using polymorphism 
           
        
        
        
   


