s = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(" ".join(map(lambda x: '"%s"' % __import__('re').sub('\d+', lambda x: f' { x[0] } '.zfill(2), x)
if any(map(str.isdigit, x)) else x, s)))