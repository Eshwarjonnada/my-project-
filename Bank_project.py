print("="*20)

customer_names = ["Eshwar","Rahul","Murali","Manu","Rohith"]
customer_pins = ["012","0123","234","0345","125"]
customer_balance = [10000,40000,50000,12000,15000]
withdraw = 0
depost = 0
balence = 0
counter_1 = 1
counter_ = 5
i = 0

# This statement below helps the program to run continuously.

while True:

    # os.system("cls")

    print("---------------------------------")
    print("   WELCOME TO THE MONEY BANK     ")
    print("---------------------------------")
    print("1.OPEN NEW ACCOUNT :- ")
    print("2.WHITDRAW         :- ")
    print("3.DEPOSIT          :- ")
    print("4.BALENCE CHECK    :- ")
    print("5.EXIT / QUIT      :- ")
    
    # The below statement takes the choice number from the user.

    choice_number = input("ENTER YOUR CHOICE NUMBER : ")

    if choice_number == "1":
        print("YOU HAVE SELECTED THE 1st NUMBER TO CREAT A NEW ACCOUNT ")

        # The line below will take the no:of customers from the user.

        NOC = eval(input("NUMBER OF CUSTOMERS : "))
 
        i = i + NOC

        # The if condition will restrict the number of new account to 5.

        if i > 5:

            print("\n")
            print("CUSGTOMER REGESTRATION MAXIMUM REACHED")
            i = i - NOC
        else:

            # The while loop will run according to the no:of customers.

            while counter_1 <= i:

                # These few lines will take information from customer and then append them to the list.

                name = input("ENTER YOUR FULL NAME : ")
                customer_names.append(name)
                pin = str(input("ENTER YOUR PIN CHOICE : "))
                customer_pins.append(pin)
                balance = 0
                deposition = eval(input("ENTER YOUR AMOUNT FOR DEPOSIT FOR YOUR NEW ACCOUNT : "))
                balance = balance + deposition
                customer_balance.append(balance)
                print("\nNAME =", end=" ")
                print(customer_names[counter_1])
                print("PIN =", end=" ")
                print(customer_pins[counter_1])
                print("BALANCE =", end=" ")
                print(customer_balance[counter_1], end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1
                counter_2 = counter_1 + 1
                print("-------------------------------------------------------")
                print("YOUR NAME, PIN & BALENCEE IS  ADDED TO THE BANK ACCOUNT")
                print("--------CUSTOMER ACCOUNT CREATED SUCCESSFULLY!---------")
                print("\n")
                print("YOUR NAME IS AVAILABLE ON THE CUSTOMER LIST : ")
                print(customer_names)
                print("\n")
                print("NOTE! PLEASE REMEMBER NAME AND PIN")
                print("-------------------------------------------------------")

                # This statement below helps the user to go back to the start of the program (main menu).

        main_menu = input("PRESS ANY NUMBER TO PERFORM MAIN TASK OR EXIT :")
    elif choice_number == "2":
        j = 0
        print("2 nd OPTION SELECTED BY CUSTOMER")

        # This while loop will prevent the user using the account if the username or pin is wrong.

        while j < 1:
            k = -1
            name = input("PLEASE ENTER YOUR NAME : ")
            pin = input("PLEASE ENTER YOUR PIN : ")

            # This while loop will keep the function running when variable k is smaller than length of the
            # customerNames list.

            while k < len(customer_names) - 1:
                k = k + 1
                
                # These two if conditions find where both the name and pin matches.

                if name == customer_names[k]:
                    if pin == customer_pins[k]:
                        j = j + 1

                        # These few statement would show the balance taken from the list.

                        print("YOUR CURRENT BALANCE IS :", end=" ")
                        print(customer_balance[k], end=" ")
                        print("-/Rs\n")
                        balance = (customer_balance[k])

                        # Statement below would take the amount to withdraw from user.

                        withdraw = eval(input("ENTER AMOUNT FOR WITHDRAW : "))

                        # The if condition below would look whether the withdraw is greater than the balance.
                        if withdraw > balance:

                            # This statement below would take a deposition from the customer.

                            deposit = eval(input("PLEASE DEPOSIT FOR MAINTAIN MINIMUM BALANCE : "))

                            # These few statements would update the value and show the balance to user.

                            balance = balance + deposit
                            print("YOUR CURRENT BALANCE IS :", end=" ")
                            print(balance, end=" ")
                            print("-/Rs\n")
                            balance = balance - withdraw
                            print("-\n")
                            print("----WITHDRAW IS SUCCESSFULL!----")
                            customer_balance[k] = balance
                            print("YOUR NEW BALANCE IS : ", balance, end=" ")
                            print("-/Rs\n\n")
                        else:
                            # Else condition mentioned above is to do withdrawal if the balance is greater than the
                            # withdraw amount.

                            balance = balance - withdraw

                            # These few statement would update the values in the list and show it to the customer.

                            print("\n")
                            print("----WITHDRAW IS SUCCESSFULL!----")
                            customer_balance[k] = balance
                            print("YOUR NEW BALANCE IS : ", balance, end=" ")
                            print("-/Rs\n\n")
            if j < 1:

                # The if condition above would work when the pin or the name is wrong.

                print("YOUR NAME AND PIN DOES NOT MATHCH!\n")
                break

            # This statement below helps the user to go back to the start of the program (main menu).

        main_menu = input("PRESS ANY NUMBER TO PERFORM MAIN TASK OR EXIT :")
    elif choice_number == "3":
        print("3 rd OPTION IS DELECTED BY THE CUSTOMER")
        n = 0

        # The while loop below would work when the pin or the username is wrong.

        while n < 1:
            k = -1
            name = input("PLEASE ENTER YOUR NAME : ")
            pin = input("PLEASE ENTER YOUR PIN : ")

            # The while loop below will keep the function running to find the correct user.

            while k < len(customer_names) - 1:
                k = k + 1

                # The two if conditions below would find whether both the pin and the name is correct.

                if name == customer_names[k]:
                    if pin == customer_pins[k]:
                        n = n + 1

                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.

                        print("YOUR CURRENT BALANCE : ", end=" ")
                        print(customer_balance[k], end=" ")
                        print("-/Rs")
                        balance = (customer_balance[k])

                        # This statement below takes the depositionn from the customer.

                        deposition = eval(input("ENTER AMOUT FOR DEPOSIT: "))
                        balance = balance + deposition
                        customer_balance[k] = balance
                        print("\n")
                        print("----DEPOSIT IS SUCCESSFULL!----")
                        print("YOUR NEW BALANCE : ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("YOUR NAME AND PIN DOES NOT MATCH!\n")
                break

            # This statement below helps the user to go back to the start of the program (main menu).

        main_menu = input("PRESS ANY NUMBER TO PERFORM MAIN TASK OR EXIT :")
    elif choice_number == "4":
        print("4 th OPTION IS SELECTED BY THE CUSTOMER")
        k = 0
        print("CUSTOMER DETAILS MENTIONED BELOW : ")
        print("\n")

        # The while loop below will keeping running until all the customers and balances are shown.

        while k <= len(customer_names) - 1:
            print(">> CUSTOMER :=", customer_names[k])
            print(">> BALANCE  :=", customer_balance[k], end=" ")
            print("-/Rs")
            print("\n")
            k = k + 1

            # This statement below helps the user to go back to the start of the program (main menu).

        mainMenu = input("PRESS ANY NUMBER TO PERFORM MAIN TASK OR EXIT :")
    elif choice_number == "5":

        # These statements would be just showed to the customer.

        print("5th OPTION IS SELECTED BY THE CUSTOMER")
        print("\n")
        print("THANK YOU FOR USING OUR MONEY BANKING SYSTEM!")
        print("----------------<<TAKE CARE>>----------------")
        break
    else:
        # This else function above would work when a wrong function is chosen.

        print("SELECTED INVALID OPTION PLEASE TRY AGAIN")

        # This statement below helps the user to go back to the start of the program (main menu).

        main_menu = input("PRESS ANY NUMBER TO PERFORM MAIN TASK OR EXIT :")