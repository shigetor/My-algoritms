"""Калькулятор через стек
Input: На вход поступает список из чисел и алгебраических знаков,
создается список(стек), если в списке содержатся числа то они заносятся стек, если на вход попадает любой знак
берем два последние числа из стека до этого знака и кладем их результат их операции.
Output:Резульат вычислений и прможетучное резульататы"""


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
        return stack.pop()

a=input("input: ").split()
a = [int(x) if x.isdigit() or x[0]=='-' and x[1:].isdigit() else x for x in a]
print(stackcalculator(a))
