def main():
    while True:
        try:
            dollars = float(input("Change owed: "))
            if dollars >= 0:
                break
            else:
                print("Please enter a non-negative value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    cents = round(dollars * 100)

    quarters = cents // 25
    dimes = (cents % 25) // 10
    nickels = ((cents % 25) % 10) // 5
    pennies = ((cents % 25) % 10) % 5

    total_coins = quarters + dimes + nickels + pennies
    print(total_coins)

if __name__ == "__main__":
    main()
