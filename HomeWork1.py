from datetime import datetime
import random, re

def get_days_from_today(date):
    try:
        stripped_date = datetime.strptime(date, "%Y-%m-%d")
        return (datetime.today() - stripped_date).days
    except:
        return 0

def get_numbers_ticket(min, max, quantity):
    if (min >= max) or (quantity >= max-min):
        return ""
    
    out_numbers = {random.randint(min,max)}
    while len(out_numbers) < quantity:
        out_numbers.add(random.randint(min,max))
    out_list = list(out_numbers)
    out_list.sort()

    return out_list

def normalize_phone(phone_number):
    #формуємо цільний рядок з + та цифр
    match = "".join(re.findall("[0-9+]+", phone_number))
    #замінюємо всі символи до першого 0 з початку рядка на +380
    match = re.sub("^[^0]*0", "+380", match)
    return match

p_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

print("Нормалізовані номери телефонів для SMS-розсилки:", [normalize_phone(x) for x in p_numbers])
print (get_days_from_today("2025_12-25"))
print(get_numbers_ticket(1, 100, quantity=10))