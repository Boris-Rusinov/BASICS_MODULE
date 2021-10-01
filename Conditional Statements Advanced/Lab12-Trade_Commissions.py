city = input()
sales_count = float(input())

trade_commission = 0.00
valid = ""

if city == "Sofia":
    if 0 <= sales_count <= 500:
        trade_commission = sales_count * 0.05
    elif 500 < sales_count <= 1000:
        trade_commission = sales_count * 0.07
    elif 1000 < sales_count <= 10000:
        trade_commission = sales_count * 0.08
    elif 10000 < sales_count:
        trade_commission = sales_count * 0.12
    else:
        valid = "error"
        print("error")
elif city == "Varna":
    if 0 <= sales_count <= 500:
        trade_commission = sales_count * 0.045
    elif 500 < sales_count <= 1000:
        trade_commission = sales_count * 0.075
    elif 1000 < sales_count <= 10000:
        trade_commission = sales_count * 0.10
    elif 10000 < sales_count:
        trade_commission = sales_count * 0.13
    else:
        valid = "error"
        print("error")
elif city == "Plovdiv":
    if 0 <= sales_count <= 500:
        trade_commission = sales_count * 0.055
    elif 500 < sales_count <= 1000:
        trade_commission = sales_count * 0.08
    elif 1000 < sales_count <= 10000:
        trade_commission = sales_count * 0.12
    elif 10000 < sales_count:
        trade_commission = sales_count * 0.145
    else:
        valid = "error"
        print("error")
else:
    valid = "error"
    print("error")

if sales_count >= 0 and valid != "error":
    print(f"{trade_commission:.2f}")