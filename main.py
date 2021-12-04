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
    print(all_list)
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
search_bar = ""

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
previous <<   >> next

Tab:
T1. Inventory
T2. Transaction
T3. Stats""")
    ans = input("click: ").lower()
    
    if ans=="c1":
        current_list = search()
        j=0
    elif ans=="c2":
        all_list = add_item()
        all_list.sort(key=lambda x: x.name)
        current_list.sort(key=lambda x: x.name)
        search_bar = ''
    elif ans=="t1":
        print("a")
    elif ans=="t2":
        print("a")
    elif ans=="t3":
        print("a")
    elif ans=="next" or ">>":
        j+=1
    elif ans=="previous" or "<<":
        j-=1
    else:
        x = i+int(ans)-1
