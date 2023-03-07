def menu():
    print("Menu")
    print("-----------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(string):
    encoded_string = ""
    for num in string:
        encoded_string = encoded_string + str(int(num) + 3)
    return encoded_string


def main():
    cont = True
    while cont:
        menu()
        option = int(input("Please choose an option:"))
        if option == 1:
            string = input("Please enter your password to encode:")
            encoded_string = encode(string)
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {encoded_string}, and the original password is {string}")
        elif option == 3:
            cont = False


if __name__ == '__main__':
    main()
