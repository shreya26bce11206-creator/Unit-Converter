from history import save_history
def speed_converter():


    print("\n -------- Speed Converter --------")


    print("1. Km/hr to m/sec")
    print("2. m/sec to Km/hr")
    print("3. Miles/hr to Km/hour")
    print("4. Km/hr to Miles/hr")

    try:
                choice = int(input("Enter your choice: "))
    except ValueError:
                print ("Kindly Enter a number :)")
                return
    
    value = float(input("Enter the value: "))

    if choice == 1:
        result = value / 3.6
        print(value, "km/h =", result, "m/s")
        save_history(str(value) + " km/h = " + str(result) + " m/s")

    elif choice == 2:
        result = value * 3.6
        print(value, "m/s =", result, "km/h")
        save_history(str(value) + " m/s = " + str(result) + " km/h")

    elif choice == 3:
        result = value * 1.60934
        print(value, "mph =", result, "km/h")
        save_history(str(value) + " mph = " + str(result) + " km/h")

    elif choice == 4:
        result = value / 1.60934
        print(value, "km/h =", result, "mph")
        save_history(str(value) + " km/h = " + str(result) + " mph")

    else:
        print("Please try again Thank you!!")

        