def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    # Допустимые доменные суффиксы
    suffix = [".com", ".ru", ".net"]

    # Проверка на наличие символа "@" в адресах
    if "@" not in recipient or "@" not in sender:
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)

    # Проверка на отправку самому себе
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")

    # Проверка на корректность домена у получателя
    elif not any(recipient.endswith(sub_suffix) for sub_suffix in suffix):
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)

    # Проверка на корректность домена у отправителя
    elif not any(sender.endswith(sub_suffix) for sub_suffix in suffix):
        print("Невозможно отправить письмо с адреса ", sender, "на адрес ", recipient)

    # Проверка отправителя
    elif sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса ", sender,  "на адрес ", recipient)

    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса ", sender, "на адрес ", recipient)


# Тестовые вызовы функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

