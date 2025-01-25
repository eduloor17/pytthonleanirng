from datetime import datetime

class Person:
    def __init__(self, name, height, birthday):
        self.name = name
        self.height = height
        self.birthday = self.parse_birthday(birthday)
    
    @staticmethod
    def parse_birthday(birthday_str):
        try:
            return datetime.strptime(birthday_str, "%m%d%Y").date()
        except ValueError:
            raise ValueError("Birthday must be in the format MMDDYYYY.")
    
    @property
    def age(self):
        today = datetime.today().date()
        age = today.year - self.birthday.year
        if (today.month, today.day) < (self.birthday.month, self.birthday.day):
            age -= 1
        return age

    @property
    def zodiac_sign(self):
        day = self.birthday.day
        month = self.birthday.month
        
        if (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Aquarius"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            return "Pisces"
        elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "Sagittarius"
        else:
            return "Capricorn"

    def show_info(self):
        print(f'\n\nYour name is {self.name}.\nYou are {self.height} ft tall.\nYou were born on {self.birthday.strftime("%m/%d/%Y")}.\nYou have completed {self.age} years.\nYour zodiac sign is {self.zodiac_sign}.\n\n')

# Input and object creation
try:
    person = Person(
        input('Type your name: '),
        input('Type your height: '),
        input('Type your birthday in the format (MMDDYYYY): ')
    )
    person.show_info()
except ValueError as e:
    print(e)