def main():

    reviews = [
        {'id': 1, 'product': 'Чехол', 'stars': 5},
        {'id': 1, 'product': 'Чехол', 'stars': 3},
        {'id': 1, 'product': 'Чехол', 'stars': 4},
        {'id': 2, 'product': 'Наушники', 'stars': 2},
        {'id': 2, 'product': 'наушники', 'stars': 2},
        {'id': 2, 'product': 'НАУШНИКИ', 'stars': 5},
        {'id': 3, 'product': 'Планшет', 'stars': 5},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 4, 'product': 'Колонка', 'stars': 4},
        {'id': 5, 'product': 'Кабель', 'stars': 1},
    ]

    for i in reviews:
        i['product'] = i['product'].capitalize()

    # 1
    product = {}
    for i in reviews:
        if i['product'] not in product:
            product[i['product']] = {'sum': 0, 'count': 0}
        product[i['product']]['sum'] += i['stars']
        product[i['product']]['count'] += 1

    avg_stars = {k: v['sum']/v['count'] for k, v in product.items()}
    print(f'среднюю оценку каждого товара: {avg_stars}')

    # 2
    product = {k: v for k, v in product.items() if v['count'] >= 2}
    avg_stars_new = {k: v['sum']/v['count'] for k, v in product.items()}

    min_avg_stars = 10
    for k, v in avg_stars_new.items():
        if v < min_avg_stars:
            min_avg_stars = v
            product_min_rating = k

    answer = {product_min_rating: min_avg_stars}
    print(f'худший товар по средней оценке среди тех, у кого хотя бы два отзыва: {answer}')

    # 3
    count_negative = sum(1 for i in reviews if i['stars'] == 1 or i['stars'] == 2)
    print(f'сколько отзывов на 1 или 2 звезды: {count_negative}')

    # 4
    dolya_negative = count_negative / len(reviews) * 100
    print(f'какую долю всех отзывов они составляют: {dolya_negative}%')


if __name__ == "__main__":
    main()
