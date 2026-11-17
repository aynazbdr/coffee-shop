from menu import menu
orders=[]

def add_order():
    product=input("enter product name: ").lower()
    if product in menu:
       quantity= int(input("enter quantity: "))

       if quantity>0:
         order={
           "product":product,
           "price":menu[product],
           "quantity":quantity
         }

         orders.append(order)
         print("order added successfully!")

       else:
         print("quantity must be positive!")
    else:
       print("product not found!")
def show_orders():
    if len(orders)==0:
       print("no orderss registered!")            
    else:
         print("\n==========your orders==========")


         for order in orders:
            print("product:", order["product"])
            print("price:" , order["price"])
            print("quantity" , order["quantity"])
            print("-------------------")
if __name__=="__main__":
   add_order()
   show_orders()            