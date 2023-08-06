class EmptyResourceError(Exception):
    pass


class Resource:

    def __init__(self,stage,resources):
        self.stage = stage
        self.resources = resources
        
    def display(self):
        try :
            if len(self.resources) == 0 :
                raise EmptyResourceError("Empty Resources!")
            
            print("Resouces List : ")
            for r in self.resources :
                print('- ' + r[0] + ' [' +
                    self.checkResourceType(r[1]) +
                    '] : ' + r[1])
        except Exception as ex :
            print("Exception occurred :",ex)
            

    def checkResourceType(self,resourceslink) :
        if ("youtube.com" in resourceslink) :
            return "YOUTUBE"
        elif ("icbc.com" in resourceslink) :
            return "ICBC Official"
        elif (".pdf" in resourceslink) :
            return "PDF"
        else :
            return "MISC"

#################

class PrepResource(Resource) :
    
    def __init__(self,stage,resources):
        Resource.__init__(self,stage,resources)
        self.category = "P"
        
    def display(self):
        print("Resource Category : Preparatory Resources")
        Resource.display(self)

        
##################

class OLResource(Resource) :
    
    def __init__(self,stage,resources):
        Resource.__init__(self,stage,resources)
        self.category = "O"
        
    def display(self):
        print("Resource Category : Online Services Resources")
        Resource.display(self)
    