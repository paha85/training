time = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

kimchi = []
for item in time:
    if item.isdigit():
        item = item.zfill(2)
        kimchi.append(item)
        # kimchi.append(f'"{item}"')
        kimchi.insert(kimchi.index(item), '"')
        kimchi.insert(kimchi.index(item) + 2, '"')
    elif item[1:].isdigit():
        item = item.zfill(3)
        # kimchi.append(f'"{item}"')
        kimchi.append(item)
        kimchi.insert(kimchi.index(item), '"')
        kimchi.insert(kimchi.index(item) + 2, '"')
    else:
        kimchi.append(item)
print(kimchi)

kimchi[1:4] = [''.join(kimchi[1:4])]
kimchi[3:6] = [''.join(kimchi[3:6])]
kimchi[8:11] = [''.join(kimchi[8:11])]
kimchi = ' '.join(kimchi)
print(f'{kimchi}')
