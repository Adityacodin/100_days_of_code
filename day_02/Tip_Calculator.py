print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? : "))
tip_percent = int(input("What percentage of tip would you like to give? 10/12/15: "))/100
tip = tip_percent*total_bill
people_count = int(input("How many people to split the bill among?: "))

each_person_amt = round((total_bill + tip)/people_count,2)
print(f"Each person should pay : {each_person_amt}")