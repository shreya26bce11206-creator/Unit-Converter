from history import save_history
def data_converter():

    print("\n ------- DATA STORAGE CONVERTER -------")

    print("1. Bytes to KB")
    print("2. KB to MB")
    print("3. MB to GB")
    print("4. GB to MB")

    try:
                choice = int(input("Enter your choice: "))
    except ValueError:
                print ("Kindly Enter a number :)")
                return

    if choice == 1:
        byte = float(input("Enter bytes : "))
        kb = byte / 1024
        print (byte , "bytes = " , kb , "KB")
        save_history(str(byte) + " byte = " + str(kb) + " KB")

    elif choice == 2:
        kb = float(input("Enter KB : "))
        mb = kb / 1024
        print (kb , "KB = " , mb , "MB")
        save_history(str(kb) + " KB = " + str(mb) + " MB")

    elif choice == 3:
        mb = float(input("Enter MB : "))
        gb = mb / 1024
        print (mb , "MB = " , gb , "GB")
        save_history(str(mb) + " MB = " + str(gb) + " GB")

    elif choice == 4:
        gb = float(input("Enter GB : "))
        mb = gb * 1024
        print (gb , "GB = " , mb , "MB" )
        save_history(str(gb) + " GB = " + str(mb) + " MB")

    else:
        print (" Please try again Thank you!!")



    