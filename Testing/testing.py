#magic = 4
#mp = input()

#if mp != "4" and mp != "7":
#    print("You dont have enough")
#else:
#    print("You have enough to cast the spell")

def order_sum(prices):
    total = sum(prices)
    average = total/len(prices)
    return len(prices),total,average

count,total,average = order_sum([24.99,120.00,8.50,46.25])
print(f"Orders: {count}")
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")

#result=order_sum([10.00,30.00])
#print(type(result).__name__,result)