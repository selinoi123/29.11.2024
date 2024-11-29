import random

#START Question 1
num1 = [x for x in range(95, 106)] #a
print(num1)

num2 = [x for x in range(10, 20 + 1, 2)] #b
print(num2)

num3 = [random.choice([False, True]) for _ in range(5)] #c
print(num3)

num4 = [random.randint(1, 100) for _ in range(10)] #d
print(num4)

num5 = [random.randint(50, 100) for _ in range(10)] #e
print(num5)

num6 = [num for num in [random.randint(1, 100) for _ in range(10)] if num > 50] #f
print(num6)

num7: str = str(input("Enter strings: "))  #g   masters python hello
str_1= [x for x in num7 if x != 't' and x != ' ']
print(str_1)

num8 = [random.randint(10, 99) for _ in range(10)] #h
print(num8)

num8_2 = [num % 10 for num in num8]
print(num8_2)
#END

#START Question 2
#a כדי לתפוס את השגיאה ולטפל בה בצורה מבוקרת, מבלי שהקוד יפסיק לעבוד.
#b זה יכול לתת לקוד את האפשרות להמשיך לעבוד גם אם התרחשה שגיאה. זה עוזר למנוע קריסת תוכניות בשל שגיאות לא צפויות

try:
    result = 88 / 0
except ZeroDivisionError:
    print(f"Error: Cannot divide by zero!") #c

try:
    raise ValueError("This is a custom error!") #d
except ValueError:
    print(f"Error")

array_num: list[int] = [12, 57, 73, 49]

while True:
    try:
        number: int = int(input("Enter an index: "))
        if number == -999:
            break
        print(f"The number at index {number} is {array_num[number]}")
    except ValueError:
        print("Error: Please enter a valid number.")
    except IndexError:
        print("Error: Index out of range. Please enter an index between 0 and 3.") #e
#END

