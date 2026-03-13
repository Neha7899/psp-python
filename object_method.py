#methods

#1.object method


#example

class Bank:
    bank_name="ICICI"   #class members
    branch="Banglore"
    website="www.icici.com"
    helpline=1234567890
    def __init__(self,name,phno,email,address):         #constructor
        self.name=name
        self.phno=phno
        self.email=email
        self.address=address
    def change_name(self,new):   #object method   #modification of object member 
            self.name=new
    def change_email(self,email): #object method
          self.email=email
    def display(self):   #object method     #accessing the object members
            print(self.name,self.phno,self.email,self.address)
ac1=Bank("A",9087654321,"A@gmail.com","Banglore")
ac2=Bank("B",9067453291,"B@gmail.com","Mumbai")
ac3=Bank("C",9234566581,"C@gmail.com","Delhi")
print(Bank.bank_name,Bank.branch,Bank.website,Bank.helpline)
Bank.display(ac3)
Bank.change_name(ac3,'Python')
Bank.display(ac3)
Bank.change_email(ac3,"cat@gmail.com")
Bank.display(ac3)
