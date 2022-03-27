"""
Не стал сам придумывать цифры, решил, что в этом мне поможет рандом))
import random
numbers = []
for num in range(0, 20):
    float_price = round(random.uniform(01.01, 100.00), 2)
    numbers.append(float_price)
print(numbers)
"""
numbers = [59.22, 2.8, 43.51, 20.15, 11.33, 10.87, 11.5, 36.26, 80.46, 19.52, 36.86, 17.74, 47.24, 23.18, 39.36, 28.46,
          2.34, 72.92, 7.16, 92.4]
print(id(numbers))

#5.A
prices = [str(x) for x in numbers]
full_prices = []
for price in prices:
    price_two = price.split('.')
    full_prices.append(f'{price_two[0].zfill(2)} руб. {price_two[1].zfill(2)} коп.')
full_prices_str = ', '.join(full_prices)
print(full_prices_str)
print(id(full_prices_str))

#5.B
print(sorted(full_prices))
print(id(numbers))

#5.C
full_prices_reversed = full_prices.copy()
full_prices_reversed.sort(reverse=True)
print(full_prices_reversed)
#print(reversed(sorted(full_prices_reversed)))