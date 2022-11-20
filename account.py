#讓使用者重複的輸入商品名稱->迴圈 適合在不知道次數的情況下使用
#程式重構: 定義好function後考慮是否要參數 or 是否需要回傳(return)
#一個function只做一件事
import os 

#讀取檔案
def read_file(filename):
    products = []    
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products #因為結果有寫入到一個清單

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        p = [name,price]
        products.append(p)
    #products.append('name','price')
    print(products)
    return products #有新增清單，所以重新存下來

def print_products(products):
    for p in products:
        print(p[0],'的價格是',p[1])
        #只是普通的印出檔案，沒有新增要素，所以不需要回傳

#將清單寫入到檔案中
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

#只是寫入檔案，不需要回傳

#整理成function，將主要執行的程式碼，整理成function(main function)

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查檔案在不在
        print('yeah! 找到檔案了')
        products = read_file(filename)

    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main() 


