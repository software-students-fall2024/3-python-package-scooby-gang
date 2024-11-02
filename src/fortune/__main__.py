import FortuneCookie as FortuneCookie

def main():
    #prints 5 good fortunes
    print("Get 5 fortunes: \n")
    FortuneCookie.quoteGetter(5)
    print("\n")

    #custom fortune cookie
    print("Custom fortune cookie: \n")
    FortuneCookie.customFortuneCookie("You will get ice cream.")
    print("\n")

    #add quote to data
    print("Custom quote added to file: \n")
    FortuneCookie.addQuote("You will get ice cream.", "g")
    print("\n")

    #random fortune
    print("Get 2 random fortune cookies: \n")
    FortuneCookie.randomFortuneCookie(2)
    print("\n")

    #fortune cookie image
    print("Fortune Cookie Image:")
    FortuneCookie.fortuneCookie()

    #cookieScript
    print("Simulated experience of getting fortunes: \n")  
    print("Shopping for fortunes: \n")
    FortuneCookie.cookieScript("s")
    print("\nCustom fortune making: \n")
    FortuneCookie.cookieScript("c")


if __name__ == "__main__":
    main()