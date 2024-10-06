# Name: FinalProject
# Author: Mandeep Kaur

# Description: The  program to to get customer information and the details of the call he/she wants from the technician 
#               working in Rogers Company. It prompts the customer which type of call it wants and then present the details 
#               to the it which was selecetd.

# Storing some values in the variales
selfInstallFee = "$60"
profInstallFee = "$100"
serviceFee = "$30"
# Empty ddictionary for storing call information
callChoice = {}

#
# Function: introText()
# Description: will output the main text that is the Welcome message to the customer
# Parameters: none
# Return Value: none
#
def introText():
    print("Welcome to Rogers!!\nHope you have a great experience with our service!!\n")

#
# Function: takeUserInfo()
# Description: will prompt user some information and then store in the list i.e., is userInfo
# Parameters: none
# Return Value: none
#
def takeUserInfo():
    # Empty list to store customer details be using append() method
    userInfo = []
    firstName = input("Enter your first name: ")
    userInfo.append(firstName)
    lastName = input("Enter your last name: ")  
    userInfo.append(lastName) 
    streetName = input("Enter your street name: ")  
    userInfo.append(streetName)
    unit = input("Enter the unit: ")
    userInfo.append(unit)
    city = input("Enter your city name: ")
    userInfo.append(city)
    province = input("Enter your province: ")
    userInfo.append(province)
    postalCode = input("Enter your postal code: ")
    userInfo.append(postalCode)
    phoneNumber = input("Enter your phone number: ")
    userInfo.append(phoneNumber)

    return userInfo

#
# Function: custCallChoice()
# Description: will prompt user to pick call and then confirm it whether the choice is correct or not
# Parameters: 
#             nestDict: the nesdted dictionary containing information about 3 types of calls and their corressponding time taken
# Return Value: none
#
def custCallChoice(nestDict):
    while True:
        # Exception Handling to handle errors
        try:
            print("\nPlease select the call [1-3] you prefer from the options provided above.")
            callName = int(input())

            if (callName == 1):
                callChoice["Name"] = nestDict[callName]["Call"]
                print("If you own your equipment then ther's no replacement")
                callChoice["Time"] = nestDict[callName]["Time"]
                callChoice["Cost"] = serviceFee

            elif (callName == 2):
                callChoice["Name"] = nestDict[callName]["Call"]
                callChoice["Time"] = nestDict[callName]["Time"]
                while True:
                    print("Please select '1' for Self-Install and '2' for Professional-Install")
                    callChoice["installType"] = int(input())
                    if (callChoice["installType"] == 1):
                        callChoice["Install"] = "Self-Install"
                        callChoice["Cost"] = selfInstallFee
                        break
                    elif (callChoice["installType"] == 2):
                        callChoice["Install"] = "Professional-Install"
                        callChoice["Cost"] = profInstallFee
                        break
                    else:
                        print("Enter the correct option.") 

            elif (callName == 3):
                print("Customer is needed on-site for this call.")
                print("If the fault is outside then customer is not needed at that point.")
                print("There are no charges for the miscellaneous call")
                callChoice["Name"] = nestDict[callName]["Call"]
                callChoice["Time"] = nestDict[callName]["Time"]
                callChoice["Cost"] = "No Charges"

            else:
                print("Please choose the correct call number.")
                continue
        #Used except to handle if there is any exception or error      
        except KeyError:
            print("Please choose number among [1-3] only.")
        except Exception:
            print("Please enter number only.")
            continue

        #Loop to repeat until customer confirms the call type   
        while True:
            callConfirm = input("\nEnter 'y' for Yes or 'n' for No to confirm the call selected: ").lower()    
            if (callConfirm == "y" or callConfirm == "n" ):
                break
            else:
                print("Please enter y or n only.")    
        if (callConfirm == "y"):
            break   

#
# Function: callInfoPrint()
# Description: will print out customer details and the call information
# Parameters:  none       
# Return Value: none
#
def callInfoPrint():
    printInfo = ""
    printInfo += "{0:<30s}{1}{2}{3}".format("Name: ", userInfo[0], " " , userInfo[1])
    printInfo += "\n{0:<30s}{1}{2}{3}".format("Street Address: ", userInfo[2], " ", userInfo[3])
    printInfo += "\n{0:<30s}{1}{2}{3}{4}{5}".format("City, Province, Postal Code: ", userInfo[4], ", ", userInfo[5], ", ", userInfo[6])
    printInfo += "\n{0:<30s}{1}".format("Phone Number: ", userInfo[7])
    printInfo += "\n"
    printInfo += "\nThe booked call details are given below:"
    printInfo += "\n{0:12s}{1:<18s}".format("Call Name: ", callChoice["Name"])
    printInfo += "\n{0:12s}{1:<18s}".format("Call Time: ", callChoice["Time"])
    printInfo += "\n{0:12s}{1:<19s}".format("Call Fee: ", callChoice["Cost"])

    return printInfo

    
# Main part of the program
# Calling the function introText()
introText()

# Calling the function which prompt user information and then store in the list
userInfo = takeUserInfo()

# Nested Dictionary conatining call names and their coressponding timmings
callNestDict = {
    1 : {"Call" : "Service" , "Time" : "50 Min"},
    2 : {"Call" : "Install" , "Time" : "120 Min"},
    3 : {"Call" : "Miscellanous" , "Time" : "45 Min"}
}

print("\nHave a look at the below Calls and the average time they can take!!")
print("{0:20s}\t{1:>21s}".format("Call Names", "Call Duration"))
# Looping through all the calls stored in the above nested dictionay and then print them
for x in callNestDict:
    print("{0}{1}{2:20s}\t\t{3:>1.2s}".format(x, ")" ,callNestDict[x]["Call"] ,callNestDict[x]["Time"]))

# Calling the function which make customer to choose the call and then confirm it's choice
custCallChoice(callNestDict)

print("\n")
#Calling function callInfoPrint and then store in a variable
callInfo = callInfoPrint()
print(callInfo)

#Used with open to print the call Details in a text file
with open(fileName, "w") as theLogFile:
    theLogFile.write(callInfo)


