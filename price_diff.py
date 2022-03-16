from constants import(
    today_date,
    price_drop_percentage
)
import csv 

day_1 = csv.reader(open('books_amazon_goodreads_15_03_2022.csv', 'r'))
row_1 = next(day_1)

day_2 = csv.reader(open('books_amazon_goodreads_16_03_2022.csv', 'r'))
row_2 = next(day_2)

for x,y in zip(day_1, day_2):
    if x[3] != 0:
        price_drop = x[3] - y[3]/ x[3]
        percentage = price_drop * 100
        if(percentage>=price_drop_percentage):
            with open('price_diff.csv', 'w')as a:
                a.write(x)
