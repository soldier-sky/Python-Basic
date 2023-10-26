# This program will handle shipping container details
# This will allow us to understand how to use instance variable and class variable

class ShippingContainer:

    next_serial=1234 # class attribute or class variable
    ''' 
    @staticmethod
    def _generate_serial():    # We removed self parameter to function def as it was redundent in this case
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result
    '''
    @classmethod
    def _generate_serial(cls):     #cls is equivalent of self
        result=cls.next_serial
        cls.next_serial+=1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        ''' create_empty() is named constructor which create empty 
            ShippingContainer ie. content would be None
        '''
        return cls(owner_code,content=[])

    @classmethod
    def create_with_items(cls,owner_code, items):
        ''' Creates shipping container with list of items 
        '''
        return cls(owner_code, content=list(items))


    def __init__(self, owner_code, content):
        self.owner_code=owner_code      # Instance attribute example
        self.content=content
        self.serial= ShippingContainer._generate_serial()

    def print_content(self):
       print("Content of shipping container {0} is {1}".format(self.owner_code, self.content))
       


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_TEMP_CELCIUS=4

    def __init__(self, owner_code, items, temp):
        super().__init__(owner_code, items)
        self.temp=temp

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self,value):
        if value > self.MAX_TEMP_CELCIUS :
            raise ValueError("temperature too hot")
        self._temp=value


s1=ShippingContainer("EVG",'textile')
s1.print_content()
# print("Container ID is ",s1.get_containerID())

s2=ShippingContainer("TMS","vegetable")
s1.print_content()
# print("container ID is",s1.get_containerID())


rc=RefrigeratedShippingContainer('SKY', 'fishe', 4)
print(rc.temp)

#rc2=RefrigeratedShippingContainer('PSY', 'Potato', 12)

rc.MAX_TEMP_CELCIUS=12;
print(rc.MAX_TEMP_CELCIUS)
