menu={"coffee":80000 ,"tea":50000,"cake":120000}

def show_menu():
    print("\n=========cafe menu=========")
    for product, price in menu.items():
        print(product , ":" , price , "toman")

if __name__=="__main__":
    show_menu() 