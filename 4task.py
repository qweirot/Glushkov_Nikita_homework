def main():

    days = [
        {'day': 'пн', 'orders': 20, 'revenue': 40_000, 'returns': 2},
        {'day': 'вт', 'orders': 16, 'revenue': 19_200, 'returns': 4},
        {'day': 'ср', 'orders': 25, 'revenue': 55_000, 'returns': 1},
        {'day': 'чт', 'orders': 10, 'revenue': 12_000, 'returns': 3},
        {'day': 'пт', 'orders': 30, 'revenue': 48_000, 'returns': 3},
    ]

    # 1
    week_revenue = sum(i['revenue'] for i in days)
    print(f'выручку за всю неделю: {week_revenue}')

    # 2
    max_revenue = 0
    for i in days:
        if i['revenue'] > max_revenue:
            max_revenue = i['revenue']
            max_day = i['day']

    print(f'день с самой большой выручкой: {max_day}')

    # 3
    week_avg = {}
    for i in days:
        week_avg[i['day']] = i['revenue'] / i['orders']
    print(f'среднюю выручку на один заказ в каждый день: {week_avg}')

    # 4
    days_with_returns = {}
    for i in days:
        if i['returns'] / i['orders'] > 0.2:
            days_with_returns[i['day']] = i['returns'] / i['orders'] * 100
    print(f'дни, где возвратов больше 20% заказов: {days_with_returns}')


if __name__ == "__main__":
    main()
