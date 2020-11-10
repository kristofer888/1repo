class Computer:
    
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('Config is ', self.cpu, self.ram)

com1 = Computer('i5',16)
com2 = Computer('Kris 3',8)

com1.config()
com2.config()

print(com1.cpu, com1.ram)
print(com2.cpu, com2.ram)

class Show():
    def __init__(self, x):
        self.y = x
    def __call__(self, z):
        print('hello' + self.y)
f = Show('world')
f('1')




