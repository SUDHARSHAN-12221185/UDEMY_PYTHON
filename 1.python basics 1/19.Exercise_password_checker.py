user_name=input('what is your name: ')

password=input('what is your password: ')

password_lenght=len(password)

hidden_password="*" * password_lenght

print(f'{user_name} , your password , {hidden_password}, is {len(password)} long')
