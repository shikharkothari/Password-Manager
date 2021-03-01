'''
This app is created by SHIKHAR KOTHARI - NEOS. CLI - Command Line Interface.
This app allows you to generate and mange your passwords safe.
this app will use encryption techniques to keep your passwords safe.
'''
import random
import datetime
import os

a = '\033[95m'#purple
b = '\033[94m'#indigo
c = '\033[96m'#blue
d = '\033[92m'#green
e = '\033[93m'#yellow
f = '\033[91m'#red
g = '\033[0m'#end
h = '\033[1m'#bold
u = '\033[4m'#underline


def encryptor(message):
    '''This function takes original passwords as an
    input and encrypts it using caesar cypher.
    Here we are shifting letters to 5 position to right.
    A-->F'''

    alphabet1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmonpqrstuvwxyz1234567890!@#$%^&*/?\|+_-= .,:;<>"
    encrypt = ''
    for i in message:
        position = alphabet1.find(i)
        newposition = (position + 5) % 85
        encrypt += alphabet1[newposition]
    return encrypt

def decryptor(message):
    '''This function takes encrypted passwords as an
    input and decrypts it using caesar cypher.
    Here we are shifting letters to 5 position to left.
    F-->A'''

    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmonpqrstuvwxyz1234567890!@#$%^&*/?\|+_-= .,:;<>"
    decrypt = ''
    for i in message:
        pos = alphabet2.find(i)
        newpos = (pos - 5) % 85
        decrypt += alphabet2[newpos]
    return decrypt

def password_genrator(pass_len):
     '''This function generates the password randomly on the basis of length of characters given.'''
     try:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*/?\|+_-='
        password = "".join(random.sample(alphabet, pass_len))
        return password
     except Exception as error:
         print(f'{f}{error}{g}\n')

def delete_password(line_no):
    '''This function deletes specific line of password data. Given <-- line number'''
    file = open('passwords.txt', 'r')
    lines = file.readlines()
    file.close()
    newfile = open('passwords.txt', 'w')
    line_number = 0
    for i in lines:
        line_number += 1
        if line_number != int(line_no):
            newfile.write(i)
    newfile.close()

def save_password(account):
    f = open("passwords.txt", "a")
    f.write(encryptor(f"{account} - {datetime.datetime.today()} -> {password}"))
    f.write("\n")
    f.close()

def show_password():
    pass_file = open("passwords.txt", "r")
    print("\nYour password's list looks like this")
    for i in pass_file:
        decrypted_message = decryptor(i)
        print(f'{c}{decrypted_message}{g}')
    pass_file.close()

os.system('cls')# This let work the ascii colours work properly
print(f'{a}{h}Press:\nG - Generate Password\nA - Access Password\nQ - Quit\n--help - Help{g}')

while True:
    home = str(input('\nG/A/Q :')).upper()
    if home == 'G':
        password_length = int(input("No. of characters you want in password.(Integer):"))
        while True:
            password = password_genrator(password_length)
            os.system('cls')
            verifying_password = str(input(f'{e}{password}{g},'
                                           f'{a}Y - Save password, Enter - Genrate again, H - To go to home.{g}')).upper()

            if verifying_password == 'Y':
                account_name = input("Enter the account name:")
                save_password(account_name)
                break

            elif verifying_password == '':
                continue

            elif verifying_password == 'H':
                break

            else:
                print("Enter Valid Key")
                break

    elif home == 'A':#Accessed
        authen = str(input('Enter the password:'))
        if authen == 'shikhar24042006':
            show_password()
            ask = str(input("\nPress 'H' - home, 'Q' - Quit, 'D' - Delete password :")).upper()

            if ask == 'H': continue

            elif ask == 'D':
                del_line_no = input('Enter the number of the password line you want to delete.')

                try: del_line_no = int(del_line_no)

                except Exception as error: print(f'{f}{error}{g}')

                else:
                    ask_to_del = str(input(f'{f}WARNING:Are you sure you want to delete line no. '
                                           f'{del_line_no}.\nYes/No?{g}')).lower()

                    if ask_to_del == 'y' or ask_to_del == 'yes':
                        delete_password(del_line_no)
                        show_password()

                    elif ask_to_del == 'n' or ask_to_del == 'no': continue

                    else: continue


            elif ask == 'Q': quit()

            else: print(f'{f}Enter valid key.{g}')

    elif home == 'Q': quit()

    elif home == '--HELP': print(f'{a}\nPress:\nG - Genrate Password\nA - Access Password\nQ - Quit\n--help - Help{g}')

    else: print(f'{f}Enter valid key{g}')