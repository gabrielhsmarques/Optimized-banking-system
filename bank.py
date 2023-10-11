
def fun_menu():
    
    menu = """
    ==========Welcome to your bank==========
    
    Menu of the options:
    
    [d]Deposit
    [w]Withdraw 
    [e]Extract
    [cu]Create user
    [ca]Create account
    [g]Get user
    [dl]Delete user
    [q]Quit
    => """
    return input(menu)


def fun_deposit(balance, value, extract):
    print("Put the desired value: ")
    value = int(input("Value:"))
    print(f"You deposited: R${value:.2f}")
    extract += f"Deposit R${value:.2f}"
    if( value <= 0):
        print("Invalid operation")
    else:
        balance += value
    return balance, extract
        
        
def fun_withdraw(balance, value, extract, limit, num_withdraw, lim_withdraw):
    if num_withdraw <= lim_withdraw:
        print("Put the desired value: ")
        value = int(input())
        print(f"You withdrew: R${value:.2f}")
        extract += f"Withdraw R${value:.2f}"
        if value > limit:
            print("Invalid operation")
        balance -= value
    num_withdraw += 1
    return balance, extract
    
    
def fun_extract(balance, extract):
    print("Extract")
    if extract == "":
        print("No move was made")
    else:
        print(f"Balance available: R${balance:.2f}")
        print(extract)
    return extract

def fun_filter(cpf, users):
    filtred_users = [user for user in users if user["cpf"] == cpf]
    return filtred_users[0] if filtred_users else None

def fun_create_user(users):
    cpf = input("Put your CPF (only numbers): ")
    user = fun_filter(cpf, users)
    
    if user:
        print("already exists user with the cpf inserted")
        return
    
    name = input("Insert the complet name:")
    date_of_birth = input("Insert your date of birth in format (dd-mm-aaaa):")
    address = input("Insert your address in format (street, number - neighborhood - city/state abbreviations ): ")
    
    users.append({"name": name, "cpf": cpf, "date_of_birth": date_of_birth, "address": address})
    
    print("User created successfully!")
    
def fun_create_account(users, agency, number_of_account, accounts):
    cpf = input("Insert cpf of the user: ")
    user = fun_filter(cpf, users)
    
    if user:
        for account in accounts:
            if number_of_account == account["number_of_account"]:
                number_of_account += 1
        print("Account created successfully!")
        return {"agency": agency, "number_of_account": number_of_account, "user": user["name"]}

    print("User not found!\nMaking of account failed!")
    
def fun_delete(users, accounts):
    cpf = input("Insert the cpf of the user delete: ")
    delete_client = fun_filter(cpf, users)
    delete_account = delete_client["name"]
    for user in accounts:
        if user.get("user") == delete_account:
            user.clear()
    delete_client.clear()
    for user in users:
        if user == {}:
            users.remove(user)
    for user in accounts:
        if user == {}:
            accounts.remove(user)
    
    return print(f"User deleted successfully!\n")


def fun_get(users, accounts):
    cpf = input("Insert cpf of the user to search for: ")
    client = fun_filter(cpf, users)
    print(f"""User founded!: 
            Name: {client["name"]}
            Cpf: {client["cpf"]}
            Date of birth: {client["date_of_birth"]}
            Address: {client["address"]}
          """)
    for user in accounts:
        if client["name"] == user["user"]:
            print(f"""User account(s): 
                    Agency: {user["agency"]}
                    Number of account: {user["number_of_account"]}
                  """)
    else:
        print("The user does not have an account!")
    


def main():
    
    balance = 0
    limit = 500
    extract = ""
    num_withdraw = 0
    LIMIT_WITHDRAW = 3
    deposit = 0
    value = 0
    users = []
    accounts = []
    AGENCY = "0001"

    while True:

        option = fun_menu()

        if option == "d":
            balance, extract = fun_deposit(balance, value, extract)
          
        elif option == "w":
            balance, extract = fun_withdraw(balance=balance, value=value, limit=limit, extract=extract, num_withdraw=num_withdraw, lim_withdraw=LIMIT_WITHDRAW)
        
        elif option == "e":
            fun_extract(balance, extract=extract)
            
        elif option == "cu":
           fun_create_user(users)
           
        elif option == "ca":
            number_of_account = len(accounts) + 1
            account = fun_create_account(users, AGENCY, number_of_account, accounts)
            
            if account:
                accounts.append(account)
            
        elif option == "dl":
            fun_delete(users, accounts)
            
        elif option == "g":
            fun_get(users, accounts)
        
        elif option == "q":
            break

        else:
            print("Invalid Operation. Please, reselect the desired operation")
if __name__ == "__main__":
    main()    
           
