import os,random
os.system("cls")
os.system("color 01")
print("------------Quote")


def menu():
    print("1.Motivational\n2.Funny\n3.From the movies\n4.Sarcastic")


def loading_files():
    menu()
    option_ch = input()
    option_ch = option_ch + '.txt'
    handle = open(option_ch,errors="ignore",encoding="UTF8")
    list1 = []
    for line in handle:
        list1.append(line)
    for line in  list1:
        print(list1[random.randint(0,(len(list1)-1))])
        break


again = "y"

while again == "y" or "Y":
    loading_files()
    print("Do you another one?[y/n]")
    again = input()
    if again == "n" or again == "N":
        exit(0)