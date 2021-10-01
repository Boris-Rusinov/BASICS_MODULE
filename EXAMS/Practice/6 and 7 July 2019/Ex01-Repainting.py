needed_nylon = int(input())  # 1.50 per square meter
needed_paint = int(input())  # 14.50 per litre
needed_diluent = int(input())  # 5.00 per litre
hours_to_accomplish_task = int(input())  # 30% of total price for materials is the hourly fee for workers

total_expenses_materials = 0.00
total_expenses = 0.00


total_nylon_fee = (needed_nylon + 2) * 1.50
total_paint_fee = (needed_paint + needed_paint * 0.1) * 14.50
total_diluent_fee = needed_diluent * 5.00

total_expenses_materials = total_nylon_fee + total_paint_fee + total_diluent_fee + 0.40

total_workers_fee = total_expenses_materials * 0.30 * hours_to_accomplish_task

total_expenses += (total_expenses_materials + total_workers_fee)

print(f"Total expenses: {total_expenses:.2f} lv.")
