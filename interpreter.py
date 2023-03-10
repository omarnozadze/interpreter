expression =input("Expression:")

x, y, z = expression.split(" ")


x= float(x)
z= float(z)


if y== "+":
   result = x+z
   print (result)
elif y== "-":
   result = x-z
   print (result)
elif y== "*":
   result = x*z
   print (result)
elif y== "/":
   result = x/z
   print (result)



