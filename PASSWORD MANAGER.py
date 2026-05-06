import pyperclip
password={
    'snap':'abc@123',
    'gmail':'efg@123',
    'insta':'ghi@123',
    }
account=input('enter the account name')
if account in password:
    pyperclip.copy(password[account])
    print('password copied to cclipboard')
else:
    print('password not found')
