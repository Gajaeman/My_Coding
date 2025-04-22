lunch = {}
for _ in range(2):
    menu, price = input("메뉴와 가격을 써").split()
    lunch[menu] = price

what = input("뭐 알고싶어?")
print(lunch[what])