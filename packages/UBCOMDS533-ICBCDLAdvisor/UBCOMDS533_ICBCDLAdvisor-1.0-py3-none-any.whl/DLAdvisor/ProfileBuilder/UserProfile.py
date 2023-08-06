class UserProfile:
    
    def __init__(self,name,current_icbc_lic,is_dl_exchange,is_recip_country,stage):
        self.name = name
        # 0 : None; 1 : Learner's; 2 : Novice
        self.current_icbc_lic = current_icbc_lic
        self.is_dl_exchange = is_dl_exchange
        self.is_recip_country = is_recip_country
        self.stage = stage
      
    def __str__(self):
        
        if (self.current_icbc_lic == 0) :
            current_icbc_lic_str = "None"
        elif (self.current_icbc_lic == 1) :
            current_icbc_lic_str = "Learner's License"
        else :
            current_icbc_lic_str = "Novice's License"
        
        # TODO : other attributes to be added ....
        
        #is_dl_exchange_val = "Yes" if self.is_dl_exchange else "No"
        #if (not self.is_dl_exchange) :
        #    is_recip_country_val = 'N/A'
        #elif (self.is_recip_country) :
        #    is_recip_country_val = 'Yes'
        #else :
        #    is_recip_country_val = 'No'
        
        return f'User Details \nName : {self.name}\nCurrent ICBC License : {current_icbc_lic_str}\nWant to exchange : {self.is_dl_exchange}\nForeign License from Reciprocal Country: {self.is_recip_country}'
    
    
    def formatName(self) :
        self.name = self.name.capitalize()
        
        
