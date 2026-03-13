#sample program on how to create a cl;ass,define attributes in it, and objects

# class Bank:
#     bank_name='SBI'
#     bank_location='Mysore'
# c1=Bank()
# c2=Bank()
# print(Bank.bank_name,Bank.bank_location)
# print(c1.bank_name,c1.bank_location)
# print(c2.bank_name,c2.bank_location)
# Bank.bank_location='Bangalore'
# print(Bank.bank_name,Bank.bank_location)    #modification with respect to class
# c1.bank_name='ICICI' #modification with respect to object
# print(c1.bank_name,c1.bank_location)
# print(Bank.bank_name,Bank.bank_location)





#WAP to create one class as school and pass 2 variables as schl_name=DPS and schl_city=Hyd. then modify the school name as KPS and city as Delhi

#1.modification of class

# class School:
#     schl_name='DPS'
#     schl_city='Hyd'
# print(School.schl_name,School.schl_city)
# School.schl_name='KPS'
# School.Schl_city='Delhi'
# print(School.schl_name,School.schl_city)


#2.modification of object

# class School:
#     schl_name='DPS'
#     schl_city='Hyd'
# s1=School()
# s2=School()
# print(School.schl_name,School.schl_city)
# s1.schl_name="KPS"
# s1.schl_city='Delhi'
# print(s1.schl_name,s1.schl_city)





#create class company , 4 class members, create 2 objects consists of 5 object members
# class Company:   #class name
#     name="Airtel" #class member
#     cloc='Pune'   #class member
#     ceo='John'    #class member
#     website='www.airtel.com'   #class member

# emp1=Company() #object 1
# emp2=Company() #object 2

# def to_initialize(obj,ename,eloc,contact,stfid,bldgrp):#function to initialize
#     obj.ename=ename  #object member
#     obj.eloc=eloc   #object member
#     obj.contact=contact   #object member
#     obj.stfid=stfid     #object member
#     obj.bldgrp=bldgrp  #object member

# print(Company.name,Company.cloc,Company.ceo,Company.website)

# to_initialize(emp1,'Neha','Hyd',1234567890,'EMP114','O+')  #calling the function and entering data in emp1 
# print(emp1.ename,emp1.eloc,emp1.contact,emp1.stfid,emp1.bldgrp)

# to_initialize(emp2,'Krish',"Pune",'0987654321','EMP115','O+')  #calling the function again and entering data in emp2
# print(emp2.ename,emp2.eloc,emp2.contact,emp2.stfid,emp2.bldgrp)






#using self and init

# class Company:   #class name
#     name="Airtel" #class member
#     cloc='Pune'   #class member
#     ceo='John'    #class member
#     website='www.airtel.com'   #class member
#     def init_employee(self,ename,eloc,contact,stfid,bldgrp):#function to initialize
#         self.ename=ename  #object member
#         self.eloc=eloc   #object member
#         self.contact=contact   #object member
#         self.stfid=stfid     #object member
#         self.bldgrp=bldgrp  #object member

# print(Company.name,Company.cloc,Company.ceo,Company.website)
# emp1=Company()
# emp1.init_employee('Neha','Hyd',1234567890,'EMP114','O+')  #calling the function and entering data in emp1 
# print(emp1.ename,emp1.eloc,emp1.contact,emp1.stfid,emp1.bldgrp)
# emp2=Company()
# emp2.init_employee('Krish',"Pune",'0987654321','EMP115','O+')  #calling the function again and entering data in emp2
# print(emp2.ename,emp2.eloc,emp2.contact,emp2.stfid,emp2.bldgrp)
    


#constructor "__init__()"

# class Company:
#     cname='Docomo'
#     cloc="Don't exist"
#     ceo='Pug'
#     website='www.docomo.com'
#     def __init__(self,ename,eloc,contact,bldgrp,email):
#         self.ename=ename
#         self.eloc=eloc
#         self.contact=contact
#         self.bldgrp=bldgrp
#         self.email=email
# emp1=Company('John','Pune',9870654321,'O+','john123@gmail.com')
# emp2=Company('Sam','Delhi',2345167939,'A+','sam980@gmail.com')
# print(emp1.ename,emp1.eloc,emp1.contact,emp1.bldgrp,emp1.email)
# print(emp2.ename,emp2.eloc,emp2.contact,emp2.bldgrp,emp2.email)





#WAP for creating class as bank,pass 2 class members:bank_name,bank_branch,use constructor and create 3 object members:acc_no,name,balance,create 2 objects:acc1 and acc2 and then access the members directly

# class Bank:
#     bank_name="SBI"
#     bank_branch="Hyd"
#     def __init__(self,acc_no,name,balance):
#         self.acc_no=acc_no
#         self.name=name
#         self.balance=balance
# acc1=Bank(1000,'xyz','2,00,000')
# acc2=Bank(1019,"abc","1,23,000")
# print(Bank.bank_name,Bank.bank_branch)
# print(acc1.acc_no,acc1.name,acc1.balance)  
# print(acc2.acc_no,acc2.name,acc2.balance)



