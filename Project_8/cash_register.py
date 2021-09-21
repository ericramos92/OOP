import retailitems_class
class register():
    def __init__(self):
        self.register_list = []
    def getlistitems(self):
        return self.register_list
    def purchase_items(self, object_added):
        self.register_list.append(object_added)
    def get_total(self,object_added):
        self.total = 0
        self.total += object_added.getprices()
        return self.total
    def clear_items(self):
        self.register_list.clear()


def main():
    #create object'shirt','20','24.95
    obj = retailitems_class.retail('shirt','20',10)
    obj1 = retailitems_class.retail('Jacket','10',100)
    obj2 = retailitems_class.retail('Jeans','10',24.95)
    register_object =register()
    register_object.purchase_items(obj)
    register_object.purchase_items(obj1)
    register_object.purchase_items(obj2)
    array = register_object.getlistitems()
    for i in array:
        print("")
        print(i)
    print("----------------")
    t=register_object.get_total(obj)
    r=register_object.get_total(obj1)
    l=register_object.get_total(obj2)
    print("Total:"+ str(t+r+l))





main()
