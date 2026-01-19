def viewmenu(menu):
    for i,j in menu.items():
        print(f" {i} : {j} ")

def editmenu(menu):
    while 1:
        print("Enter 1 for adding the item.")
        print("Enter 2 for deleting the item.")
        print("Enter 3 for editing the item.")
        print("Enter 4 for Exit .")

        num=int(input("Enter the number : "))

        if (num==1):
            nt=int(input("Enter the number of items you want to add : "))
            for i in range(nt):
                item=input(f"Enter the item : ")
                price=int(input(f"Enter the price for {item}:"))
                menu[item]=price

        elif(num==2):
            nt=int(input("Enter the number of items you want to delete : "))
            for i in range(nt):
                item=input("Enter the item you want to delete : ")
                menu.pop(item,None)
            
        elif(num==3):
            nt=int(input("Enter the number of items you want to edit : "))
            for i in range(nt):
                item=input(f"Enter the item : ")
                price=int(input(f"Enter the price for {item}:"))
                if item in menu:
                    menu[item]=price
                else:
                    print("enter the valid item")

        elif(num==4):
            break
        else:
            print("Enter the valid number")           
    return menu
class order:
    def __init__(self,order_id,order_list):
        self.order_id=order_id
        self.order_list=order_list
    def view_order(self):
        print(self.order_list)
    def edit_order(self):
        ol=list(order.menu_list)
        print(self.order_list)
        while 1:
            print("Enter 1 for deleting the item.")
            print("Enter 2 for Adding the item. ")
            print("Enter 3 for editing the quantity of item. ")
            num=int(input("Enter the number: "))
            if(num==1):
                while True:
                    print("true")


orders=[]
menu = {
    "Cheeseburger": 9.99,
    "French Fries": 3.99,
    "Caesar Salad": 8.00,
    "Grilled Salmon": 19.99,
    "Soda": 2.50,
    "Coffee": 3.00
    }
x="menulist"
setattr(order,x,menu)
while 1:
    print("Enter 1 if you are an owner .")
    print("Enter 0 if you are an customer . ")

    num=int(input("Enter the number :"))

    if(num==1 or num==0):
        if(num==1):
            while 1:
                print("Enter 1 for viewing the menu .")
                print("Enter 2 for editing the menu .")
                print("Enter 3 for viewing the order .")
                num2=int(input("Enter the number :"))
                if(num2==1):
                    viewmenu(menu)
                elif(num2==2):
                    menu = editmenu(menu)
                elif(num2==3):
                    order_no=int(input("Enter the order no"))
                    orders[order_no-1].view_order()
                else:
                    print("Enter the valid number")
        
        else:
            while 1:
                print("Enter 1 for viewing the menu . ")
                print("Enter 2 for placing an order . ")
                print("Enter 3 for viewing the order . ")
                print("Enter 4 for editing the order . ")

                num=int(input("Enter the number : "))

                if(num==1):
                    viewmenu(menu)
                elif(num==2):
                    i=len(orders)
                    ol=list(menu)
                    cust_order={}
                    print("Enter -1 when you are done with your order : ")
                    while True:
                        item_no=int(input("Item no. "))
                        item_quantity=int(input("Item Quantity. "))
                        cust_order[ol[item_no-1]]=item_quantity

                        if(item_no==-1 or item_quantity==-1):
                            break
                    o=order(i+1,cust_order)
                    orders.append(o)
                elif(num==3):
                    order_no=int(input("Enter the order no"))
                    orders[order_no-1].view_order()
                elif(num==4):
                    order_no=int(input("Enter the order no you want to edit :"))
                    orders[order_no-1].view_order()
                    orders[order_no-1].edit_order()




    else:
        print("Please Enter a Valid number")