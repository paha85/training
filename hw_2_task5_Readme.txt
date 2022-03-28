Не стал сам придумывать цифры, решил, что в этом мне поможет рандом))
"""
import random
numbers = []
for num in range(0, 20):
    float_price = round(random.uniform(01.01, 100.00), 2)
    numbers.append(float_price)
print(numbers)
"""

Над заданием долго думал и перечитывал, гуглил использование join и reverse=True