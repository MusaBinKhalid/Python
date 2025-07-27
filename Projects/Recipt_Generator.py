item_dict= {}
total_price = 0

choice = input("Press A to ADD item or Press R for RECIPT: ")

if choice.lower() == 'a':

    while(True):

            item = input("Enter Item: ")
            price = int(input("Enter Price: "))

            total_price = total_price + price
            item_dict[item] = price

            choice = input("Press A to ADD item or Press R for RECIPT: ")

            if choice.lower() == 'r':
                
                print("\nItem                 Price")
                print("-" * 30)

                for item, price in item_dict.items():
                    print(f"{item:<10}           {price:<5}")

                print("-" * 30)
                print(f"Total |              {total_price}")
                print(f"Your total Bill is {total_price}. Thank You for Shopping!")
                break

            elif choice.lower() == 'a':
                continue

            else:
                print("Enter Valid Choice!")

elif choice.lower() == 'r':
    print("No item was Bought!")

else:
    print("Enter Valid Choice!")