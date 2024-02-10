#String slicing and operation on string in python

var="Sachin Suthar"
print(len(var))

fruit= "Mango"
print(len(fruit))
print(fruit[0:4])    # 0 include but 4 not include means 0->3   => Mang
print(fruit[:4])     # 0->3   Mang
print(fruit[1:4])    # 1->3   ang
print(fruit[:])      # 0 to length of string   0->5  Mango
print(fruit[0:-3])   # len(fruit)-3  => 5-3=2  => 0->1    Ma
print(fruit[-3:-1])  # 2->4  => 2-3 => ng

#Quick Quiz

rm="Harry"
print(rm[-4:-2])    # 1:3 => 1->2 => ar