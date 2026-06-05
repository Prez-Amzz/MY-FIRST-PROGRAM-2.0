from datetime import date

items = {
    "food" : 20,
    "water" : 3,
    "soda" : 7,
    "chips" : 10,
    "toiletry" : 100
 }

print("-------WELCOME TO THE CHECKOUT-------")
print()
print()

for k, v in items.items():
    print(f"[{k:<5}- ${v}]")

choices = []
print()
print("To use please enter choice. Enter quit to move on when finished and exit to leave program")

while True:
    print()
    choice = input("Enter choice: ")

    if choice in items:
        choices.append(choice)
    elif choice == "quit":
        break
    elif choice.strip().lower() == "exit":
        print("Goodbye!")
        exit()
    else:
        print("Please enter a valid choice.")
        continue

total = 0
while True:
    for i in choices:
        print("You entered ", i, "which costs ", "$",items[i])
        total += items[i]

    print(f" Your total's {total}, will you like to proceed the purchase?")
    print("Enter yes/no")
    ans = input()

    if ans.strip().lower() == "yes":
        print("PURCHASE CONFIRMED ON-", date.today())
        print("COME AGAIN LATER!")
        print("GOODBYE! <3")
        exit()
    elif ans.strip().lower() == "no":
        while True:
            print('Would you like to remove any item from your list?(yes/no)')
            response = input().strip().lower()
            if response == "yes":
                for i in choices:
                    print("You entered ", i, "which costs ", "$",items[i])
                print("How many would you like to remove?")
                while True:
                    try:
                        k = int(input())

                    except ValueError:
                        print("Mst be an integer.")
                        continue

                    for i in range(k):
                        m = input("Enter item to remove: ")

                        if m not in choices:
                            print("Enter item in your cart!")
                            continue
                        else:
                            choices.remove(m)
                            total -= items[m]

                    print()
                    print("Now you have: ")
                    for i in choices:
                        print(i, ",which costs $",items[i])
                    break

                print("Now, you have a total of $", total, " will you like to proceed the purchase?")
                print("Enter yes/no")
                answer = input()

                if answer.strip().lower() == "yes":
                    print("PURCHASE CONFIRMED ON-", date.today())
                    print("COME AGAIN LATER!")
                    print("GOODBYE! <3")
                    exit()
                elif answer.strip().lower() == "no":
                    print("Goodbye!")
                    print("Thanks for your time! Come back soon!")
                    exit()
            elif response.strip().lower() == "no":
                while True:
                    l = input('Would you like to add any item from your list?(yes/no)')
                    if l == "yes":
                        for n, v in items.items():
                            print(f"[{n:<5}- ${v}]")
                        try:
                            print("How many would you like to add?")
                            amount = int(input())
                            if amount == 0 or amount < 0:
                                print("Must be an integer above 0.")
                                continue

                            for i in range(amount):
                                print("Enter item to add: ")
                                w = input()

                                if w not in items.keys():
                                    print("Invalid item. We don't sell that here.")
                                    continue
                                else:
                                    choices.append(w)
                                    total += items[w]

                        except ValueError:
                            print("Must be an integer.")

                        print("Now you have: ")
                        for i in choices:
                            print(i, ",which costs $",items[i])

                        print("Now your total's $", total, " will you like to proceed the purchase?")
                        print("Enter yes/no to complete")
                        answer = input()

                        if answer.strip().lower() == "yes":
                           print("PURCHASE CONFIRMED ON-", date.today())
                           print("COME AGAIN LATER!")
                           print("GOODBYE!! <3")
                           exit()

                        elif answer.strip().lower() == "no":
                            print("Goodbye!")
                            print("Thanks for your time! Come back soon!")
                            exit()




                    elif l == "no":
                        print("Goodbye!")
                        exit()
                    else:
                        print("Please enter a valid choice.")
                        continue

            else:
                print("Please enter a valid choice.")
                continue
    else:
        print("Please enter a valid choice.")
        continue

    print()
    print()

