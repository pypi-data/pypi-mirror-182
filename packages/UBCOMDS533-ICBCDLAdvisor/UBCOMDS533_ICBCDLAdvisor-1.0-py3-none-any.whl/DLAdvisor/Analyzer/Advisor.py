from DLAdvisor.ProfileBuilder import Collector
from DLAdvisor.Analyzer import Resource

class InvalidStageError(Exception):
    pass

def advice(stage) :
    if stage > 5 :
        raise InvalidStageError("Your input stage : ",stage," is invalid!")
    prepRes = populatePrepResources(stage)
    OLRes = populateOLResources(stage)
    if (stage == 1) :
        objective = "pass the ICBC Knowledge Test"
    elif (stage == 2) :
        objective = "pass the ICBC Road Test 7"
    elif (stage == 3) :
        objective = "pass the ICBC Road Test 5"
    else :
        objective = "apply exchanging for your license from Reciprocal countries"
        
    print(f'Your next step should be : {objective}' )
    print(f'The following resources are suggested to achieve your above goals.\n##########') 
    prepRes.display()
    print("")
    OLRes.display()
    print("########")
    
def populatePrepResources(stage):
    
    if stage > 5 :
        raise InvalidStageError("Your input stage : ",stage," is invalid!")
    
    res1 = [
        ['Knowledge Test Info','https://www.icbc.com/driver-licensing/new-drivers/Pages/Get-your-L.aspx'],
        ['Practice Knowledge Test', 'https://www.icbc.com/driver-licensing/new-drivers/Pages/practice-knowledge-test.aspx'],
        ['Download ICBC Apps for iOS','https://apps.apple.com/ca/app/icbc-practice-knowledge-test/id438491857'],
        ['Download ICBC Apps for Android','https://play.google.com/store/apps/details?id=com.icbc.knowledge'],
        ['Learn to Drive Smart', 'https://www.icbc.com/driver-licensing/driving-guides/Pages/Learn-to-Drive-Smart.aspx']
        ]
    
    res2 = [
        ['RoadTest 7 Info','https://www.icbc.com/driver-licensing/new-drivers/Pages/Get-your-N.aspx'],
        ['Learn to Drive Smart', 'https://www.icbc.com/driver-licensing/driving-guides/Pages/Learn-to-Drive-Smart.aspx'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]
    
    res3 = [
        ['RoadTest 5 Info','https://www.icbc.com/driver-licensing/new-drivers/Pages/Get-your-full-licence.aspx'],
        ['Learn to Drive Smart', 'https://www.icbc.com/driver-licensing/driving-guides/Pages/Learn-to-Drive-Smart.aspx'],
        ['Kelowna Best Driving School','https://threebestrated.ca/driving-schools-in-kelowna-bc'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]
    
    res4 = [
        ['Reciprocal License Info','https://www.icbc.com/driver-licensing/moving-bc/Pages/Moving-from-another-country.aspx'],
        ['BC Driving Tips','https://www.youtube.com/watch?v=UohMY0CT_V8']
        ]

    if (stage == 1) :
        res = res1
    elif (stage == 2) :
        res = res2
    elif (stage == 3) :
        res = res3
    else :
        res = res4
        
    return Resource.PrepResource(stage,res)


## Populate Online Resources (e.g. icbc application links to apply knowledge test/road test/reciprocal license exchange, knowledge test registration links, driving school registration link, etc) 

def populateOLResources(stage):

    res1 = [
        ['Book a ICBC Knowledge Test','https://onlinebusiness.icbc.com/qmaticwebbooking/#/'],
        ['ICBC Office Locator','https://www.icbc.com/locators/Pages/default.aspx?type=1&subtype=0']
        ]
    
    res2 = [
        ['Book a Road Test 7','https://onlinebusiness.icbc.com/webdeas-ui/home'],
        ['ICBC Office Locator','https://www.icbc.com/locators/Pages/default.aspx?type=1&subtype=0']
        ]
    
    res3 = [
        ['Book a Road Test 5','https://onlinebusiness.icbc.com/webdeas-ui/home'],
        ['ICBC Office Locator','https://www.icbc.com/locators/Pages/default.aspx?type=1&subtype=0']
    ]
    
    res4 = [
        ['Book a ICBC License Exchange Appointment','https://onlinebusiness.icbc.com/qmaticwebbooking/#/'],
        ['ICBC Office Locator','https://www.icbc.com/locators/Pages/default.aspx?type=1&subtype=0']
        ]

    if (stage == 1) :
        res = res1
    elif (stage == 2) :
        res = res2
    elif (stage == 3) :
        res = res3
    else :
        res = res4
        
    return Resource.OLResource(stage,res)
