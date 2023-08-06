from .UserProfile import UserProfile
import datetime
from datetime import date

class AgeTooLargeError(Exception) :
    pass

# This fuction will greet the applicant based onthe time of the day
def greeting():
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12 :
        print('Good morning!')
    elif 12 <= currentTime.hour < 18 :
         print('Good afternoon!')
    else:
         print('Good evening!')

#Calculate no. of years from current date based on a date input (like, age, driving license yrs, etc.)
def calculateAge(dateEntry):
    days_in_year = 365.2425  
    age = int((date.today() - dateEntry).days / days_in_year)
    if age > 150 :
        raise AgeTooLargeError("Your input age : ",age,"!, please double check!")
    return age
       
# This function takes input from user to create profile and check eligibility
# This returns True if eligible for license
def passBasicEligibility():
    global name
    global haveICBCLicense
    global wantToExchange
    global reciprocal
    global stage
    global knowledgeTest
    
    try:
        wantToExchange="No"
        reciprocal="No"
        bcres = input("Are you a BC resident?[Y/N]")#BC resident
        if (bcres == "N") :
            print("Only BC residents are eligible to get a BC Driving License")
            return False
        name = input("What is your full name?")# Full Name
        dob = input("Enter your date of birth?[DD/MM/YYYY]") #Date of birth
        birthday_list = dob.split("/")
        day=int(birthday_list[0])
        month=int(birthday_list[1])
        year=int(birthday_list[2])
        age = calculateAge(date(year, month, day)) #applicant age

        if (age < 16) :
            print("Your age is",age,"which is below 16 yrs, so you are not eligible for BC Driving license")
            return False
    
        #defines the stages
        #1=No ICBC driving license (Opt for Learner's License)
        #2=Learner's to Novice (Opt for Novice License)
        #3=Novice to Full License (Opt for Full License)
        #4=Exchanage license (Opt for Exchange)
    
        haveICBCLicense = int(input("Which ICBC driver licence you have? [Enter 0 for None, 1 for Learners, 2 for Novice]"))
        if haveICBCLicense == 0:
            wantToExchange =input("Do you want to exchange your other licence? [Yes/No]")
            if wantToExchange == "Yes":
                reciprocal = input("Is your license from a reciprocal country? [Yes/No]")
                if reciprocal == "Yes":
                    stage = 4
                else:
                    knowledgeTest =input("Did you pass ICBC Knowledge Test? [Yes/No]")
                    if knowledgeTest == "Yes":
                        stage = 3
                    else:
                        stage = 1
            else:
                #reciprocal = input("Is your license from a reciprocal country? [Yes/No]")
                stage = 1
        elif haveICBCLicense == 1:
            stage = 2
        else:
            stage = 3
    
        #country = input("Where are you from? Canada/Your Country Name/Others")# Full Name       
        #haveDriveLic = input("Do you have a driving license from your country? [Yes/No]")# Have exiting license?
        #if haveDriveLic == "Yes":
        #    drivingLicDate=input("Driving license date [DD/MM/YYYY]:")# country type
        #    driveDate = drivingLicDate.split("/")
        #    day=int(driveDate[0])
        #    month=int(driveDate[1])
        #    year=int(driveDate[2])
        #    drivingYears = calculateAge(date(year, month, day)) #driving years
        #else:
        #    drivingYears = 0 #driving years
        return True
    except Exception as ex:
        print("An exception occurred : ",ex)

# After taking input from user in passBasicEligibility() it then constructs the UserProfile object
# call class modeule in the same pkg
# Return UserProfile object
def gatherProfile():
    try :
        profile = UserProfile(name,haveICBCLicense,wantToExchange,reciprocal,stage)
        #print(profile)
        #UserProfile(self,name,current_icbc_lic,is_dl_exchange,is_recip_country,stage)
        return profile
    except Exception as ex:
        print("An exception occured in gatherProfile: ",ex)
        return
