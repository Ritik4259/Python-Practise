""" class bio:
    name="Ritik"
    age=18
    def b(self):
        print("my name is",self.name)
        print("my age is",self.age)
a=bio()
print(a.name)
print(a.age)
bio().b() """

""" class xyz:
    def __init__(self,d,e):
        self.name=d
        self.age=e
    def out(self):
        print("my name is",self.name,"my age is",self.age)
s1=input()
s2=int(input())
s=xyz(s1,s2)
s.out() """

""" x=input()
b=input()
if len(x)!=len(b):
        print('False')
elif len(x)==len(b):
        for i in x:
                if i in b:
                        if x.count(i)!=b.count(i):
                                a=0
                                break
                        else:
                                a=1
                else:
                        a=0
                        break
if a==1:
        print('True')
else:
        print('False')

 """
""" import string
v= 'AEIOUY'
tag=input()
tag=list(tag)
for i in range(0,len(tag)-1):
        n=tag[i]
        m=tag[i+1]
        if n.isdigit() and m.isdigit():
                if (int(n) + int(m))%2==0:
                        x='valid'
                else:
                        x="invalid"
                        break
        if n.isalpha():
                if n not in v:
                        x='valid'
                else:
                        x="invalid"
                        break
print(x) """



""" n=int(input())
a=input().split()
ans=''
for i in a:
    ans+=i[-1]
if int(ans)%10==0:
    print("Yes")
else:
    print("No") """


""" grid=int(input())
vil=input()
ans=''
for i in vil:
    if i!='.':
        ans+=i
    elif i=='.':
        ans+='B'
print("Yes")
print(ans) """

#### WRITE A PYTHON PROGARM TO CREATE A CALCULATOR CLASS. INCLUDE METHODS FOR ADD, SUB , MUL , DIV'

""" class calculator:
    def num(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a + self.b)
    def sub(self):
        print(self.a - self.b)
    def mul(self):
        print(self.a * self.b)
    def div(self):
        if self.b!=0:
            print(self.a / self.b)
        else:
            print("cannot divide by 0")

result=calculator()
a=int(input("num1: "))
b=int(input("num2: "))
result.num(a,b)
result.add()
result.sub()
result.mul()
result.div() """


#### Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not.

""" class Student:
    def __init__(self) -> None:
        pass
class Marks:
    def __init__(self) -> None:
        pass
s=Student()
m=Marks()
print(type(s))
print(type(m))
print(type(Student))
print(type(StudentM)) """

""" class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

a=Vehicle('School Volvo',180,12)
b=bus('School Volvo',180,12)
print(b.name)
print(b.max_speed)
print(b.mileage) """

""" class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

a=bus('bus',60,30)
print(a.seating_capacity()) """

class Vehicle:

    def __init__(self, name, max_speed, mileage,color):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass

