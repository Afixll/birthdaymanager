from pyfiles.birthday import birthday
import pandas as pd

class birthdaysmanager:
    path = None
    birthdays = pd.DataFrame({"Name":[], "Date":[], "Days left":[], "Dev_Daysleft":[]})

    def __init__(self, path: str):
        self.path = path

        try:
            f = open(path, "x")
            f.close()
            f = open(path, "r")
        except:
            f = open(path, "r")

        rows = f.readlines()
        for row in rows:
            if(row != '\n'):
                info = row.split(',')
                bd = birthday(info[0], int(info[1]), int(info[2]), int(info[3].split('\n')[0]))

                days_left_text = None
                if(bd.days_left_alternative == None):
                    days_left_text = str(bd.days_left)
                else:
                    days_left_text = f"bd.days_left/bd.days_left_alternative"

                list = [bd.name, bd.date.strftime("%d/%m/%y"), days_left_text, bd.days_left]
                self.birthdays.loc[len(self.birthdays)] = list

        f.close()

    def __str__(self) -> str:
        if(self.birthdays.empty):
            return "No birthdays have been added yet"
        else:
            return self.birthdays.to_string(columns=["Name", "Date", "Days left"], col_space=[10,10,10], justify="center")

    def add_bd(self, name: str, day: int, month: int, year=2039):
        with open(self.path, "a") as f:
            f.write(f"{name},{day},{month},{year}\n")

    def rm_bd(self, index: int):
        lines = None
        with open(self.path, 'r') as f:
            lines = f.readlines()

        with open(self.path, 'w') as f:
            i = 0
            for line in lines:
                if(i != index):
                    f.write(line)
                    print("Y")
                print(i)
                i = i +1

    def get_next(self):
        next_birthdays = self.birthdays[self.birthdays["Dev_Daysleft"] <= 30].sort_values(["Dev_Daysleft"])
        if(next_birthdays.empty):
            return "No birthdays within the next 30 days"
        else:
            return next_birthdays.to_string(columns=["Name", "Date", "Days left"], col_space=[10,10,10], justify="center")

