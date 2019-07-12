"""Couting bobs."""

password = input("Enter your password: \n")

if password == "password":
    loop = "y"
    while loop == "y":

        text = input("Give me a bob text: ").lower()

        bobs = 0

        for i in range(len(text)):
            if text[i: i+3] == 'bob':
                bobs += 1

        print("There are {} bobs".format(bobs))
        loop = input("Do you want to count bobs again? y/n\n").lower()

    else:
        print("See you! :)")

else:
    print("Sorry your password is incorrect :(")
