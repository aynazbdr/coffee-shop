from menu import show_menu
from order import add_order, show_orders
from billing import calculate_total, print_invoice

def main():
    while True:
        print("\n==========coffee shop============")
        print("1. show menu")
        print("2. add order")
        print("3. show orders")
        print("4. calculate total")
        print("5. print invoice")
        print("6. exit")

        choice= input("enter your choice: ")
        if choice=="1":
            show_menu()
        elif choice=="2":
            add_order()
        elif choice=="3":
            show_orders()
        elif choice=="4":
            total=calculate_total()
            print("total price: ", total, "toman")
        elif choice=="5":
            print_invoice()
        elif choice=="6":
            print("thank you for visiting coffee shop!")
            break
        else:
            print("invalid choice! please try again.")

if __name__=="__main__":
    main()            