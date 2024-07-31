import random

password_letters_count = int(input("How many letters would you like in your password?\n"))
password_symbols_count = int(input("How many symbols would you like in your password?\n"))
password_numbers_count = int(input("How many numbers would you like in your password?\n"))

password_length = password_letters_count + password_symbols_count + password_numbers_count

password_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
password_symbols = ['~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','`','~','/','.',',']
password_numbers = range(0, 10)

symbols_count = 0
numbers_count = 0
letters_count = 0
password = ''
index = 0

generate_password_letters = []
generate_password_symbols = []
generate_password_numbers = []
while index < password_length:
    # 0 代表数字, 1表示符号, 2表示字母
    random_type = random.randint(0, 2)
    if random_type == 0:
        if numbers_count < password_symbols_count:
            numbers_count += 1
            temp = str(password_numbers[random.randint(0, len(password_numbers) - 1)])
            generate_password_numbers.append(temp)
            password += temp
        else:
            continue
    elif random_type == 1:
        if symbols_count < password_numbers_count:
            symbols_count += 1
            temp = str(password_symbols[random.randint(0, len(password_symbols) - 1)])
            generate_password_symbols.append(temp)
            password += temp
        else:
            continue
    elif random_type == 2:
        if letters_count < password_letters_count:
            letters_count += 1
            # 0 代表大写，1代表小写
            upper_lower = random.randint(0, 1)
            which = random.randint(0,25)
            temp = password_letters[which].upper() if upper_lower == 0 else password_letters[which]
            generate_password_letters.append(temp)
            password += temp
        else:
            continue
    index += 1

print(f"Your password is {password}, the length is {len(password)}\n")
print(f"letters: {generate_password_letters}\nsymbols: {generate_password_symbols}\nnumbers: {generate_password_numbers}")