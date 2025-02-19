userNameInput = input("Enter Username: ")
passWordInput = input("Enter Password: ")

existsUserName = "test"
existsPassword = "1234"

if userNameInput == existsUserName and passWordInput == existsPassword:
    print("Login Success")
    print("--------- Welcome to Python shop ---------")
    print("--------- List of product ---------")
    print("1. Video Game", "Price: 1790")
    print("2. Booster pack", "Price: 590")
    print("3. Trading card", "Price: 495")
    selectedProduct = int(input("Please select product: "))
    if selectedProduct == 1:
        quantity = int(input("Please enter number of quantity: "))
        videoGamePrice = 1790.00
        print("Total Price:", videoGamePrice * quantity)
    if selectedProduct == 2:
        quantity = int(input("Please enter number of quantity: "))
        boosterPackPrice = 590.00
        print("Total Price:", boosterPackPrice * quantity)
    if selectedProduct == 3:
        quantity = int(input("Please enter number of quantity: "))
        tradingCardPrice = 495.00
        print("Total Price:", tradingCardPrice * quantity)
else:
    print("Username or Password incorrect")
