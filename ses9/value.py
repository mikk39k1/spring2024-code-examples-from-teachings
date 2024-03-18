class Value:

    def __init__(self, data):
        self.data = data


    def __repr__(self):
        return f"{self.__dict__}"

    def __add__(self, other):
        return self.data + other.data
        

    

a = Value(1)
b = Value(2)


