import datetime as dt

class birthday:
    name = None
    date = None
    days_left = None
    days_left_alternative = None

    def __init__(self, name: str, day: int, month: int, year: int):
        self.name = name
        self.date = dt.date(year, month, day)

        # Calculate days left till birthday
        c_date = dt.date.today()
        rel_date = None
        match (day == 29 and month == 2):
            case False:
                match size_relation(c_date.month, month):
                    case -1:
                        rel_date = dt.date(c_date.year, month, day)
                        self.days_left = calc_daysleft(c_date, rel_date)
                        return
                    case 1:
                        rel_date = dt.date(c_date.year + 1, month, day)
                        self.days_left = calc_daysleft(c_date, rel_date)
                        return
                    case 0:
                        match c_date.day > day:
                            case False:
                                self.days_left = day - c_date.day
                                return
                            case True:
                                rel_date = dt.date(c_date.year + 1, month, day)
                                self.days_left = calc_daysleft(c_date, rel_date)
                                return

            case True: # A whole case for people born on a leap-day
                match size_relation(c_date.month, 2):
                    case -1:
                        if(c_date.year % 4 != 0):
                            rel_date = dt.date(c_date.year, 2, 28)
                            self.days_left = calc_daysleft(c_date, rel_date)
                            self.days_left_alternative = self.days_left + 1
                            return
                        else:
                            rel_date = dt.date(c_date.year, 2, 29)
                            self.days_left = calc_daysleft(c_date, rel_date)
                            return
                    case 1:
                        if((c_date.year + 1) % 4 != 0):
                            rel_date = dt.date(c_date.year + 1, 2, 28)
                            self.days_left = calc_daysleft(c_date, rel_date)
                            self.days_left_alternative = self.days_left + 1
                            return
                        else:
                            rel_date = dt.date(c_date.year + 1, 2, 29)
                            self.days_left = calc_daysleft(c_date, rel_date)
                            return
                    case 0:
                        match size_relation(c_date.day, day):
                            case -1:
                                if(c_date.year % 4 != 0):
                                    self.days_left = 28 - c_date.days
                                    self.days_left_alternative = self.days_left + 1
                                    return
                                else:
                                    self.days_left = 29 - c_date.days
                                    return
                            case 1:
                                if((c_date.year + 1) % 4 != 0):
                                    rel_date = dt.date(c_date.year + 1, 2, 28)
                                    self.days_left = calc_daysleft(c_date, rel_date)
                                    self.days_left_alternative = self.days_left + 1
                                    return
                                else:
                                    rel_date = dt.date(c_date.year + 1, 2, 29)
                                    return
                            case 0:
                                self.days_left = 0
                                return

    def __str__(self):
        return f"{self.name}  {str(self.date)}   {self.days_left}"

def size_relation(n1, n2):
    if(n1 > n2):
        return 1
    if(n1 < n2):
        return -1
    return 0

def calc_daysleft(c_date, rel_date):
    return (rel_date - c_date).days
