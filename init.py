class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        

    def configure(self):
        print("Configuration is: ", self.cpu, self.ram)

comp1 = computer('15',16)


# __init__ , not neede to be called by obj, it gets executed by default.


