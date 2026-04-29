list_of_purchase = [

]
while True:
    hub = input("add или remove или view или write: ")
    if hub == "add":
        element = list_of_purchase.append(input("что вы хотите добавить в список покупок?: "))
    elif hub == "remove":
        remove_element = input("что вы хотите удалить из списка: ")
        if remove_element in list_of_purchase:
            list_of_purchase.remove(remove_element)
        else:
            print("такого продукта нет")
    elif hub == "view":
        print(list_of_purchase)
    elif hub == "write":
        finall_list = " ".join(list_of_purchase)
        with open("list.txt", "w", encoding="utf-8") as f:
            f.write(finall_list)
        break
    else:
        print("такой команды не существует")