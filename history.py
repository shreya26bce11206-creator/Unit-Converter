def save_history(data):
    f = open("history.txt", "a")
    f.write(data + "\n")
    f.close()


def show_history():
    try:
        f = open("history.txt", "r")
        data = f.read()
        f.close()

        if data == "":
            print(" Sorry no history available!")

        else:
            print("\n----- CONVERSION HISTORY -----")
            print(data)

    except FileNotFoundError:
        print(" Sorry no history available!")