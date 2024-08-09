def username_password_operations():
    passwd = {'rahul': 'genius', 'kumar': 'smart', 'ankita': 'intelligent'}

    def print_items():
        print(passwd.items())

    def print_keys():
        print(passwd.keys())

    def print_values():
        print(passwd.values())

    def get_password(user):
        return passwd.get(user, 'User not found')

    def change_password(user, new_password):
        passwd[user] = new_password

    print_items()
    print_keys()
    print_values()
    user = input("Enter username to get password: ")
    print(get_password(user))
    user = input("Enter username to change password: ")
    new_password = input("Enter new password: ")
    change_password(user, new_password)
    print_items()

username_password_operations()
