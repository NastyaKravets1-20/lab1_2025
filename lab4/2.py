a=int(input('введите место:'))
if a in range(1,10):
    print('вверхний')
if a in range(10,20):
    print('нижний')
if a in range(20,30):
    print('купе')
if a in range(30, 41):
        print('боковое')
else:
    print("нет мест")
