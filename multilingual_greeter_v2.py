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

    while mode_user:
        multilingual_greeter.print_language_options(multilingual_greeter.lang_dict)
        chosen_lang = multilingual_greeter.language_input()
        while multilingual_greeter.language_choice_is_valid(multilingual_greeter.lang_dict, chosen_lang) is False:
            print("Unavailble, select again.")
            chosen_lang = multilingual_greeter.language_input()

        select_prompt = f"{multilingual_greeter.get_name_input(multilingual_greeter.name_prompt_dict, chosen_lang)} \n"
        chosen_name = multilingual_greeter.name_input(select_prompt)
        multilingual_greeter.greet(chosen_name, multilingual_greeter.greetings_dict, chosen_lang)
    #handles mode_user
