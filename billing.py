from order import orders
def calculate_total():
    total=0
    for order in orders:
        total +=order["price"]*order["quantity"]
    return total

def calculate_discount(total):
    if total>1000000:
        discount=total*0.10
    else:
        discount=0
    return discount

def print_invoice():
    if len(orders)==0:
        print("no orders registered!")
        return
    total= calculate_total()
    discount=calculate_discount(total)
    final_price=total-discount
    print("\n=========invoice==========")
    for order in orders:
        print("product" , order["product"])
        print("price:" , order["price"])
        print("quantity" , order["quantity"])
        print("----------------------")
    print("total:" , total, "toman")
    print("discount:" , discount, "toman")
    print("final price:" , final_price, "toman")

if __name__=="__main__":
    print_invoice()