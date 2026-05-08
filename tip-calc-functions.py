def bill_amount():
    bill = float(input("What is the bill total: "))

    return bill

def tip_percent():
    tip = int(input("Tip percent: "))

    return tip

def tip_total(bill, tip):
    total = (tip /100) * bill

    return total


def main():
    while True:
        print("\nTip Calculator")
        print("1. Calculate tip")
        print("2. Quit")

        choice = int(input("Option 1 or 2"))

        if choice == 1:
            bill = bill_amount()
            tip = tip_percent()
            total = tip_total(bill, tip)
            grand_total = bill + total

            print(f"Your total is: {grand_total:.2f}")
        elif choice == 2:
            print("Goodbye")
            break
        else:
            print("Invalid Option")

main()