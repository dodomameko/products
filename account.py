#讓使用者重複的輸入商品名稱->迴圈 適合在不知道次數的情況下使用
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = [name,price]
	products.append(p)
	#products.append('name','price')
print(products)

for p in products:
	print(p[0],'的價格是',p[1])