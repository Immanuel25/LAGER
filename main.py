import matplotlib
import os



class item:
    def __init__(self, name, stock, image, sales, price):
        self.name = name
        self.stock = stock
        self.image = image
        self.sales = sales
        self.price = price

    def add_stock(self, amount): #bisa buat kurangin juga
        self.stock += amount
    
    def transaction_item(self, amount):
        self.add_stock(-amount)
        #simpen ke transaction history beserta waktu

def clearConsole():
    os.system('cls')

clearConsole()

def search():
    global search_bar
    search_bar = input("search: ")
    current_list = []
    for obj in all_list:
        name = obj.name
        if search_bar.lower() in name.lower():
            current_list.append(obj)
    return(current_list)

def add_item():
    all_list.append( item(input('Name: '), int(input('Stock: ')), input('Image dir: '), int(input('Sales: ')), int(input('price: '))) )
    return all_list
    
all_list = []
all_list.append( item('Paku', 214, 'LAGER (inventory app)\images\paku.jpg', 0, 250) )
all_list.append( item('Dulux', 15, 'LAGER (inventory app)\images\dulux.jpg', 0, 45000) )
all_list.append( item('Impra', 32, 'LAGER (inventory app)\images\impra.jpg', 0, 90000) )
all_list.append( item('Palu', 214, 'LAGER (inventory app)\images\paku.jpg', 0, 250) )
all_list.append( item('Semen', 15, 'LAGER (inventory app)\images\dulux.jpg', 0, 45000) )
all_list.append( item('Pasir', 32, 'LAGER (inventory app)\images\impra.jpg', 0, 90000) )

all_list.sort(key=lambda x: x.name)

current_list = all_list

j=0
search_bar, is_transaction, is_inventory, is_stats = "", "", "(X)", ""


while True:
    clearConsole()
    print("""Command:
C1. Search ({})
C2. Add item

List item:""".format(search_bar))
    for i in range(6):
        if len(current_list)<=j*6+i:
            if i==0:
                print('no item')
            break
        print(str(i+1), '.', current_list[j*6+i].name, ", stock:", current_list[j*6+i].stock)
    print("""
previous << {} >> next

Tab:
T1. Inventory {}
T2. Transaction {}
T3. Stats {}""".format(j+1, is_inventory, is_transaction, is_stats))
    ans = input("click: ").lower()
    
    if ans=="c1":
        current_list = search()
        j=0
    elif ans=="c2":
        all_list = add_item()
        all_list.sort(key=lambda v: v.name)
        current_list = all_list
        search_bar = ''
    elif ans=="t1":
        is_inventory, is_transaction, is_stats = "(X)", "", ""
        print("a")
    elif ans=="t2":
        is_inventory, is_transaction, is_stats = "", "(X)", ""
        print("a")
    elif ans=="t3":
        is_inventory, is_transaction, is_stats = "", "", "(X)"
        print("a")
    elif ans=="next" or ans ==">>":
        if j<(len(current_list)-1)//6:
            j+=1
    elif ans=="previous" or ans=="<<":
        if j>0:
            j-=1
    else:
        ans = int(ans)
        clearConsole()
        print(current_list[j*6+ans-1].name)
        print("stock:", current_list[j*6+ans-1].stock)
        print(current_list[j*6+ans-1].image)
        print("sales:", current_list[j*6+ans-1].price)
        print("sales (thismonth):", current_list[j*6+ans-1].sales)
        temp = input('back: ')

