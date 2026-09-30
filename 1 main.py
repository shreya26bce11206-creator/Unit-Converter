from history import show_history
from weight import weight_converter
from temperature import temperature_converter
from length import length_converter
from timeee import time_converter
from storage import data_converter
from speed import speed_converter


while True:

    print("\n===== UNIT CONVERTER =====")

    print("1. Weight Converter")
    print("2. Temperature Converter")
    print("3. Length Converter")
    print("4. Time Converter")
    print("5. Data Converter")
    print("6. Speed Converter")
    print("7. View History")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print ("Kindly Enter a number :)")
        continue


    if choice == 1:
        weight_converter()
    elif choice == 2:
        temperature_converter()

    elif choice == 3:
        length_converter()

    elif choice == 4:
        time_converter()

    elif choice == 5:
        data_converter()

    elif choice == 6:
        speed_converter()

    elif choice == 7:
        
        show_history()
         
    elif choice == 8: 
        print("Thank you for using Unit Converter!")


        break

    else:
        print("Please try again Thank you!!")