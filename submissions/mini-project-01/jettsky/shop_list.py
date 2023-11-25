shop_list = []
i=0
while i != -1:
    print(f"\nOptions:\
\n1. Add item to the shopping list\
\n2. View shopping list\
\n3. Remove item from the shopping list\
\n4. Quit")
    name = (int(input('Enter the number of your choice: ')))
    if name == 1:
            shop_list.append(input("Enter the item you want to add: "))
            Length = len(shop_list )
            print(shop_list [Length-1]+" has been added to your shopping list.")
    if name == 2:
            for item in shop_list :
                print(item)
    if name == 3:
            remove_list = input("Enter the item you want to remove: ")
            Length = len(shop_list)
            print(shop_list [Length -1]+" has been removed from your shopping list.")
            shop_list.remove(remove_list)
    if name == 4:
            print("Good Bye!\n")
            break
    i+=1
       

