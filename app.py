from peewee import *
from main import *


def menu():
    def show_contacts():
        for user in Person.select():
            print(user.first_name, user.last_name)
            print(user.phone)
            print(user.email)

    def find_contacts():
        find = input("Please type in firstname: ")
        Person.get(Person.first_name == f'{find}')
        grabbing = Person.get(Person.first_name == f'{find}')
        print(grabbing.first_name, grabbing.last_name)
        print(grabbing.phone)
        print(grabbing.email)

    def add_contacts():
        contact_name = input(f'Firstname: ')
        contact_lastname = input(f'Lastname: ')
        contact_phone = input(f'Phone number: ')
        contact_email = input(f'Email address: ')
        Person.create(first_name=f'{contact_name}', last_name=f'{contact_lastname}',
                      phone=f'{contact_phone}', email=f'{contact_email}')
        print(f"{contact_name} has been added to your contacts.")

    def update_contacts():
        update_info = input("Firstname: ")
        update_field = input(f'''Which field would you like to update:
        1. Firstname
        2. Lastname
        3. Phone
        4. Email
        Input selection: ''')
        new_value = input(f'Input new value: ')
        value_field = ""
        if update_field == '1':
            to_update = (Person.update(first_name=f'{new_value}')
                         .where((Person.first_name == f'{update_info}'))
                         .execute())
        if update_field == '2':
            to_update = (Person.update(last_name=f'{new_value}')
                         .where((Person.first_name == f'{update_info}'))
                         .execute())
        if update_field == '3':
            to_update = (Person.update(phone=f'{new_value}')
                         .where((Person.first_name == f'{update_info}'))
                         .execute())
        if update_field == '4':
            to_update = (Person.update(email=f'{new_value}')
                         .where((Person.first_name == f'{update_info}'))
                         .execute())

        print(f"{update_info}'s information has been updated.")

    def delete_contact():
        delete_data = input(
            "Input the firstname of the individual you'd like to delete: ")
        confirm = input(
            f"Are you sure you'd like to delete {delete_data}? Y/N: ")
        if confirm == 'Y' or 'y':
            to_delete = Person.get(Person.first_name == f'{delete_data}')
            to_delete.delete_instance()
            print(f'{delete_data} has been deleted.')
        else:
            menu()

    user_input = input(f'''Hello.  Please pick from the following contacts menu options:
                       1. Show all
                       2. Find using firstname
                       3. Add
                       4. Update
                       5. Delete using firstname
                       6. Exit
                       Input Selection: ''')
    if user_input == '1':
        show_contacts()
        menu()
    elif user_input == '2':
        find_contacts()
        menu()
    elif user_input == '3':
        add_contacts()
        menu()
    elif user_input == '4':
        update_contacts()
    elif user_input == '5':
        delete_contact()
    elif user_input == '6':
        exit()

    else:
        print("Please pick one of the options from the menu selection")
        menu()


menu()
