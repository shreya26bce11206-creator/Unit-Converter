from history import save_history
def temperature_converter():

    print("\n --------- TEMPERATURE CONVERTER --------- ")

    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin" )
    print("4. Kelvin to Celsius" )

    try:
                choice = int(input("Enter your choice: "))
    except ValueError:
                print ("Kindly Enter a number :)")
                return

    if choice == 1:
        try :
            c = float(input("Enter temperature in Celsius : "))
        except ValueError:
              print ("Kindly enter a valid number :)")
              return
        f = (c *9 / 5) + 32
        print(c, "°C = ", f ,"°F" ) 
        save_history(str(c) + " °C = " + str(f) + " °F")

    elif choice == 2:
        try:
            f = float(input("Enter temperature in Fahrenheit : "))
        except ValueError:
                print ("Kindly enter a valid number :)")
                return
        c = (f - 32) * 5 / 9
        print(f , "°F = " , c, "°C")
        save_history(str(f) + " °F = " + str(c) + " °C")

    elif choice == 3:
        try:
            c = float(input("Enter temperature in Celsius : "))
        except ValueError:
            print ("Kindly enter a valid number :)")
            return
        k = c + 273.15
        print(c, "°C = ", k , "K")
        save_history(str(c) + " °C = " + str(k) + " K")


    elif choice == 4:
        try:
            k = float(input("Enter temperature in Kelvin : "))
        except ValueError:
            print ("Kindly enter a valid number :)")
            return
        c = k - 273.15
        print(k , "K = " , c , "°C")
        save_history(str(k) + " K = " + str(c) + " °C")
        

    else:
        print(" Please try again Thank you!!")

