import multilingual_greeter
from typing import Dict

#New features

def key_input(lang_dict: Dict[int, str]) -> int:
    key = input("Enter next open key value:\n")
    while True:
        if key in lang_dict:
            key = input("Please select an open key value:\n")
        else:
            break
    return key

def add_lang_input(lang_dict: Dict[int, str]) -> str:
    lang = input("Please enter desired language to add:\n")
    while True:
        if lang in lang_dict.values():
            lang = input("Language already in dictionary, please review selection:\n")
        else:
            break
    return lang

def add_name_prompt() -> str:
    return input("Enter prompt for name in language:\n")

def add_greeting() -> str:
    return  input("Enter greeting for language:\n")


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

        while mode_admin:
            new_key = key_input(multilingual_greeter.lang_dict)
            new_lang = add_lang_input(multilingual_greeter.lang_dict)
            new_name_prompt = add_name_prompt()
            new_greeting = add_greeting()
            multilingual_greeter.lang_dict[new_key] = new_lang
            multilingual_greeter.name_prompt_dict[new_key] = new_name_prompt
            multilingual_greeter.greetings_dict[new_key] = new_greeting

            user_mode = False
            mode_admin = False
            break
            #need a way to restart with added languages
        #handles mode_admin