class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def c(self):
        print(self.cpu,self.ram)         

comp=computer(2,3)
comp.c()
