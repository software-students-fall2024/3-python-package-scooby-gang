import FortuneCookie as FortuneCookie

def main():
    #prints 5 good fortunes
    FortuneCookie.quoteGetter(5)

    #custom fortune cookie
    FortuneCookie.customFortuneCookie("You will get ice cream.")

    #add quote to data
    FortuneCookie.addQuote("You will get ice cream.", "g")

    #random fortune
    FortuneCookie.randomFortuneCookie(2)

    #fortune cookie image
    FortuneCookie.fortuneCookie()

    #cookieScript
    FortuneCookie.cookieScript("s")
    FortuneCookie.cookieScript("c")


if __name__ == "__main__":
    main()