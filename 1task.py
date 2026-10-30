def main():

    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    both_cities = moscow & kazan
    only_moscow = moscow - kazan
    only_kazan = kazan - moscow
    count_distinct_items = len(set(moscow | kazan))

    print(f'что можно забрать в любом из двух городов: {both_cities}')
    print(f'что есть только в Москве: {only_moscow}')
    print(f'что есть только в Казани: {only_kazan}')
    print(f'сколько разных товаров на обоих складах вместе: {count_distinct_items}')


if __name__ == "__main__":
    main()
