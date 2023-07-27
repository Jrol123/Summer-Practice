"""
D. СМС-рассылка
"""


class Person:

    def __init__(self, first_name: str, last_name: str, patronymic: str, phone_book: dict):
        """
        Класс работника компании.

        :param first_name: Имя.
        :type first_name: str
        :param last_name: Фамилия.
        :type last_name: str
        :param patronymic: Отчество.
        :type patronymic: str
        :param phone_book: Номера телефонов сотрудника.
        :type phone_book: dict

        """
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.phone_book = phone_book

    def get_phone(self, keyword: str = "private") -> str | None:
        """
        Получение номера телефона.

        По-умолчанию выдаёт частный номер телефона.

        :param keyword: ключевое слово.
        :return: Номер телефона
        :rtype: str | None

        """
        # Как правильно оформить except?
        return self.phone_book.get(keyword, None)  # Второй аргумент кастомный.

    def get_work_phone(self) -> str | None:
        """
        Получение рабочего номера телефона.

        :param keyword: ключевое слово.
        :return: Номер телефона
        :rtype: str | None
        :except None: Если нет номера телефона.

        """
        return self.get_phone("work")

    def get_name(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

    def get_sms_text(self):
        return f'Уважаемый {self.first_name} {self.patronymic}! \n' \
               f'Примите участие в нашем беспроигрышном конкурсе для физических лиц.'


class Company:
    def __init__(self, name: str, type: str, phone_book: dict, *staff: Person):
        self.name = name
        self.type = type
        self.phone_book = phone_book
        self.staff = list(staff)

    def get_phone(self, keyword: str = "contact") -> str | None:
        """
        Получение номера телефона.

        По-умолчанию выдаёт номер телефона компании.

        :param keyword: ключевое слово.
        :return: Номер телефона
        :rtype: str | None
        :except None: Если нет номера телефона.

        """
        try:
            return self.phone_book[keyword]
        except:
            for person in self.staff:
                phone = person.get_work_phone()
                if phone is not None:
                    return phone
            return None

    def get_name(self) -> str:
        return self.name

    def get_sms_text(self) -> str:
        return f'Для компании {self.name} есть супер предложение!\n' \
               f'Примите участие в нашем беспроигрышном конкурсе для {self.type}.'


def send_sms(*args: Person | Company) -> None:
    for entity in args:
        print()
        if entity.get_phone():
            print(f'«Отправлено СМС на номер {entity.get_phone()}; с текстом:\n{entity.get_sms_text()}')
        else:
            print(f'«Не удалось отправить сообщение абоненту:\n{entity.get_name()}.')
