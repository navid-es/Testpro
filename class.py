class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



class partyanimal:
  x = 0

  def party(self):
    self.x += 1
    print ('so far',self.x)
  
an = partyanimal()

# an.party()
# an.party()
# an.party()
partyanimal.party(an)


# Instantiate :
class Sample:
  pass

sample_object = Sample()  # Instantiation
type(sample_object)



class Car:
    def drive(self):
        print('i drive a car')

a = Car()
a.drive()