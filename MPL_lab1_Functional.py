from functools import reduce

initialBalance = 1000  # AZN

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


def is_valid(tx, balance):
    if tx["amount"] <= 0:
        return False
    return tx["type"] == "deposit" or tx["amount"] <= balance


def step(state, tx):
    balance, accepted = state
    if not is_valid(tx, balance):
        return state
    delta = tx["amount"] if tx["type"] == "deposit" else -tx["amount"]
    return (balance + delta, accepted + (tx,))

_, accepted = reduce(step, transactions, (initialBalance, ()))

deposits = list(filter(lambda t: t["type"] == "deposit", accepted))
withdrawals = list(filter(lambda t: t["type"] == "withdraw", accepted))


deposit_amounts = list(map(lambda t: t["amount"], deposits))
withdraw_amounts = list(map(lambda t: t["amount"], withdrawals))


total_deposited = reduce(lambda a, b: a + b, deposit_amounts, 0)
total_withdrawn = reduce(lambda a, b: a + b, withdraw_amounts, 0)

final_balance = initialBalance + total_deposited - total_withdrawn
rejected = len(transactions) - len(accepted)

print("Valid deposit amounts:   ", deposit_amounts)
print("Valid withdrawal amounts:", withdraw_amounts)
print(f"Total deposited: {total_deposited} AZN")
print(f"Total withdrawn: {total_withdrawn} AZN")
print(f"Final balance:   {final_balance} AZN")
print(f"Rejected transactions: {rejected}")
