phone_book = {}
phone_book['Jenny'] = 848484
phone_book['emergency'] = 911
s=phone_book['emergency']
print(type(s))
print(phone_book)
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

