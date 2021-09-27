shop={}
shop['apple']=2
a=shop['apple']-1
shop['apple']=a

def sell(list):
    if list == 'apple':
        a=shop[list]-1
        shop[list]=a
    return shop
a=input("че надо").split()
print(sell(a))



