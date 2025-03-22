
from typing import Dict
import random

lang_dict = {
    1: 'English',
    2: 'Spanish',
    3: 'Portuguese'
}

name_prompt_dict = {
    1: 'What is your name?',
    2: '¿Cómo te llamas?',
    3: 'Qual é o seu nome?'
}

# greetings need to be changed so values are a list not a string
# then need to be able to select a random greeting from list
greetings_dict = {
    1: ['Hello', 'Hi', 'Greetings'],
    2: 'Hola',
    3: 'Olá'
}

#brought over from v1
def print_language_options(lang_options: Dict[int, str]) -> None:
    print("Please choose a language: ")
    for x, y in lang_options.items():
        print(f"{x}: {y}")

def language_input() -> int:
    user_input = input()
    return int(user_input)

def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    return lang_choice in lang_options

def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    var = name_prompt_options[lang_choice]
    print (var)

def name_input(name_prompt: str) -> str:
    user_input = input()
    return str(user_input)

#updated to choose between list options 0-3 but needs to be made for len of list
def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    x = random.randrange(0, 3)
    var = greetings_options[lang_choice][x]
    print(f"{var} " + name)

def key_input(lang_dict: Dict[int, str]) -> int:
    key = input("Enter next open key value:\n")
    while True:
        if key in lang_dict:
            key = input("Please select an open key value:\n")
        else:
            break
    return int(key)

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
            print_language_options(lang_dict)
            chosen_lang = language_input()
            while language_choice_is_valid(lang_dict, chosen_lang) is False:
                print("Unavailable, select again.")
                chosen_lang = language_input()

            select_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
            chosen_name = name_input(select_prompt)
            greet(chosen_name, greetings_dict, chosen_lang)
        #handles mode_user

        while mode_admin:
            new_key = key_input(lang_dict)
            new_lang = add_lang_input(lang_dict)
            new_name_prompt = add_name_prompt()
            new_greeting = add_greeting()
            #needs to be updated to add to a list i.e. somelist.append(new_greeting)
            lang_dict[new_key] = new_lang
            name_prompt_dict[new_key] = new_name_prompt
            greetings_dict[new_key] = new_greeting

            user_mode = False
            mode_admin = False