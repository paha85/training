numbers = [59.22, 2.8, 43.51, 20.15, 11.33, 10.87, 11.5, 36.26, 80.46, 19.52, 36.86, 17.74, 47.24, 23.18, 39.36, 28.46,
           2.34, 72.92, 7.16, 92.4]

# 5.A
prices = [str(x) for x in numbers]
full_prices = []
for price in prices:
    price_two = price.split('.')
    full_prices.append(f'{price_two[0].zfill(2)} руб. {price_two[1].zfill(2)} коп.')
full_prices_str = ', '.join(full_prices)
print( full_prices_str)
id_before = id(full_prices)
print(f'Идентификатор списка до сортировки: {id(full_prices)}')

# 5.B
full_prices.sort()
print(full_prices)
id_after = id(full_prices)
print(f'Идентификатор списка после сортировки: {id(full_prices)}')
print(f'Список цен до сортировки равен списку после сортировки: {id_before == id_after}')

# 5.C
full_prices_reversed = full_prices.copy()
full_prices_reversed.sort(reverse=True)
print(full_prices_reversed)
print(f'Идентификатор списка после копирования и обратной сортировки: {id(full_prices_reversed)}')

# 5.D
print(sorted(full_prices_reversed[-20:-15]))
