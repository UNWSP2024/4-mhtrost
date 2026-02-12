def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         
    

budget = float(input("Enter your budget amount for this month: $"))
total = 0.0

while True:
    spent = float(input("Please enter an expense as a numerical number (Enter '0' to end): $"))
    total += spent

    if spent == 0:
        break

difference = budget - total

if difference > 0:
    print(f"You have ${abs(difference):.2f} left.")

if difference < 0:
    print(f"You are ${abs(difference):.2f} over budget.")

if difference == 0:
    print("You have gone neither over or under your budget goal. Congratulations!")


if __name__ == '__main__':
    main()