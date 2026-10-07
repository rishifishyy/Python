# calculator program 
bill=int(input("Enter the total Bill: \n"))
tip=int(input("Tip % , enter without the sign: \n"));
tip_amount=tip/100*bill;
total_amount=tip_amount+bill;
people=int(input("How many people ate the food? \n"));
split_amount=total_amount/people
print(f"You have to pay ${split_amount}\n");
