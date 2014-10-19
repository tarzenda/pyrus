sales_tax_percent = 0.09

def tax_calc():
    print ("Please enter sales total.")
    sales_total = input()
    sales_tax = float(sales_total) * sales_tax_percent
    grand_total = float(sales_tax) + float(sales_total)
    print ("Sales total: ", sales_total)
    print ("Sales tax: ", sales_tax)
    print ("Grand total: ", grand_total)
