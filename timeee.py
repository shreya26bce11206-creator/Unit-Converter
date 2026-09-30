from history import save_history
def time_converter():

    print("\n ------- TIME CONVERTER -------")

    print("1. Hours to Minutes")
    print("2. Minutes to Seconds")
    print("3. Days to Hours")
    print("4. Minutes to Hours")

    try:
            choice = int(input("Enter your choice: "))
    except ValueError:
            print ("Kindly Enter a number :)")
            return

    if choice == 1:
        hours = float(input("Enter hours : "))
        minutes = hours * 60
        print(hours , "hours = " , minutes , "minutes")
        save_history(str(hours) + " hours = " + str(minutes) + " minutes")

    elif choice == 2:
        minutes = float(input("Enter minutes : "))
        seconds = minutes * 60
        print(minutes , "minutes = " , seconds , "seconds")
        save_history(str(minutes) + " minutes = " + str(seconds) + " seconds")

    elif choice == 3: 
        days = float(input("Enter days : "))
        hours = days * 24
        print(days , "days = ", hours , "hours")
        save_history(str(days) + " days = " + str(hours) + " hours")

    elif choice == 4:
        minutes = float(input("Enter minutes : "))
        hours = minutes / 60
        print(minutes , "minutes = ", hours , "hours")
        save_history(str(minutes) + " minutes = " + str(hours) + " hours")


    else:
        print(" Please try again Thank you!!")


