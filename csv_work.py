from gpt_work import create_wish
import csv


def list_with_wishes():
    with open('input.csv', mode='r', encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        with open("output.csv", mode='w', encoding='utf-8') as w_file:
            writer = csv.writer(w_file, delimiter=",")
            writer.writerow(['Имя', 'Дата рождения', 'Поздравление'])
            count = 0
            for row in file_reader:
                if count == 0:
                    count += 1
                    continue
                else:
                    count += 1
                    text = create_wish(row[0])
                    writer.writerow([row[0], row[1], " ".join(text.split())])


list_with_wishes()
print("ГОТОВО!")
