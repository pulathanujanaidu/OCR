class Animal():
    def sound(self):
        print("animal makes a sound")

class Animal2():
    def sound(self):
        print("dog makes a sound")

class Animal3():
    def sound(self):
        print("cat makes a sound")

def make_sound(Animal):
    Animal.sound()

my_animal =Animal()
make_sound(my_animal)
my_animal=Animal2()
make_sound(my_animal)
my_animal=Animal3()
make_sound(my_animal)


def swaplist(list):
    a=list[-1],list[0]
    list[0],list[-1]=a
    return list
my_list=[1,2,3,4,5]
print(swaplist(my_list))

