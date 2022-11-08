#import partials (logo,menu)
import logo

# import only system from os
from os import system, name
 
# import sleep to show output for some time period
from time import sleep

print(logo.logo)
print(logo.menu)

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux
    else:
        _ = system('clear')


def add_account(account):
    account_list = [account]

    return account_list


def print_rates(rates_list):
    my_list = []
    for items in rates_list:
        my_list.append(items)

    return my_list


def total_variable_charges(list):
    total = 0
    for ele in range(0, len(list)):
        total = total + float(list[ele])

    return_this = float("{:.2f}".format(total))
    return "{:.2f}".format(return_this)


def total_fixed_charges(fc_list):
    total = 0

    for ele in range(0, len(fc_list)):
        total = total + float(fc_list[ele])


    additional = 5.00 + 16.38
    subtotal = float("{:.2f}".format(total)) + additional
    # + (float("{:.2f}".format(subtotal * 0.12)) / 100)
    # print(type(return_this))
    # + 5.00 + 16.38

    return "{:.2f}".format(subtotal)


def choose_account(account, rate):
    my_account = [account]
    my_rate = [rate]

    my_accounts = {my_account[0]: my_rate[0]}

    return my_accounts


def main():
    exit_program = False
    final_account_list = []
    user_rates = [0, 0, 0, 0, 0]
    rates_list = []

    # Add this later: 5.0, 16.38

    chunked_list = list()
    chunk_size = 5

    # account_listed = dict(zip(final_account_list, user_rates))
    # print(account_listed)

    new_list = []

    final_rate_list = []
    charges = {
               0: "Generation charge",
               1: "Transmission charge",
               2: "System loss charge",
               3: "Lifeline Rate subsidy",
               4: "Fit-All Renewable"
               }

    while not exit_program:
        command = input("\nEnter command: ").lower()

        if command == "A".lower():
            # ADD ACCOUNT
            new_account = input("\nAdd an account: ")
            add_account(new_account)
            final_account_list.append(', '.join(add_account(new_account)))
            
            sleep(1)           
            clear()
            print(logo.menu)
        elif command == "B".lower():
            # PRINT ACCOUNTS
            print(f"Account listed: {', '.join(final_account_list)}")
        
            sleep(2)           
            clear()
            print(logo.menu)

        elif command == "C".lower():
            # UPDATE RATES
            for items in range(0, 5):
                rates = float(input(f"\nEnter {charges[items]}: "))
                user_rates[items] = rates
            # print(user_rates + given_rates)
            new_list = print_rates(user_rates)
            rates_list += new_list

            chunked_list = list()
            chunk_size = 5
            for i in range(0, len(rates_list), chunk_size):
                chunked_list.insert(0, (rates_list[i:i + chunk_size]))
                
            sleep(1)           
            clear()
            print(logo.menu)

        elif command == "D".lower():
            if not new_list:
                print("List is empty")
            else:
                # PRINT RATES

                print((' '.join(map(str, chunked_list))))
            sleep(2)           
            clear()
            print(logo.menu)

        elif command == "E".lower():

            if not final_account_list:
                print("ERROR(2) Create an account first!")
            elif not chunked_list:
                print("ERROR(3) Update your rates first!")

            else:
                appendToList = []

                for items in range(0, len(final_account_list)):
                    print(f"∎ {final_account_list[items]}")
                choose = input("Choose account: ")
                if choose not in final_account_list:
                    print("\nERROR(4) Choose appropriate account!")
                    continue

                else:

                    print(choose, chunked_list[0])
                    appendToList += chunked_list[0]
                    # account_list_length = len(final_account_list)
                    kwh_value = float(input("\nEnter kWh: "))

                    # print(final_account_list[account_list_length-1])

                    if kwh_value <= 100:

                        for i in range(0, len(appendToList)):
                            appendToList[i] = "{:.2f}".format(appendToList[i] * kwh_value)
                            if i == 3:
                                appendToList[i] = 0
                                continue
                    elif kwh_value > 100:
                        for i in range(0, len(appendToList)):
                            appendToList[i] = "{:.2f}".format(appendToList[i] * kwh_value)

                    # FIXED CHARGES
                    if 50 <= kwh_value < 100:
                        given_rates = [-0.0001, -1.8009, 0.2228, 0.9803, 1.2908, 1.5837, 2.0941, 0.4979, 0.335]

                        for items in range(0, len(given_rates)):
                            given_rates[items] = float("{:.2f}".format(given_rates[items] * kwh_value))
                            # print(items)
                            if 4 <= items < 7:
                                given_rates[items] = 0
                                continue
                    elif 100 <= kwh_value < 300:
                        given_rates = [-0.0001, -1.8009, 0.2228, 0.9803, 1.2908, 1.5837, 2.0941, 0.4979, 0.335]

                        for items in range(0, len(given_rates)):
                            given_rates[items] = float("{:.2f}".format(given_rates[items] * kwh_value))
                            # print(items)
                            if 4 <= items < 7:
                                given_rates[items] = 0
                                continue

                    elif 300 <= kwh_value < 400:
                        given_rates = [-0.0001, -1.8009, 0.2228, 0.9803, 1.2908, 1.5837, 2.0941, 0.4979, 0.335]

                        for items in range(0, len(given_rates)):
                            given_rates[items] = float("{:.2f}".format(given_rates[items] * kwh_value))
                            # print("--------")
                            # print(kwh_value)
                            # print(float("{:.2f}".format(given_rates[items])))
                            # print("--------")

                            if items == 3:
                                given_rates[items] = 0
                            if items >= 5 and items <= 6:
                                given_rates[items] = 0
                                continue

                    elif kwh_value > 400:
                        given_rates = [-0.0001, -1.8009, 0.2228, 0.9803, 1.2908, 1.5837, 2.0941, 0.4979, 0.335]

                        for items in range(0, len(given_rates)):
                            given_rates[items] = float("{:.2f}".format(given_rates[items] * kwh_value))
                            # print(items)
                            if items == 3:
                                given_rates[items] = 0
                            if items >= 5 and items <= 6:
                                given_rates[items] = 0
                                continue
                    else:
                        print("ERROR(5) Enter appropriate kWh value!")
                        continue

                    # print(appendToList)
                    # print(given_rates)
                    # print(total_variable_charges(appendToList))
                    # print(total_fixed_charges(given_rates))

                    convert_to_float_fc = float(total_fixed_charges(given_rates))
                    convert_to_float_vc = float(total_variable_charges(appendToList))

                    total_charge = convert_to_float_fc + convert_to_float_vc
                    # 1,028.43 - 514.215
                    if kwh_value >= 0 and kwh_value <= 20:
                        lifeline_dc = 0.00
                    elif kwh_value > 20 and kwh_value <= 50:
                        lifeline_dc = -float("{:.2f}".format(total_charge)) * 0.50
                        # print(f"{lifeline_dc} sfffssfsffs")
                    elif kwh_value > 50 and kwh_value <= 70:
                        lifeline_dc = 0.00
                    elif kwh_value > 70 and kwh_value <= 100:
                        lifeline_dc = -float("{:.2f}".format(total_charge)) * 0.20
                    else:
                        lifeline_dc = 0.00

                    total_charge = convert_to_float_fc + convert_to_float_vc
                    vat = float(total_charge * 0.12)

                    consumed = (float(total_charge + (vat / 2)) + lifeline_dc)

                    if kwh_value >= 50 and kwh_value < 100:
                        if consumed < 0:
                            print("ERROR(5)")
                        else:
                            print(f'\nTOTAL WITH VAT: {"{:.2f}".format((float(total_charge + (vat / 2)) + lifeline_dc))}')
                    else:
                        if consumed < 0:
                            print("ERROR(5)")
                        else:
                            print(f'\nTOTAL WITH VAT: {"{:.2f}".format((float(total_charge + vat) + lifeline_dc))}')
                            
       
            sleep(1)           
            print(logo.menu)



        elif command == "F".lower():
            exit_program = True
            print("Ending program...")
            sleep(1)           
            clear()

        else:
            print("ERROR(1) Invalid command!")
            continue


main()
