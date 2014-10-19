def calc_bill():
   print("Enter sales total")
   sales_total = float(input())
   sales_tax = sales_total * 0.09
   grand_total = sales_total+sales_tax
   print("Sales total: " + str(sales_total))
   print("Sales tax:   " + str(sales_tax))
   print("Grand total: " + str(grand_total))

calc_bill()
