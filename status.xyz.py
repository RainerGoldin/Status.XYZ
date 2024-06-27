import os, time


# Display Template
def template():
    # Print a template for the UI
    print('|' + '-' * 61 + '|')
    print('|' + ' ' * 61 + '|')
    print('|{:^61}|'.format('*'))
    print('|{:^61}|'.format('*'))
    print('|{:^61}|'.format('* * *'))
    print('|{:^61}|'.format('* *   * *'))
    print('|{:^61}|'.format('* * *   +   * * *'))
    print('|{:^61}|'.format('* *   * *'))
    print('|{:^61}|'.format('* * *'))
    print('|{:^61}|'.format('*'))
    print('|{:^61}|'.format('*'))
    print('|' + ' ' * 61 + '|')
    print('|{:^61}|'.format('status.xyz'))
    print('|' + ' ' * 61 + '|')


# Mixed Display
def mixed_display(x):
    # Display a mixed template with a customizable message 'x'
    template()
    print('|{:^61}|'.format(x))
    print('|' + ' ' * 61 + '|')
    print('|' + '-' * 61 + '|')


# Public Display
def public_display(id, username):
    # Display the public page UI after logging in, showing user-specific information
    data = read_data()
    print('|{:^61}|'.format('PUBLIC PAGE'))
    print('|' + ' ' * 61 + '|')
    print('|{:^61}|'.format(f'Welcome {username}!'))
    print('|' + ' ' * 61 + '|')
    print('|{:61}|'.format(f'My status: {data[int(id)-1][3]}'))
    print('|' + ' ' * 61 + '|')
    for user_info in data:
        print('|{:61}|'.format(f'{user_info[1]}: {user_info[3]}'))
    print('|' + ' ' * 61 + '|')
    print('|' + ' ' * 61 + '|')
    print('|{:^61}|'.format('Other things you might need'))
    print('|' + ' ' * 61 + '|')
    print('|{:61}|'.format('1. Update status'))
    print('|{:61}|'.format('2. Change password'))
    print('|{:61}|'.format('3. Change username'))
    print('|{:61}|'.format('4. Log out'))
    print('|' + ' ' * 61 + '|')
    print('|' + '-' * 61 + '|')


# Read Data from Database
def read_data():
    """
    Read user data from the database file and parse it into a list of user information.
    Each user's information is represented as a list containing their ID, username, password, and status.
    Returns:
        list: A list of lists, where each inner list represents a user's information.
    """
    with open('database.txt','r') as f:
        data = []
        for line in f:
            # Split each line in the database file by '|' to extract user information
            id, username, password, status = line.strip().split('|')
            user_info = [id, username, password, status]
            data.append(user_info)
        return data


# Replace Data from Database
def replace_data(data):
    """
    Replace user data in the database file with updated data.
    Args:
        data (list): A list of lists containing user information.
    """
    with open('database.txt','w') as f:
        for user_info in data:
            # Join user information with '|' separator and write to the database file
            line = '|'.join(user_info)
            f.write(line+'\n')


# Log In
def log_in():
    # Handle user log-in process
    data = read_data()
    while True:
        os.system('cls')
        mixed_display("LOG IN")
        username = input('Enter username: ')
        if username == '/menu':
            choice_menu()
        elif not any(user_info[1] == username for user_info in data):
            print("No account with the username'{username}'!")
            time.sleep(1)
        else:
            break
    while True:
        os.system('cls')
        mixed_display("LOG IN")
        password = input('Enter password: ')
        if password == '/menu':
            choice_menu()
        elif not any(user_info[1] == username and user_info[2] == password for user_info in data):
            print('Incorrect password!')
            time.sleep(1)
        else:
            user_info = next(user_info for user_info in data if user_info[1] == username)
            id, _, _, _ = user_info
            public(id, username)


# Register
def register():
    # Handle user registration process
    data = read_data()
    while True:
        os.system('cls')
        mixed_display("REGISTER")
        print('Min. 3 char, Max. 20 char')
        username = input('Make a new username: ')
        if username == '/menu':
            choice_menu()
        elif len(username) > 20:
            print('Your username is too long! Make it shorter!')
            time.sleep(1)
            continue
        elif len(username) < 3:
            print('Your username is too short! Make it longer!')
            time.sleep(1)
            continue
        elif any(user_info[1] == username for user_info in data):
            print('Username already existed! Make a new one!')
            time.sleep(1)
            continue
        else:
            break
    while True:
        os.system('cls')
        mixed_display("REGISTER")
        print('Min. 6 char, Max. 30 char')
        password = input('Make a new password: ')
        if password == '/menu':
            choice_menu()
        elif len(password) > 20:
            print('Your password is too long! Make it shorter!')
            time.sleep(1)
            continue
        elif len(password) < 6:
            print('Your password is too short! Make it longer!')
            time.sleep(1)
            continue
        else:
            break
    while True:
        os.system('cls')
        mixed_display("REGISTER")
        print('Max. 30 char')
        status = input("Input status (Example: I'm Great!): ")
        if status == '/menu':
            choice_menu()
        elif len(status) > 30:
            print('Your status is too long! Make it shorter!')
            time.sleep(1)
            continue
        else:
            break
    id = str(int(data[-1][0]) + 1)
    f = open('database.txt','a')
    f.write(id+'|'+username+'|'+password+'|'+status+'\n')
    f.close()
    os.system('cls')
    mixed_display('ACCOUNT SUCCESSFULLY CREATED')
    while True:
        os.system('cls')
        mixed_display('Would you like to log in?')
        choice = input('y/n: ').lower()
        if choice == 'y':
            log_in()
        elif choice == 'n':
            choice_menu()
        else:
            print('Invalid option!')
            time.sleep(1)


# Public Page
def public(id, username):
    # Display the public page UI and handle user interactions after logging in
    data = read_data()
    while True:
        os.system('cls')
        template()
        public_display(id, username)
        try:
            os.system('cls')
            template()
            public_display(id, username)
            choice = int(input('Choice: '))
            if choice == 1:
                while True:
                    os.system('cls')
                    template()
                    public_display(id, username) 
                    new_status = input('Input a new status: ')
                    if len(new_status) > 30:
                        print('Your status is too long! Make it shorter!')
                        time.sleep(1)
                        continue
                    else:
                        data[int(id)-1][3] = new_status
                        replace_data(data)
                        print('Status updated!')
                        time.sleep(1)
                        return public(id, username)
            elif choice == 2:
                while True:
                    os.system('cls')
                    template()
                    public_display(id, username)
                    new_password = input('Input a new password')
                    if new_password == '/menu':
                        choice_menu()
                    elif len(new_password) > 20:
                        print('Your password is too long! Make it shorter!')
                        time.sleep(1)
                        continue
                    elif len(new_password) < 6:
                        print('Your password is too short! Make it longer!')
                        time.sleep(1)
                        continue
                    else:
                        data[int(id)-1][2] = new_password
                        replace_data(data)
                        print('Password changed!')
                        time.sleep(1)
                        return public(id, username)
            elif choice == 3:
                while True:
                    os.system('cls')
                    template()
                    public_display(id, username)
                    new_username = input('Input a new username: ')
                    if new_username == '/menu':
                        print("You can't change your username to '/menu'")
                        time.sleep(1)
                    elif len(new_username) > 20:
                        print('Your username is too long! Make it shorter!')
                        time.sleep(1)
                        continue
                    elif len(new_username) < 3:
                        print('Your username is too short! Make it longer!')
                        time.sleep(1)
                        continue
                    elif any(user_info[1] == new_username != id for user_info in data):
                        print('Username already existed! Make a new one!')
                        time.sleep(1)
                        continue
                    else:
                        data[int(id)-1][1] = new_username
                        replace_data(data)
                        print('Username changed!')
                        time.sleep(1)
                        return public(id, username)
            elif  choice == 4:
                while True:
                    os.system('cls')
                    template()
                    public_display(id, username)
                    choice = input('You sure (y/n)? ').lower()
                    if choice == 'y':
                        choice_menu()
                    elif choice == 'n':
                        return public(id, username)
                    else:
                        print('Invalid option!')
                        time.sleep(1)
            else:
                print('Invalid option! Number is out of choice!')
                time.sleep(1)
        except ValueError:
            print('Invalid option! Input a number only!')
            time.sleep(1)


# Log In or Register
def choice_menu():
    # Display the main menu and handle user choices for log-in, registration, or quitting
    while True:
        os.system('cls')
        template()
        print('|{:61}|'.format('1. Log In'))
        print('|{:61}|'.format('2. Register'))
        print('|{:61}|'.format('3. Quit'))
        print('|' + '-' * 61 + '|')
        try:
            choice = int(input('Choice: '))
            if choice == 1:
                log_in()
            elif choice == 2:
                register()
            elif choice == 3:
                quit()
            else:
                print('Invalid option! Number is out of choice!')
                time.sleep(1)
        except ValueError:
            print('Invalid option! Input a number only!')
            time.sleep(1)


# Start
if __name__ == '__main__':
    choice_menu()