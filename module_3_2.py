def send_mail(message, recipient, *, sender='university.help@gmail.com'):
    cor_ = False
    mail = ('.com', '.ru', '.net')

    for i in recipient:
        if recipient.endswith(mail):
            if i == '@':
                cor_ = True
                break
            else:
                cor_ = False
        else:
            cor_ = False

    for i in sender:
        if sender.endswith(mail):
            if i == '@':
                cor_ = True
                break
            else:
                cor_ = False
        else:
            cor_ = False

    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif not cor_:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_mail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_mail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

