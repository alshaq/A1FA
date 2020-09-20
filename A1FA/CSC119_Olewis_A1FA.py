#created by Orlando Lewis
import time
import Flight
import FlightValidations





def main():
    #Displayimg the information about the program
    header()
   
        

    #initializing variables
    flight1="D143"
    flight2="B157"
    flight3="K260"
    flight4="J791"
    numFlights=0
    rep='y'
    slash="-"


    #initializing  lists 
    allFlight=[]
    flightMiami=['D143','K260']
    flightJamaica=['B157','J791']

    airlines=["Delta","British Airlines","Air Jamaica","King's Airways"]
    airlinesNum=["800-654-7565","800-324-6753","800-344-3442","800-244-7659"]




    #initializing tuple
    CustomerCare=("800","767","8890")



    #initializing dictionaries
    D143={'Time': '7:00', 'Destination':'Miami','Gate':'G1'}
    B157={'Time': '6:30', 'Destination':'Jamaica','Gate':'F2'}
    K260={'Time': '17:00', 'Destination':'Miami','Gate':'G10'}
    J791={'Time': '18:00', 'Destination':'Jamaica','Gate':'F5'}




    #using the try statement to catch all the exceptions
    try:


        #while loop so the program repeats if the user want to use it again
        while (rep =='y' or rep=='Y'):



            time.sleep(0.9) # sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
        #asking the user to choose from a menu 


            print("\nChoose from the menu by entering the corresponding number:")
 

            print("1) Check Flights\n2) Change Flights\n3) All Flight\n4) Exit")


            choice = int(input(">>> "))


            v_alidate=FlightValidations.FlightValidations
            



            print("\n\n")
    
            #using a decision statement to figure ou what the user selected
            if choice ==1 :

                print ("CHECKS FLIGHTS\n__________________\n")


                time.sleep(0.9) #sleep class from the time module to give breaks in between output so the user is not bombard with output
        

                #calling the displayflight function to show the flights
                displayFlights() 
        


            elif choice== 2:

                print("CHANGE FLIGHTS\n__________________\n")

                print("Changing the flight is free however your seat will not be secured.\nYou will be placed on standby.\n")



                time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
                


                #asking the user to enter information that will be needed later on in the program for proccessing and to change their flight
                p_firstname=input("Please enter your firstname: ")
                p_firstname2=v_alidate.valPassengerName(p_firstname)
                p_lastname=input("Please enter your lastname: ")
                


                #validating the user input
              
                p_lastname2=v_alidate.valPassengerName(p_lastname)



                 #asking the user to enter information that will be needed later on in the program for proccessing and to change their flight
                p_ticket_code= input("\nPlease enter your ticket code(case sensitive): ")
                p_seat=input("\nEnter your seat letter and number: ")
                p_flight_nam=input("\nEnter flight number(Case sensitive): ")



                #putting together the student full name and creating the passkey to use to search for the passenger
                fullname=p_firstname2.upper()+" "+p_lastname2.upper()

                p_name_caps=p_firstname2.upper()+p_lastname2.upper()

                p_key= p_name_caps + p_ticket_code
               

                #open file to search for the passenger
                infile=open(p_flight_nam + '.txt','r')

                flight_file=infile.readlines()


                infile.close() #closing the file


                #go through the file to find the user

                for ch in flight_file:



                    #use a if statement to determine if the passenger in the file
                    if p_key in ch:



                    #if-elif-else statements deciding the flight the passenger is a part of
                            if p_flight_nam == flight1:
                                


                                time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
                                #creating an instance of the PassengerInfo class in the Flight module
                                passenger_info=Flight.PassengerInfo(fullname,p_ticket_code,p_flight_nam, D143['Destination'],D143['Time'],D143['Gate'],p_seat)


                                #using the get methods / accessors to get the information and then displaying them
                                print("Passenger Name: ",passenger_info.getPassengerName())
                                print("Ticket Code: ",passenger_info.getTicketNumber())
                                print("Flight Name: ",passenger_info.getFlightName())
                                print("Destination: ",passenger_info.getDestination())
                                print("Departure Time: ",passenger_info.getFlightTime())
                                print("Seat: ",passenger_info.getSeat())
                                print("Gate: ",passenger_info.getFlightGate())



                            elif p_flight_nam == flight2:
                                
                                time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
                                
                                      
                                                          
                               #creating an instance of the PassengerInfo class in the Flight module
                                passenger_info=Flight.PassengerInfo(fullname,p_ticket_code,p_flight_nam, B157['Destination'],B157['Time'],B157['Gate'],p_seat)


                                #using the get methods / accessors to get the information and then displaying them
                                print("Passenger Name: ",passenger_info.getPassengerName())
                                print("Ticket Code: ",passenger_info.getTicketNumber())
                                print("Flight Name: ",passenger_info.getFlightName())
                                print("Destination: ",passenger_info.getDestination())
                                print("Departure Time: ",passenger_info.getFlightTime())
                                print("Seat: ",passenger_info.getSeat())
                                print("Gate: ",passenger_info.getFlightGate())



                            elif p_flight_nam == flight3:
                                  
                                time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
                               

                                #creating an instance of the PassengerInfo class in the Flight module
                                passenger_info=Flight.PassengerInfo(fullname,p_ticket_code,p_flight_nam, K260['Destination'],K260['Time'],K260['Gate'],p_seat)
                                
                                

                                #using the get methods / accessors to get the information and then displaying them
                                print("Passenger Name: ",passenger_info.getPassengerName())
                                print("Ticket Code: ",passenger_info.getTicketNumber())
                                print("Flight Name: ",passenger_info.getFlightName())
                                print("Destination: ",passenger_info.getDestination())
                                print("Departure Time: ",passenger_info.getFlightTime())
                                print("Seat: ",passenger_info.getSeat())
                                print("Gate: ",passenger_info.getFlightGate())



                            elif p_flight_nam == flight4:
                                
                                time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
                                

                                #creating an instance of the PassengerInfo class in the Flight module
                                passenger_info=Flight.PassengerInfo(fullname,p_ticket_code,p_flight_nam,J791['Destination'] ,J791['Time'],J791['Gate'],p_seat)


                                #using the get methods / accessors to get the information and then displaying them
                                print("Passenger Name: ",passenger_info.getPassengerName())
                                print("Ticket Code: ",passenger_info.getTicketNumber())
                                print("Flight Name: ",passenger_info.getFlightName())
                                print("Destination: ",passenger_info.getDestination())
                                print("Departure Time: ",passenger_info.getFlightTime())
                                print("Seat: ",passenger_info.getSeat())
                                print("Gate: ",passenger_info.getFlightGate())


                            else:
                                print("An error occurred")
                               
                                #asking the user if he or she is sure
                            choice=input("\nAre you sure you want to change your flight:(Use \"y\" for yes and \"n\" for no)\n>>>")




                             #if statements to decide if the user wants to continue and change his or her flight or just go back to main menu
                            if choice == "y" or choice == "Y":

                                print()


                                displayFlights()# using this function to display the flights available


                                flightN2=bookFlight(fullname,p_key) # using this function so the user can select his or her flight and passing the passenger name and pass key
                                
                                

                                print()
                                

                                 #if-elif-else statements deciding the flight the passenger chose
                                if flightN2 == flight1:


                                     #creating an instance of the PassengerInfo class in the Flight module
                                    passenger_info=Flight.NewPassengerInfo(fullname,p_ticket_code,flightN2, D143['Destination'],D143['Time'],D143['Gate'],'Standby')
                                    

                                    time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
                                    

                                    #using the get methods / accessors to get the information and then displaying them
                                    print("Passenger Name: ",passenger_info.getPassengerName())
                                    print("Ticket Code: ",passenger_info.getTicketNumber())
                                    print("Flight Name: ",passenger_info.getFlightName())
                                    print("Destination: ",passenger_info.getDestination())
                                    print("Departure Time: ",passenger_info.getFlightTime())
                                    print("Seat: ",passenger_info.getSeat())
                                    print("Gate: ",passenger_info.getFlightGate())

                                    print("\nYou have been added to Flight {} ".format(flightN2))


                                elif flightN2 == flight2:
                                    
                                    time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
                                    

                                     #creating an instance of the PassengerInfo class in the Flight module
                                    passenger_info=Flight.NewPassengerInfo(fullname,p_ticket_code,flightN2, B157['Destination'],B157['Time'],B157['Gate'],'Standby')


                                    #using the get methods / accessors to get the information and then displaying them
                                    print("Passenger Name: ",passenger_info.getPassengerName())
                                    print("Ticket Code: ",passenger_info.getTicketNumber())
                                    print("Flight Name: ",passenger_info.getFlightName())
                                    print("Destination: ",passenger_info.getDestination())
                                    print("Departure Time: ",passenger_info.getFlightTime())
                                    print("Seat: ",passenger_info.getSeat())
                                    print("Gate: ",passenger_info.getFlightGate())

                                    print("\nYou have been added to Flight {} ".format(flightN2))


                                elif flightN2 == flight3:


                                     #creating an instance of the PassengerInfo class in the Flight module
                                    passenger_info=Flight.NewPassengerInfo(fullname,p_ticket_code,flightN2, K260['Destination'],K260['Time'],K260['Gate'],'Standby')
                                    


                                    time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
                                    

                                    #using the get methods / accessors to get the information and then displaying them
                                    print("Passenger Name: ",passenger_info.getPassengerName())
                                    print("Ticket Code: ",passenger_info.getTicketNumber())
                                    print("Flight Name: ",passenger_info.getFlightName())
                                    print("Destination: ",passenger_info.getDestination())
                                    print("Departure Time: ",passenger_info.getFlightTime())
                                    print("Seat: ",passenger_info.getSeat())
                                    print("Gate: ",passenger_info.getFlightGate())

                                    print("\nYou have been added to Flight {} ".format(flightN2))



                                elif flightN2== flight4:



                                     #creating an instance of the PassengerInfo class in the Flight module
                                    passenger_info=Flight.NewPassengerInfo(fullname,p_ticket_code,flightN2,J791['Destination'] ,J791['Time'],J791['Gate'],'Standby')
                                    



                                    #using the get methods / accessors to get the information and then displaying them
                                    time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
                                    print("Passenger Name: ",passenger_info.getPassengerName())
                                    print("Ticket Code: ",passenger_info.getTicketNumber())
                                    print("Flight Name: ",passenger_info.getFlightName())
                                    print("Destination: ",passenger_info.getDestination())
                                    print("Departure Time: ",passenger_info.getFlightTime())
                                    print("Seat: ",passenger_info.getSeat())
                                    print("Gate: ",passenger_info.getFlightGate())

                                    print("\nYou have been added to Flight {} ".format(flightN2))




                                break #using the break function to make the program break out of the loop if one of the option above is chosen




                            else: 
                                   

                               pass #using the pass function so the program pass over this else statement and not call an exception . the pass function is just a place holder 



                    else:
                        print ("You weren't found on this Flight ")


                        break #using the break function to make the program break out of the loop if the else statement is chosen
             

            elif choice == 3:
               

                #using the extend function to add elements of other list to one list.
                allFlight.extend(flightMiami)
                allFlight.extend(flightJamaica)

                
              
                #using the while loop to count each flights
                while numFlights <len(allFlight):

                    if numFlights < len(allFlight):

                        numFlights+=1
                        


                        continue #using the continue to function so the program automatically move back to the top of the while statement instead going to the next statement
                    

                    else:

                        break  #using the break function to make the program break out of the loop if one of the option above is chosen

                    


                time.sleep(0.9)
                print("There are {} number of flights departuring from this airport:".format(numFlights)) #using the format function to add the 
                






           #If the user choice is anything other from 1 and 2 the program will exit         
            else:
               customerCareNumber=slash.join(CustomerCare)# using the join method to put a slash inbetween each group of numbers. It combines two strings into one
               
               print("Incase you need more information you can call {}\n".format(customerCareNumber))

               airlinesInfo=zip(airlines,airlinesNum) #using the zip function to concatenate elements of two or more list.

               airlinesInfo2=list(airlinesInfo)# the zip function puts the elements in a tuple and i use the list function to change it back to a list

               print("Airlines Information:\n")

               print(airlinesInfo2)

               print("\nThank You Have A Great Flight!!!\n")
              
               rep="n" 


    #Exceptions to catch some errors 
    except FileNotFoundError:
        print("The file for the flights are not found or the flight Name wasn't found(e.g FN: B157 )")

        time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think

        main() #using recursion to run the program once more 



    except KeyError:
        print("No key is found in the dictionary")
        time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think

        main() #using recursion to run the program once more



    except IndexError:
        print("No indexes found")

        time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think


        main() #using recursion to run the program once more



    except ImportError:

        print("Importing Failed")


        time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think


        main() #using recursion to run the program once more



    except ValueError:
        print("incorrect issue with the value used")

        time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think


        main() #using recursion to run the program once more


  
    



#function use to display the flights
def displayFlights():
    print("\n")
    print("FN     Time     Destination       Gate")
    print("D143   7:00       Miami            G1")
    print("B157   6:30      Jamaica           F2")
    print("K260   17:30      Miami            G10")
    print("J791   18:00     Jamaica           F5")


def bookFlight(name,key):
    
    time.sleep(0.9)# sleep method from the time module is used here so the program doesn't seem like it is rushing but give the user time to think
    print ("\nSelect a flight number (*FN: J200):")

    flight=input() #getting the user input for the flight they want 
    passkey_info=open(flight+'.txt','a') #opening the flight flie with the pass keys
    passinput=open(flight+'passengers.txt','a') #opening the flight flie with the passengers' names


    #writing the user passkey and user name and adding the user to the flight 
    passkey_info.write("\n"+key)
    passinput.write("\n" +name.upper()+"- Standby\n") # the user will have standby beside their name
    #closing the flies
    passinput.close() 
    passkey_info.close()

    return flight #returning the  that the user chose

#Header with information on the program
def header():
    print("\t\t\t\tWelcome to A1FA\n")
    print("\t\t\t\t\t\t\tBy Swerf Tech\n")

    print("Adelva 1.0 Flight Agent is a program that will help you to get you back on flight. We at Swerf Tech knows")
    print("that everything don't always go perfect so we want to help you the passenger to get to your final destination in time \nwith not much time lost.\n")
    print(">>>Let A1FA help you because that is what she was built for !!!<<<\n")
    print("___________________________________________________________________________________")





main()