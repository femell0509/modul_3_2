# Способы вызова ф-ии. Задача на письма e-mail

def send_email(message, recipient, sender='university.help@gmail.com'):
    if ('@' in recipient and '@' in sender and
            '.com' == recipient[-4:] or '.net' == recipient[-4:] or '.ru' == recipient[-3:] and
            '.com' == sender[-4:] or '.net' == sender[-4:] or '.ru' == sender[-3:]):
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        elif sender != 'university.help@gmail.com':
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!Письмо успешно отправлено с адреса {sender} на адрес {recipient}. ')
    else: print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

message_ = str(input('Ведите сообщение, которое хотите передать: '))
recipient_ = str(input('Введите адрес получателя: '))
sender_question = str(input('Вы хотите поменять адрес отправителя?: '))
if sender_question == 'да' or sender_question == 'Да' or sender_question == 'Yes':
    sender_ = str(input('Введите адрес отправителя: '))
    send_email(message_, recipient_, sender_)
else: send_email(message_, recipient_)
