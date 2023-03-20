# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []

def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else: 
        print("Empty Data\n")

def iSexist(str):
    for i in all_data:
        if i == str:
            return True
    return False
    
def add_new_contact():
    global last_id
    array = ["surname", "name", "patronym", "phone_number"]    #template
    string = ""
    for i in array:
        string += input(f"Enter {i} ") + " "
    if iSexist(string) == False:
        last_id += 1

        with open(file_base, "a", encoding="utf-8") as f:
            f.write(f"{last_id} {string}\n")
    else:
        print("Already in Base")

def search_contact():
    searched = input("Введите что-то для поиска по справочнику:")
    searched = searched.split()
    found = False
    for i in searched:
        for j in all_data:
            if i in j: 
                print("Search Result: ", j)
                found = True
    if found:
        print("That's all we found\n")
    else: 
        print("Not found, try again? press 3")

def change_contact():
    show_all()
    modID = int(input("Введите ID контакта для редактирования:"))
    global last_id, all_data
    if modID <= last_id:
        with open(file_base, 'w', encoding="utf-8") as f:
            f.write("")
        for i in all_data:
            j = int(i.split()[0])
            if j == modID:
                changes = i.split()
                answer = input("Что хотите изменить:\n"
                       "1. Фамилия\n"
                       "2. Имя\n"
                       "3. Отчество\n"
                       "4. Телефон\n"
                       "5. Exit\n")
                match answer:
                    case "1":
                        changes[1] = input("Введите новую фамилию:\n")
                    case "2":
                        changes[2] = input("Введите новое имя:\n")
                    case "3":
                        changes[3] = input("Введите новое отчество:\n")
                    case "4":
                        changes[4] = input("Введите новый телефон:\n")
                    case "5":
                        return
                    case _:
                        print("Try again!\n") 
    changes = " ".join(changes)
 ####
    for i in all_data:
            j = int(i.split()[0])
            if j == modID:
                with open(file_base, "a", encoding="utf-8") as f:
                    f.write(f"{changes} \n")
            else:
                with open(file_base, "a", encoding="utf-8") as f:
                    f.write(f"{i} \n")

def del_contact():
    global all_data

    symbol = "\n" ### вставить в конструкцию ниже нельзя без переменной
    show_all()
    delId = int(input("Введите id записи для удаления: "))
    with open(file_base, 'w', encoding="utf-8") as f:
        f.write("")
    for i in all_data:
            j = int(i.split()[0])
            with open(file_base, 'a', encoding="utf-8") as f:
                if j != delId:
                    f.write(f'{i}\n')
    print("Record deleted!\n")
    
def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book menu:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change a record\n"
                       "5. Delete\n"
                       "6. Export/Import\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                change_contact()
            case "5":
                del_contact()
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")

main_menu()
            