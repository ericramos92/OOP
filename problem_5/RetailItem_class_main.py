import RetailItem_class

#creating instancees
obj = RetailItem_class.retailitems('description','unit','price')
obj1 = RetailItem_class.retailitems('Designer Jeans',40,34.95)
obj2 = RetailItem_class.retailitems('shirt','20','24.95')


obj.setdescription('Jacket')
obj.setunits('12')
obj.setprices('34.95')

print("Description\t\tUnits\t\tPrice")
print("------------------------------------------------")
print(f'Item#1{obj.getdescription()}\t\t{obj.getunits()}\t\t{obj.getprices()}')
print(f'Item#2{obj1.getdescription()}\t{obj1.getunits()}\t\t{obj1.getprices()}')
print(f'Item#3{obj2.getdescription()}\t\t{obj2.getunits()}\t\t{obj2.getprices()}')
