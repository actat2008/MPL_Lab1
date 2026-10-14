initialBalance = 1000

transactions = [
    {"type": "deposit",  "amount": 500},
    {"type": "withdraw", "amount": 200},
    {"type": "deposit",  "amount": -50},   
    {"type": "withdraw", "amount": 2000},   
    {"type": "deposit",  "amount": 300},
    {"type": "withdraw", "amount": 150},
    {"type": "deposit",  "amount": 0},      
    {"type": "withdraw", "amount": 400},
    {"type": "deposit",  "amount": 250},
]

balance = initialBalance

rejected = 0

for i in transactions:
    amount = i["amount"]
    if amount <= 0:
        rejected += 1
        print("Rejected " + i["type"] + " of " + str(amount) ,  "Invalid amount.")
    elif i["type"] == "deposit":
        balance += amount
        print("Deposit " + str(amount), "Balance " + str(balance))
    elif i["type"] == "withdraw":
        if amount > balance:
            rejected += 1
            print("Rejejcted withdraw of " + str(amount) , "Balance is only " + str(balance))
        else:
            balance -= amount
            print("withdraw " + str(amount) , "Balance " + str(balance))


print("Final balance : " + str(balance))
print("Num of rejected operantions : " + str(rejected))
