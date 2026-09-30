from history import save_history
def weight_converter():

    print("\n------ WEIGHT CONVERTOR ------ ")

    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    print("3. Kilogram to Pound")
    print("4. Pound to Kilogram")


    try:
            choice = int(input("Enter your choice: "))
    except ValueError:
            print ("Kindly Enter a number :)")
            return

    if choice == 1:
        kg = float(input("Enter kilograms : "))
        gram = kg * 1000
        print(kg , "kg =" , gram , "g")
        save_history(str(kg) + "kg = " + str(gram) + "g")


    elif choice == 2:
        gram = float(input("Enter grams : "))
        kg = gram / 1000
        print(gram ,"g=" , kg ,"kg")
        save_history(str(gram) + "g = " + str(kg) + "kg")
        


    elif choice == 3:
        kg = float(input("Enter kilograms : "))
        pound = kg * 2.20462
        print(kg, "kg = " , pound, "pounds")
        save_history(str(kg) + "kg = " + str(pound) + "pounds")
        


    elif choice == 4:
        pound = float(input("Enter pounds : "))
        kg = pound / 2.20462
        print(pound , "pounds = ", kg , "kg")
        save_history(str(pound) + "kg = " + str(kg) + "kg")
        


    else:
        print(" Please try again Thank you!!")

