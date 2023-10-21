n=3
m=2
price_list=['4', '8', '6']
youhui_list=[ ['5', '1'], ['8', '5']]

youhui_list=sorted(youhui_list)
total_price=0
for item in price_list:
    item=int(item)
    min_price=item
    for youhui in youhui_list:
        if int(youhui[0])<=item:
            if item-int(youhui[1])< min_price:
                min_price=item-int(youhui[1])

    total_price+=min_price
print(total_price)

