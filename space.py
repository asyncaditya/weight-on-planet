print("Find out your Weight on Different Planets:\n")
 
weight = int(input("Please enter your current Weight: "))

print("\n1. Venus   2. Mars    3. Jupiter")
print("4. Saturn  5. Uranus  6. Neptune\n")

planet = int(input("Please enter a Planet number: "))

if planet == 1:
  print(weight*0.91)
elif planet == 2:
  print(weight*0.38)
elif planet == 3:
  print(weight*2.34)
elif planet == 4:
  print(weight*1.06)
elif planet == 5:
  print(weight*0.92)
else:
  print(weight*1.19)
