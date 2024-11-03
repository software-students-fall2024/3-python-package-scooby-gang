import FortuneCookie as FortuneCookie

def main():
    print("Welcome to Scooby's Fortunes!")

    option = input("Do you want to generate random fortunes or create your own? (r for random, c for create)")

    if option != "c" or option != "r":
        print("Invalid options")
    else: 
        FortuneCookie.cookieScript(option)


if __name__ == "__main__":
    main()