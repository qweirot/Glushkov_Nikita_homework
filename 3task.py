from collections import defaultdict


def main():

    orders = [
        {'id': 1, 'buyer': 'anya', 'status': 'delivered', 'amount': 900},
        {'id': 2, 'buyer': 'boris', 'status': 'returned', 'amount': 4_500},
        {'id': 3, 'buyer': 'anya', 'status': 'delivered', 'amount': 1_500},
        {'id': 4, 'buyer': 'vera', 'status': 'delivered', 'amount': 3_200},
        {'id': 5, 'buyer': 'boris', 'status': 'delivered', 'amount': 700},
        {'id': 6, 'buyer': 'gleb', 'status': 'returned', 'amount': 2_100},
    ]

    # 1
    sum_returns = 0
    for i in orders:
        if i['status'] == 'returned':
            sum_returns += i['amount']
    print(f'на какую сумму оформили возвраты: {sum_returns}')

    # 2
    people_who_return = [i for i in orders if i['status'] == 'returned']
    print(f'кто хотя бы раз вернул заказ: {people_who_return}')

    # 3
    count_delivered = defaultdict(int)
    for i in orders:
        if i['status'] == 'delivered':
            count_delivered[i['buyer']] += 1

    print(f'сколько заказов доставлено покупателю: {dict(count_delivered)}')

    # 4
    avg_orders = sum(i['amount'] for i in orders)/len(orders)
    print(f'средний чек доставленных заказов: {avg_orders}')


if __name__ == "__main__":
    main()
