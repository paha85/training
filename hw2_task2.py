time = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

kimchi = []
for item in time:
    if item.isdigit():
        item = item.zfill(2)
        kimchi.append(f'"{item}"')
    elif item[1:].isdigit():
        item = item.zfill(3)
        kimchi.append(f'"{item}"')
    else:
        kimchi.append(item)
print(' '.join(kimchi))
