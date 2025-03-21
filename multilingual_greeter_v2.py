import multilingual_greeter
from typing import Dict

if __name__ == '__main__':
    user_mode = False
    mode_admin = False
    mode_user = False

    while not user_mode:
        user_input = input("Please select Admin or User:\n").lower()
        if user_input == 'admin':
            print("Admin Mode activated\n")
            mode_admin = True
            user_mode = True
        elif user_input == 'user':
            mode_user = True
            user_mode = True
    #handles mode selection
