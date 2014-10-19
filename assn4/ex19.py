sales_tax_percent = 9

def tax_calc():
    print ("Please enter sales total.")
    sales_total = input()
    intSales_total = int(sales_total) * 100
    sales_tax = intSales_total * sales_tax_percent
    grand_total = float(sales_tax) / 100 + float(intSales_total)
    print ("Sales total: ", float(sales_total))
    print ("Sales tax: ", float(sales_tax) / 10000)
    print ("Grand total: ", float(grand_total) /100)
