def finding_by_number(list, query):
    for s in list:

        s_founder = True

        if query == s:
            print("The number", s, " is for :", list[s])
            s_founder = True
            break
        else:
            s_founder = False

    if s_founder == False:
        print('Sorry, the name of this number not found !!')

def finding_by_name(list, name):

    for s in list:

        s_founder = True

        if name == list[s]:
            print("The name", list[s], "his/her number is :", s)
            s_founder = True
            break
        else:
            s_founder = False

    if s_founder == False:
        print('Sorry, the name not found !!')


def adding_new_user(list,num,name):

    new_key_value_insert = {num:name}
    list.update(new_key_value_insert)
    print(list)



phone_numbers = {1111111111:'Amal', 2222222222:'Mohammed', 3333333333:'Khadijah', 4444444444:'Abdullah', 5555555555:'Rawan',6666666666:'Faisal',7777777777:'Layla'}

program = 1

while program == 1:

    chooise = int(input('\n\n\nWelcome to the phones numbers evidance ! \nEnter 1 for queries by number\nEnter 2 for queries by name\nEnter 3 for adding a new user\nEnter 4 to end the program\nYour choise is >>>'))

    if chooise == 1:

        checker = 1

        while checker == 1:

            query = int(input('Enter the number to see the name: '))
            if query < 1111111111 or query > 9999999999:
                print('This is invalid number ! please try again\n\n')
            else:
                checker +=1
        finding_by_number(phone_numbers, query)

    elif chooise == 2:

        name = str(input('Enter a name: '))
        finding_by_name(phone_numbers, name)

    elif chooise == 3:

        num = int(input('Enter new number: '))
        name = str(input('Enter new name: '))
        adding_new_user(phone_numbers,num,name)
        print(phone_numbers.keys(), "\n" , phone_numbers.values())

    elif chooise == 4:
        print("\n\n\n\n\nGood bye !!!\n\n")
        program += 1

    else:

        print('\n\nInvalid number please try again !!\n\n')
