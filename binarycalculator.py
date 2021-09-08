"""Не считает(("""
#       def podshet(stack)
#         if (x == '+'):
#             a2 = s[0]
#             a1 = s[1]
#             stack.append(int(a2)+int(a1))
#         elif (x == '-'):
#             a2 = s[0]
#             a1 = s[1]
#            stack.append(int(a2)*int(a1))
#         elif (x == '*'):
#             a2 = s[0]
#             a1 = s[1]
#             stack.append(int(a2)*int(a1))
#         elif (x == '/'):
#             a2 = s[0]
#             a1 = s[1]
#            stack.append(int(a2/int(a1))
#         else:
#             stack.append(list+stack)
#     return stack[0]
#
#


"""Калькулятор через стек
Input: На вход поступает список из чисел и алгебраических знаков,
создается список(стек), если в списке содержатся числа то они заносятся стек, если на вход попадает любой знак
берем два последние числа из стека до этого знака и кладем их результат их операции.
Output: Список из полученного результата и прможетучное резульататы"""


def stackcalculator(list):
    stack = []
    if not list:
        return "Пустой ввод"
    else:
        for i in range(len(list)):
            if type(list[i]) is int:
                stack.append(list[i])
                continue

            op1, op2 = stack.pop(), stack.pop()

            if list[i] == '+':
                stack.append(op2 + op1)
                print(stack)
            elif list[i] == '*':
                stack.append(op2 * op1)
                print(stack)

            elif list[i] == '/':
                stack.append(op2 / op1)
                print(stack)

            elif list[i] == '-':
                stack.append(op2 - op1)

        print("Финальный ответ:")
        return stack


print(stackcalculator([1, 2, 3, 4, '+', '*']))
