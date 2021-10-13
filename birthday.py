# birthday app

from datetime import date

def print_header():
    print('-----------------------')
    print('     BIRTHDAY APP')
    print('-----------------------')
    print()


def get_birthday_from_user():
    bday_year = int(input("What year were you born [YYYY]? "))
    bday_month = int(input("What month were you born [MM]? "))
    bday_day = int(input("What day were you born [DD]? "))

    birthday = date(bday_year, bday_month, bday_day)
    return birthday
    

def compute_days_between_dates(original_date, target_date):
    this_year = date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print(f"You had your birthday {-days} days ago this year.")
    elif days > 0:
        print("Your birthday is in {days} days!")
    else:
        print("Happy Birthday!!")


def main():
    print_header()
    bday = get_birthday_from_user()
    today = date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)

main()