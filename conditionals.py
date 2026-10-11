# conditionals
# height=int(input("Enter your height\n"));
# if height >= 165:
#   print("You are allowed to ride ")
# else:
#   print("You are not allowed to ride ")
#BMI CALC 
size= input("What size do you want S,M OR L : ")
pepperoni=input("Do you want Pepperoni? Y OR N : ")
extra_cheese=input("Do you want Extra cheese? Y or N: ")
cost=0;
size = input("What size do you want S, M OR L: ")
pepperoni = input("Do you want Pepperoni? Y OR N: ")
extra_cheese = input("Do you want Extra cheese? Y OR N: ")

cost = 0

if size == "S":
    cost += 15
    if pepperoni == "Y":
        cost += 2
    if extra_cheese == "Y":
        cost += 1

elif size == "M":
    cost += 20
    if pepperoni == "Y":
        cost += 2
    if extra_cheese == "Y":
        cost += 1

else:
    cost += 25
    if pepperoni == "Y":
        cost += 3
    if extra_cheese == "Y":
        cost += 1

print(f"The cost of your {size} pizza\npepperoni: {pepperoni}\nextra_cheese: {extra_cheese}\nis: ${cost}")

  
        