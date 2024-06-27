def calculate_net_price(list_price , discount = 0.0 , tax= 0.05):

    net_price = list_price * (1 - discount)*(1+tax)

    return net_price

print(calculate_net_price(500))
print(calculate_net_price(500, 0.1))
print(calculate_net_price(500, 0.1 , 0.0))



# ----------------------

import time

def count_up(start, end):
    for x in range(start, end + 1):
        print(x)
        time.sleep(0.1)
print("Done")

count_up(0, 10)


