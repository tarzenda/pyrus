sales_tax_percent = 9

def tax_calc():
    print ("Please enter sales total.")
    sales_total_float = float(input())

    # calculate results in pennies...
    sales_total = int(sales_total_float * 100.0)
    sales_tax = sales_total * sales_tax_percent
    grand_total = sales_total + sales_tax

    # print results in floating...
    print ("Sales total: ", sales_total/100.0)
    print ("Sales tax: ", sales_tax/100.0)
    print ("Grand total: ", grand_total/100.0)

