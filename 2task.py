from collections import Counter


def main():

    queries = [
        'чехол',
        'iphone',
        'чехол',
        'наушники',
        'iphone',
        'iphone',
        'кабель',
        'чехол',
        'iphone',
    ]

    # 1
    print(f'сколько всего поисковых запросов в ленте: {len(queries)}')

    # 2
    counter_queries = Counter(queries)
    print(f'сколько раз ввели каждый запрос: {counter_queries}')

    # 3
    print(f'какой запрос вводили чаще всего: {counter_queries.most_common(1)[0]}')

    # 4
    dolya = counter_queries.most_common(1)[0][1] / counter_queries.total()
    print(f'какую долю всех поисков он занимает: {dolya}')

    # 5
    one_time = {k: v for k, v in counter_queries.items() if v == 1}
    print(f'какие запросы встретились один раз: {one_time}')


if __name__ == "__main__":
    main()
