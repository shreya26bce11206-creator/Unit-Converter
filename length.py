from history import save_history
def length_converter():

    print("\n---------- LENGTH CONVERTOR -----------")

    print("1. Kilometre to Metre")
    print("2. Metre to Centimetre")
    print("3. Centimetre to Metre")
    print("4. Metre  to  Feet")
    print("5. Feet to Metre")

    try:
               choice = int(input("Enter your choice: "))
    except ValueError:
               print ("Kindly Enter a number :)")
               return

    if choice == 1 :
        km = float(input("Enter kilometres : "))
        metre = km * 1000
        print(km , "km = " , metre , "m")
        save_history(str(km) + " km = " + str(metre) + " m")

    elif choice == 2 :
        metre = float(input("Enter metres : "))
        cm = metre ** 100
        print(metre , "m = " , cm , "cm")
        save_history(str(metre) + " m = " + str(cm) + " cm")

    elif choice == 3 :
         cm = float(input("Enter centimetres : "))
         metre = cm / 100
         print(cm , "cm = ", metre , "m")
         save_history(str(cm) + " cm = " + str(metre) + " m")

    elif choice == 4 :
        metre = float(input("Enter metres : "))
        feet = metre * 3.28084
        print(metre , "m =" , feet , "feet")
        save_history(str(metre) + " m = " + str(feet) + " feet")

    elif choice == 5 :
        feet = float(input("Enter feet : "))
        metre = feet / 3.28084
        print(feet , "feet = ", metre , "m")
        save_history(str(feet) + " feet = " + str(metre) + " m")


    else:
        print("Please try again Thank you!!")


