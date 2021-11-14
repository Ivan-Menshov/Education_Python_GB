def int_func(word):
    right_word = word[0].upper() + word[1:].lower()
    return right_word


user_word = str(input('Введите слово: '))
print(int_func(user_word))

user_message = str(input('Введите сообщение: ')).split()
message = ''
for i in range(len(user_message)):
    message += int_func(user_message[i])
    message += ' '
print(message[0:-1])
