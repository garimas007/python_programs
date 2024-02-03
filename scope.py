#bank app for cust transaction
#customers - unique id (key) and balance (value)
#process_trans - update balance based on amount


customers = {
    111 : 5000,
    222 : 10000,
    333 : 1000,
    444 : 7000
}

def process_transaction(cust_id, trans_amount):
    if cust_id not in customers:
        print("customer not found")
        return
    
    balance = customers[cust_id]
    new_balance = balance + trans_amount
    customers[cust_id] = new_balance

    print(f"customer_id : {cust_id}")
    print(f"updated balance : {new_balance}")

process_transaction(333,1000)