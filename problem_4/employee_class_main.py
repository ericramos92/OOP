import employee_class

#creating instances of the class
obj = employee_class.employee('name', 'id', 'department', 'job')
obj1 = employee_class.employee('Mark Jones', 39119, 'IT', 'Programmer')
obj2 = employee_class.employee('Joy Rogers', 81774, 'Manfacturing', 'Engineer')

obj.setname('Susan Mayers')
obj.setid_number('47899')
obj.setdepartment('Accounting')
obj.setjob('Vice president')


print("Name             ID        Department        Job Tittle")
print('-------------------------------------------------------')
print(f"{obj.getname()}\t{obj.getid_number()}\t\t{obj.getdepartment()}\t\t{obj.getjob()}")
print(f"{obj1.getname()}\t{obj1.getid_number()}\t\t{obj1.getdepartment()}\t\t{obj1.getjob()}")
print(f"{obj2.getname()}\t{obj2.getid_number()}\t\t{obj2.getdepartment()}\t{obj2.getjob()}")
