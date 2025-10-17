
def VATcalculate (totalprice):
    vat = totalprice * 7 / 100
    result = totalprice + vat
    return result

def main():
    inputprice = int(input("Enter price: "))
    print("Total", VATcalculate(inputprice))

if __name__ == "__main__":
    main()
