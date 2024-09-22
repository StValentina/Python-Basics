budget = int(input())

tickets = 0
other_stuff = 0

product = input()

while product != "End":
    price = 0
    if len(product) > 8:
        price = ord(product[0]) + ord(product[1])
        if budget - price < 0:
            break
        else:
            tickets += 1
            budget -= price
    else:
        price = ord(product[0])
        if budget - price < 0:
            break
        else:
            other_stuff += 1
            budget -= price
    product = input()

print(tickets)
print(other_stuff)




