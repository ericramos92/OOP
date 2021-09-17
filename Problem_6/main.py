import patient_charges
import procedure


name = input("First Name:")
middle_name = input('Middle Name:')
last_name = input('Last Name:')
address = input("Address:")
city = input("City:")
state = input("State:")
zipcode = input("Zipcode")
phone = input('Phone:')
emergency_name = input("Emergency name:")
emergency_phone = input("Emergency phone:")
#creating an object for patient class
obj = patient_charges.patients('name', 'middle_name', "last_name","address",'city',"state", "zipcode", "phone","emergency_name","emergency_phone")
obj.setname(name)
obj.setmiddle(middle_name)
obj.setlast(last_name)
obj.setaddress(address)
obj.setcity(city)
obj.setstate(state)
obj.setzipcode(zipcode)
obj.setphone(phone)
obj.setemergency_name(emergency_name)
obj.setemergency_phone(emergency_phone)

print('Patient Information')
print("___________________________")
print(f"Name:{obj.getname()} {obj.getmiddle()} {obj.getlast()}")
print(f"Addres:{obj.getaddress()} City:{obj.getcity()} State:{obj.getstate()} Zipcode:{obj.getzipcode()}")
print(f"Phone:{obj.getphone()}")
print(f"Emergency Name:{obj.getemergency_name()} Emergency Phone:{obj.getemergency_phone()}")

#getting procedure Information
obj1 = procedure.procedures("Physical Exam","9/21/2021","Dr.Irvine","250.0")
obj2 = procedure.procedures("X- Ray","9/21/2021","Dr.Jamison","500.0")
obj3 = procedure.procedures("Blodd Test","9/21/2021","Dr.Smith","200.0")

print("\n\nPlease pick one")
print("-----------------------")
print("Procedure #1:\t\t\t\tProcedure #2\t\t\tProcedure #3")
print(f"Procedure Name:{obj1.getname()}\t\tProcedure Name:{obj2.getname()}\t\tProcedure Name:{obj3.getname()}")
print(f"Date:{obj1.getdate()}\t\t\t\tDate:{obj2.getdate()}\t\t\tDate:{obj3.getdate()}")
print(f"Charge:{obj1.getcharges()}\t\t\t\tCharge:{obj2.getcharges()}\t\t\tCharge:{obj3.getcharges()}")
