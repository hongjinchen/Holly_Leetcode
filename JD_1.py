good_number=5
jindong_price=5
# a_price_list=['2', '1', '2', '1', '2']
# b_price_list=['1', '2', '1', '2', '3']
a_price_list=['2', '1', '2', '1', '2']
b_price_list=['1', '2', '1', '2', '3']
# 递归：是否能够从ab处获得更小的成本
# 递归：是否能够从ab处获得更小的成本
dic={}
def digui(index, a_price_list, b_price_list, prices,good_number):
    if index == good_number:
        return prices
    else:
        a_answer=0
        b_answer=0
        if ""+str(index + 1)+""+str(prices + int(a_price_list[index])) in dic:
            a_answer=dic[""+str(index + 1)+""+str(prices + int(a_price_list[index]))]
        else:
            a_answer=digui(
                index + 1, a_price_list, b_price_list, prices + int(a_price_list[index]),good_number
            )
            dic[""+str(index + 1)+""+str(prices + int(a_price_list[index]))]=a_answer
        if ""+str(index + 1)+""+str(prices + int(b_price_list[index])) in dic:
            b_answer=dic[""+str(index + 1)+""+str(prices + int(b_price_list[index]))]
        else:
            b_answer=digui(
                index + 1, a_price_list, b_price_list, prices + int(b_price_list[index]),good_number
            )
            dic[""+str(index + 1)+""+str(prices + int(b_price_list[index]))]=b_answer
        return min(a_answer,b_answer)
        
min_price=digui(0,a_price_list,b_price_list,0,int(good_number))
if min_price<=jindong_price:
    print(min_price)
else:
    print(jindong_price)
