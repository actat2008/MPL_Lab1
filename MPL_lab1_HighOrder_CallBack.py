def withdraw(balance, amount, on_success, on_error):
    if amount <= 0:
        on_error("Must be higher than 0 !")
    elif amount > balance:
        on_error("Not enough money on your balance !")
    else:
        new_balance = balance - amount
        on_success(new_balance)


def success_message(new_balance):
    print("Success!")
    print("New balance :", new_balance, "AZN")


def error_message(message):
    print("Error:", message)



withdraw(1000, 200, success_message, error_message)


withdraw(1000, 1200, success_message, error_message)


withdraw(
    1000,
    300,
    lambda new_balance: print("New balance :", new_balance, "AZN"),
    lambda message: print("Error :", message)
)

withdraw(
    500,
    700,
    lambda new_balance: print("New balance :", new_balance, "AZN"),
    lambda message: print("Error :", message)
)
