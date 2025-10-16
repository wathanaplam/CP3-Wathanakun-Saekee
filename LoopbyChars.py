
def main ():
    number = int(input("Enter the number: "))
    text = ""

    for i in range(number):
        text = text + "*"
        print(text)

    #print(number * "*")

if __name__ == "__main__":
    main()
