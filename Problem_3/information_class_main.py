import information_class
#instances of classes
obj1 = information_class.informations('eric','1778 Oakland road apt22 ',29,4087079495)
obj2= information_class.informations('eric','1778 Oakland road apt22 ',29,4087079495)
obj3= information_class.informations('eric','1778 Oakland road apt22 ',29,4087079495)

print(f"name:{obj1.getname()} , address:{obj1.getaddress()}, age:{obj1.getage()}, phone:{obj1.getphone_number()}")
print(f"name:{obj2.getname()} , address:{obj2.getaddress()}, age:{obj2.getage()}, phone:{obj2.getphone_number()}")
print(f"name:{obj3.getname()} , address:{obj3.getaddress()}, age:{obj3.getage()}, phone:{obj3.getphone_number()}")
