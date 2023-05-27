'''try:
    print('start code')
    print(error)
    print('No errors')

except:
    print('We hae an error')

print('Code after capsule')'''

'''try:
    print(error)

except NameError:
    print('u have NameError')

try:
    print(10/0)
except ZeroDivisionError:
    print('ZeroDivisionError')'''

'''#ValueError
#ZeroDivisionError
try:
    a = int(input('first number'))
    b = int(input('second number'))
    c = a / b
    print(c)
except ValueError:
    print('not have correct value')
except ZeroDivisionError:
    print('U can not divide by zero')
'''

def solve (a, b, c):
    if str(b) == '+':

        try:
            print(float(a) + float(c))
        except ValueError:
            print('одно из значений не число')
    elif str(b) == '*':
        try:
            print(float(a) * float(c))
        except ValueError:
            print('одно из значений не число')
    elif str(b) == '-':
        try:
            print(float(a) - float(c))
        except ValueError:
            print('одно из значений не число')
    elif str(b) == '/':
        try:
            print(float(a) / float(c))
        except ZeroDivisionError:
            print('Нельзя делить на ноль')
        except ValueError:
            print('одно из значений не число')
        return 0
while True:
    num1, b, num2 = input().split()
    solve(num1, b, num2)





