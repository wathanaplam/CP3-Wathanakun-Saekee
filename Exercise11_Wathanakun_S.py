
def main ():
    number = int(input("Enter the number: "))
    text = ""
    
    for x in range(number + 1):
        text = "*" * (2 * x - 1)
        spaces = " " * (number - x)
        print(spaces + text + spaces)

if __name__ == "__main__":
    main()
