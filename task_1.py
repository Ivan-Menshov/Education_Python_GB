class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_int(cls,date):
        date_list = date.split('-')
        return int(date_list[0]), int(date_list[1]), int(date_list[2])

    @staticmethod
    def validation():
        day = int(input('input day: '))
        if day not in range(1, 32):
            print('Перепроверьте число!')
        month = int(input('input month: '))
        if month not in range(1, 13):
            print('Перепроверьте месяц!')
        year = int(input('input year: '))
        if year < 0:
            print('Перепроверьте год!')


data = Date('01-05-1999')
print(data.date)
print(Date.date_to_int('01-05-1999'))
data.validation()
