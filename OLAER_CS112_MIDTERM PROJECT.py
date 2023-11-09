# POS System for our family's company: ALO KLEEN CHEMICAL PRODUCTS TRADING.
# The program only contains functions that are taught so far in my CS112 class, although some are not
# yet tackled, I did my best only to incorporate the lessons that are already discussed in our class.
# Revisions will be done as we tackle more lessons in Python.

def wholesale():  # wholesale function, displays prices and processes the transaction.
    print("\n   Product Name              (1) Gallon         (2) Liter"  
          "\n1. Dishwashing Liquid            175.00             50.00"
          "\n2. Liquid Detergent              275.00             95.00"
          "\n3. Fabric Conditioner            200.00             75.00"
          "\n4. Toilet Bowl Cleaner           295.00            100.00"
          "\n5. Medicated Hand Soap           235.00             75.00"
          "\n6. Payment"
          "\n7. Exit")  # The product prices in wholesale, and option to check out and exit.

    total = 0
    errors = 0
    cost_list = []  # Lists of all instances of cost.

    while True:  # Choosing of product, packaging, and quantity loop.
        cost = 0
        while True:  # Prompts to choose an option, and validates the chosen option.
            try:
                option = int(input("\nChoose an option: "))
                if 1 <= option <= 7:
                    break
                else:
                    print("Invalid option. Choose only between 1 - 7.")
                    errors = errors + 1
            except ValueError:
                print("Enter a number only.")
                errors = errors + 1

            if errors == 3:
                print("\n   Product Name              (1) Gallon         (2) Liter"
                      "\n1. Dishwashing Liquid            175.00             50.00"
                      "\n2. Liquid Detergent              275.00             95.00"
                      "\n3. Fabric Conditioner            200.00             75.00"
                      "\n4. Toilet Bowl Cleaner           295.00            100.00"
                      "\n5. Medicated Hand Soap           235.00             75.00"
                      "\n6. Payment"
                      "\n7. Exit")  # The product prices in wholesale, and option to check out and exit.
                errors = 0

        if option == 6:  # Breaks loop when checkout is chosen
            break
        elif option == 7:  # Exits program when the exit is chosen.
            print("\nThank you for your time\n\n-Exiting Program-"), exit()

        while True:  # Prompts to choose a packaging, and validates the chosen packaging.
            try:
                pack = int(input("Choose Packaging: "))
                if 1 <= pack <= 2:
                    break
                else:
                    print("Invalid option. Choose only between 1 or 2.\n")
                    errors = errors + 1
            except ValueError:
                print("Enter a number only.\n")
                errors = errors + 1

            if errors == 3:
                print("\n   Product Name              (1) Gallon         (2) Liter"
                      "\n1. Dishwashing Liquid            175.00             50.00"
                      "\n2. Liquid Detergent              275.00             95.00"
                      "\n3. Fabric Conditioner            200.00             75.00"
                      "\n4. Toilet Bowl Cleaner           295.00            100.00"
                      "\n5. Medicated Hand Soap           235.00             75.00"
                      "\n6. Payment"
                      "\n7. Exit\n"
                      "\nChosen Option: " + str(option))  # The product prices in wholesale, and option to
                # check out and exit.
                errors = 0

        # Determines the price according to the option and packaging chosen.
        if option == 1:
            if pack == 1:
                cost = cost + 175
            else:
                cost = cost + 50
        elif option == 2:
            if pack == 1:
                cost = cost + 275
            else:
                cost = cost + 95
        elif option == 3:
            if pack == 1:
                cost = cost + 200
            else:
                cost = cost + 75
        elif option == 4:
            if pack == 1:
                cost = cost + 295
            else:
                cost = cost + 100
        elif option == 5:
            if pack == 1:
                cost = cost + 235
            else:
                cost = cost + 75
        else:
            break

        while True:  # Prompts to enter quantity, and validates the entered quantity.
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    cost_list.append(cost * quantity)  # Adds the instance of cost to a list.
                    print("Cost: " + str(cost * quantity))
                    break
                else:
                    print("Invalid quantity.\n")
                    errors = errors + 1

            except ValueError:
                print("Enter a number only.\n")
                errors = errors + 1

            if errors == 4:
                print("\n   Product Name              (1) Gallon         (2) Liter"
                      "\n1. Dishwashing Liquid            175.00             50.00"
                      "\n2. Liquid Detergent              275.00             95.00"
                      "\n3. Fabric Conditioner            200.00             75.00"
                      "\n4. Toilet Bowl Cleaner           295.00            100.00"
                      "\n5. Medicated Hand Soap           235.00             75.00"
                      "\n6. Payment"
                      "\n7. Exit\n"
                      "\nChosen Option: " + str(option) +
                      "\nChosen Packaging: " + str(pack))  # The product prices in wholesale, and option to
                # check out and exit.
                errors = 0

        # sums the total cost.
        total = total + (cost * quantity)
    # Prompts to have another transaction when no product is selected.
    if total == 0:
        print("\nNo option selected.")
        confirm()

    print("Cost: " + str(cost_list))  # Displays cost breakdown.
    print("Total Cost: " + str(total) + "\n")  # Displays total cost.

    while True:  # Prompts to enter payment amount, and validates the entered payment amount.
        try:
            payment = int(input("Amount Received: "))
            if payment > total:
                break

            else:
                print("Invalid amount.\n")

        except ValueError:
            print("Enter a number only.\n")

    change = payment - total  # Calculates the change

    print("Change: " + str(change))  # Displays the change
    confirm()  # Prompts to have another transaction


def retail():  # retail function, displays prices and processes the transaction.
    print("\n   Product Name              (1) Gallon         (2) Liter"
          "\n1. Dishwashing Liquid            200.00             65.00"
          "\n2. Liquid Detergent              315.00            110.00"
          "\n3. Fabric Conditioner            250.00             95.00"
          "\n4. Toilet Bowl Cleaner           350.00            110.00"
          "\n5. Medicated Hand Soap           250.00             85.00"
          "\n6. Payment"
          "\n7. Exit")  # The product prices in retail, and option to check out and exit.

    total = 0
    errors = 0
    cost_list = []  # Lists of all instances of cost.

    while True:  # Choosing of product, packaging, and quantity loop.
        cost = 0
        while True:  # Prompts to choose an option, and validates the chosen option.
            try:
                option = int(input("\nChoose an option: "))
                if 1 <= option <= 7:
                    break
                else:
                    print("Invalid option. Choose only between 1 - 7.")
                    errors = errors + 1
            except ValueError:
                print("Enter a number only.")
                errors = errors + 1

            if errors == 3:
                print("\n   Product Name              (1) Gallon         (2) Liter"
                      "\n1. Dishwashing Liquid            200.00             65.00"
                      "\n2. Liquid Detergent              315.00            110.00"
                      "\n3. Fabric Conditioner            250.00             95.00"
                      "\n4. Toilet Bowl Cleaner           350.00            110.00"
                      "\n5. Medicated Hand Soap           250.00             85.00"
                      "\n6. Payment"
                      "\n7. Exit")  # The product prices in retail, and option to check out and exit.
                errors = 0

        if option == 6:  # Breaks loop when checkout is chosen
            break
        elif option == 7:  # Exits program when the exit is chosen.
            print("\nThank you for your time\n\n-Exiting Program-"), exit()

        while True:  # Prompts to choose a packaging, and validates the chosen packaging.
            try:
                pack = int(input("Choose Packaging: "))
                if 1 <= pack <= 2:
                    break
                else:
                    print("Invalid option. Choose only between 1 or 2.\n")
                    errors = errors + 1
            except ValueError:
                print("Enter a number only.\n")
                errors = errors + 1

            if errors == 3:
                print("\n   Product Name              (1) Gallon         (2) Liter"
                      "\n1. Dishwashing Liquid            200.00             65.00"
                      "\n2. Liquid Detergent              315.00            110.00"
                      "\n3. Fabric Conditioner            250.00             95.00"
                      "\n4. Toilet Bowl Cleaner           350.00            110.00"
                      "\n5. Medicated Hand Soap           250.00             85.00"
                      "\n6. Payment"
                      "\n7. Exit\n"
                      "\nChosen Option: " + str(option))  # The product prices in wholesale, and option to
                # check out and exit.
                errors = 0

        # Determines the price according to the option and packaging chosen.
        if option == 1:
            if pack == 1:
                cost = cost + 200
            else:
                cost = cost + 65
        elif option == 2:
            if pack == 1:
                cost = cost + 315
            else:
                cost = cost + 110
        elif option == 3:
            if pack == 1:
                cost = cost + 250
            else:
                cost = cost + 95
        elif option == 4:
            if pack == 1:
                cost = cost + 350
            else:
                cost = cost + 110
        elif option == 5:
            if pack == 1:
                cost = cost + 250
            else:
                cost = cost + 85
        else:
            break

        while True:  # Prompts to enter quantity, and validates the entered quantity.
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    cost_list.append(cost * quantity)  # Adds the instance of cost to a list.
                    print("Cost: " + str(cost * quantity))
                    break
                else:
                    print("Invalid quantity.\n")
                    errors = errors + 1

            except ValueError:
                print("Enter a number only.\n")
                errors = errors + 1

            if errors == 4:
                print("\n   Product Name              (1) Gallon         (2) Liter"
                      "\n1. Dishwashing Liquid            200.00             65.00"
                      "\n2. Liquid Detergent              315.00            110.00"
                      "\n3. Fabric Conditioner            250.00             95.00"
                      "\n4. Toilet Bowl Cleaner           350.00            110.00"
                      "\n5. Medicated Hand Soap           250.00             85.00"
                      "\n6. Payment"
                      "\n7. Exit\n"
                      "\nChosen Option: " + str(option) +
                      "\nChosen Packaging: " + str(pack))  # The product prices in wholesale, and option to
                # check out and exit.
                errors = 0

        # sums the total cost.
        total = total + (cost * quantity)
    # Prompts to have another transaction when no product is selected.
    if total == 0:
        print("\nNo product selected.")
        confirm()

    print("Cost: " + str(cost_list))  # Displays cost breakdown.
    print("Total Cost: " + str(total) + "\n")  # Displays total cost.

    while True:  # Prompts to enter payment amount, and validates the entered payment amount.
        try:
            payment = int(input("Amount Received: "))
            if payment > total:
                break

            else:
                print("Invalid amount.\n")

        except ValueError:
            print("Enter a number only.\n")

    change = payment - total  # Calculates the change

    print("Change: " + str(change))  # Displays the change
    confirm()  # Prompts to have another transaction


def sale():  # sale function, contains the option between wholesale and retail.
    print("\nSales Type:\n1. Wholesale\n2. Retail")

    while True:  # Prompts to choose a sales type, and validates the chosen sales type.
        try:
            sales_type = int(input("\nChoose Sales Type:"))

            if sales_type == 1:
                wholesale()
            elif sales_type == 2:
                retail()
            else:
                print("Choose only between 1 and 2.")

        except ValueError:
            print("Enter a number only.")


def confirm():  # confirm function, prompts to have another transaction or not.
    while True:  # Prompts to choose to have another transaction or not, and validates the chosen answer.
        again = input("\nWould you like to have another transaction? (y/n): ")

        if again.lower() == 'n':
            print("\nThank you for your time\n\n-Exiting Program-"), exit()
        elif again.lower() == 'y':
            print("\n\n\n\n")
            header()
        else:
            print("Invalid Option. Please enter 'y' or 'n'.\n")


def header():  # prints the header of the code and proceeds to the sale function
    print("\n--------- WELCOME TO THE SIMPLE CASHIERING SYSTEM ---------")
    print("\nCOMPANY: ALO KLEEN CHEMICAL PRODUCTS TRADING")
    sale()


header()
