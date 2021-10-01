air_company = input()
tickets_old_count = int(input())
tickets_child_count = int(input())
net_price_ticket_old = float(input())
service_fee = float(input())

price_ticket_child = net_price_ticket_old - net_price_ticket_old * 0.70 + service_fee

net_price_ticket_old += service_fee

total_child_tickets_profit = tickets_child_count * price_ticket_child
total_old_tickets_profit = tickets_old_count * net_price_ticket_old

total_tickets_profit = total_old_tickets_profit + total_child_tickets_profit
total_company_profit = total_tickets_profit * 0.20

print(f"The profit of your agency from {air_company} tickets is {total_company_profit:.2f} lv.")