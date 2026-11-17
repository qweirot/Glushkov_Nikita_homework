import csv

INPUT_FILE = 'Corp_Summary.csv'
OUTPUT_FILE = 'output.csv'


def read_file(filename):

    employes = []

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=";")
        line_count = 0

        for row in reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                employes.append({
                    'ФИО': row[0],
                    'Департамент': row[1],
                    'Отдел': row[2],
                    'Должность': row[3],
                    'Оценка': float(row[4]),
                    'Оклад': int(row[5]),
                })

    return employes


def report1(employes: list):

    departments = {}

    for i in employes:
        department = i['Департамент']
        otdel = i['Отдел']

        if department not in departments:
            departments[department] = set()

        departments[department].add(otdel)

    for i, v in departments.items():
        print(f'{i}: {v}')


def get_statistic(employes: list) -> list:

    departments = {}

    for i in employes:
        department = i['Департамент']
        salary = i['Оклад']

        if department not in departments:
            departments[department] = []

        departments[department].append(salary)

    statistic = []
    for department, salary in departments.items():
        statistic.append({
                    'Департмент': department,
                    'Количество человек': len(salary),
                    'Минимальная': min(salary),
                    'Максимальная': max(salary),
                    'Средняя': round(sum(salary) / len(salary)),
                })

    return statistic


def report2(employes: list):

    statistic = get_statistic(employes)
    for i in statistic:
        print(i)


def report3(employes: list, filename=OUTPUT_FILE):

    statistic = get_statistic(employes)

    with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=";")

            writer.writerow([
                'Департамент',
                'Количество сотрудников',
                'Минимальный оклад',
                'Максимальный оклад',
                'Средний оклад'
            ])

            for i in statistic:
                writer.writerow([
                    i['Департмент'],
                    i['Количество человек'],
                    i['Минимальная'],
                    i['Максимальная'],
                    i['Средняя']
                ])
    print(f'Отчет сохранен в {filename}')


if __name__ == "__main__":

    x = int(input('Введите вариант отчёта: '))
    employes = read_file(INPUT_FILE)

    if x == 1:
        report1(employes)
    elif x == 2:
        report2(employes)
    elif x == 3:
        report3(employes)
