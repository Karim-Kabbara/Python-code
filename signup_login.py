username = input("create a username:")
password = input('Enter your password here : ')
print('\n')

from re import *

lower_match = compile(r'[a-z]').findall(password)  # Finding if the password contains lowecase letters.
upper_match = compile(r'[A-Z]').findall(password)  # Finding if the password contains uppercase letters.
symbol_match = compile(r'[|\"|\'|~|!|@|#|$|%|^|&|*|(|)|_|=|+|\||,|.|/|?|:|;|[|]|{\}|<|>]').findall(
    password)  # Finding if the password contains special characters.
number_match = compile(r'[0-9]').findall(password)  # Finding if the password contains numbers.

if len(password) < 8 or len(lower_match) == 0 or len(upper_match) == 0 or len(symbol_match) == 0 or len(
    number_match) == 0:
    print('Your password is weak ! ')

elif len(password) >= 8:
    print('Your password is strong ! ')

elif len(password) >= 16:
    print('Your password is very strong ! ')
print("ok your username is:\n", username,"\n your password is:\n", password)
username_login = input("type your username:")
if username_login == username:
    password_login = input("type your password:")
    if password_login == password:
        print("Welcome,", username, "!")