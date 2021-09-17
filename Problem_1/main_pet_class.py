import pet_class
name = input("Please enter name:")
animal_type = input("PLease enter amimal type:")
age = int(input("PLease enter age:"))

# creating object
animal =pet_class.pets(name,animal_type,age)
print(f"name:{animal.getname()} animal type:{animal.getanimaltype()} age:{animal.getage()}")
