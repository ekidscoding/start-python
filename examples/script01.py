# символ # і все що праворуч від нього це - коментар, він для людей
# коментар може бути на весь рядок
print(1)  # або займати частину рядку

# зазвичай коментар пишеться перед тим, що пояснює НАПРИКЛАД

# це виклик спеціальної команди(функції)
# print(...) - зверніть увагу на дужки, вони обовʼязкові
print()  # навіть якщо в дужках нічого немає

# надрукуємо 3 найпростіші безіменні значення
print(2025)  # int
print("Python")  # str
print(True)  # bool

# друк простих значень - досить рідкісне явище. Частіше вони йдуть
# пліч-о-пліч з іменованими значеннями - змінними

name = "Python"
year = 2025
is_cool = True

# дані значення мають вказані імена, немов наліпки, стікери.
# одне й те ж значення може мати скільки завгодно імен

year_of_birth = 2010
year_of_discovery = 2010
my_favourite_language = "Python"
your_favourite_language = "Python"
is_cool = True
can_learn = True
too_boring = False

# іноді кажуть, що змінна приймає, набуває значення.
# коректніше говорити, що значенню ми даємо імʼя

print("Чарівник народився в", year_of_birth)
print("Вчений здійснив відкриття в", year_of_discovery)
print("Твоя улюблена мова програмування", your_favourite_language)
print("Моя улюблена мова програмування", my_favourite_language)



if is_cool:
    print("Python is cool")
if can_learn:
    print("Я ЗМОЖУ його вивчити!")

if not too_boring:
    print("Мені не нудно, досить весело, хоча і складно")
else:
    print("Програмувати важко, тому мені здається нудним")
