def count_of_elements_in_str(string):
    if type(string) != str:
        raise TypeError()

    return len(string)


def test_count_of_elements_in_str():
    test_data = (
        # неправильный тип входного аргумента
        (1, None),
        (['1', '2', '3'], None),
        # корректная пара
        ('123', 3),
    )

    # рассматриваем всевозможные пары входных-выходных данных
    for data, correct_result in test_data:
        try:
            result = count_of_elements_in_str(data)
        except TypeError:
            # если исключение и ожидалось, то продолжаем тестирование
            if correct_result is None:
                continue
            # при корретных входных данных всё равно было выброшено исключение TypeError —> тесты не пройдены
            if type(data) == str:
                print(f'Не пройдено тестирование для данных: {data}. \n Передан входной аргумент неверного типа.')
                return False
        except Exception as error:
            # выброшено какое-то исключение —> тесты не пройдены
            print(
                f'Не пройдено тестирование для данных: {data}. \n В ходе работы функции была сгенерирована ошибка {error}')
            return False
        else:
            # если проблем с типами данных не возникло, то переходим к проверке алгоритма
            if result != correct_result:
                print(
                    f'Не пройдено тестирование для данных: {data}. Было возвращено значение {result} вместо "{correct_result}"')
                return False

    # если все тесты пройдены, то сообщаем об успешном прохождении тестирования
    print('Все тесты пройдены успешно')
    return True


test_count_of_elements_in_str()
