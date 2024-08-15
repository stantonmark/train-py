'''a class is a bluepoint/template for creating objects 
classes enforce'''

class Client:
    def __init__(self): # refers to current objec 
        self.name='Client'
        self.email='no email supplied'
        self.dependents = []
    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, dependents: {self.dependents}"
        
client1 = Client()

print(client1)

        
print(client1.name)




class ClientWithParams:
    def __init__(self, name, email, *dependents): 
        self.name = name
        self.email = email
        self.dependents = dependents        
    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, dependents: {self.dependents}"
    
#clientWithParams = ClientWithParams()
clientWithParams = ClientWithParams("Alan", "alan@me.com", "sophie", "susie")


