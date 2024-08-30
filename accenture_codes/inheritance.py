class A:
    def function1(self):
        print("This is function1")
    def function2(self):
        print("This is function2")
class B:
    def function3(self):
        print("This is function3")
    def function4(self):
        print("This is function4")
class C(A,B):
    def function5(self):
        print("This is function5")
    def function6(self):
        print("This is function6")
c = C()


class Animal:
    def make_sound(self):
        print("animal makes a sound")
class Dog(Animal):
    def make_sound(self):
        print("dog barks")
class Cat(Animal):
    def make_sound(self):
        print("cat meows")
a=Animal()

class Library:
    def __init__(self,books,give,take):
        self.books = ["Eng","math","sci"]
        self.give = give
        self.take = take

    def add(self):
        give = input("Enter a book name to add:")
        self.books.append(give)
        print("Your added book is: ",give)
        print("Books are present in library",self.books)
    def tak(self):
        take = input("Enter a book name you want: ")
        if(take in self.books):
            self.books.remove(take)

        else:
            print("No book in library")

        print("books are prasent in library: ",self.books)
    def back(self):
        choice = input("You want to givit back:")

        if(choice=="yes"):
            restore = input("Enter a book name: ")
            self.books.append(restore)
            print("Your return book name is: ",restore)
            print("Books are present in library:",self.books)

l = Library("books","give","take")
l.add()
l.tak()
l.back()
