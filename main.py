from database import *

import os
from loguru import logger as log
from time import sleep

class Add_Game: # Класс, включающий функцию добавления игры в базу данных
    def __init__(self, name_arg: str, publisher_arg: str, year_arg: int):
        self.name = name_arg
        self.publisher = publisher_arg
        self.year = year_arg

    def Add(self) -> None:
        result = adding_a_game(self.name, self.publisher, self.year)
        if result:
            log.success("Игра успешно добавлена!")
        else:
            log.error("Что-то пошло не так! Повторите попытку или обратитесь к кодеру.")

class Search_Game: # Класс, включающий функцию поиска желаемой игры в базе данных.
    def __init__(self, name_arg: str, publisher_arg: str, year_arg: int): # Инициализация переменных для дальнейшей работы функции класса.
        self.name = name_arg
        self.publisher = publisher_arg
        self.year = year_arg

    def Search(self) -> None:
        result = searching_a_game(self.name, self.publisher, self.year)
        if result:
            log.success(f"Игра успешно найдена!: Название - {result[0]} | Издатель - {result[1]} | Год издания - {result[2]}")
        elif not result:
            log.error("Игра не была найдена в базе данных!")

class Remove_Game: # Класс, включающий функцию удаления желаемой игры, если она есть в базе данных.
    def __init__(self, name_arg: str, publisher_arg: str, year_arg: int): # Инициализация переменных для дальнейшей работы функции класса.
        self.name = name_arg
        self.publisher = publisher_arg
        self.year = year_arg

    def Removing(self) -> None:
        result = removing_a_game(self.name, self.publisher, self.year)
        if result:
            log.success("Игра успешно удалена!")
        else:
            log.error("Игру не удалось удалить!")

class Editing_Game: # Класс, включающий функцию редактирования желаемой игры, если она есть в базе данных.
    def __init__(self, name_arg: str, publisher_arg: str, year_arg: int): # Инициализация переменных для дальнейшей работы функции класса.
        self.name = name_arg
        self.publisher = publisher_arg
        self.year = year_arg

    def Editing(self) -> None:
        new_name = input("Введите новое имя для обновления данных: ") # Новые имя игры
        new_publisher = input("Введите нового издателя для обновления данных: ") # Новый издатель игры
        new_year = int(input("Введите новые данные о годе издания: ")) # Новый год издания

        result = editing_a_game(self.name, self.publisher, self.year, new_name, new_publisher, new_year)
        if result:
            log.success("Игра успешно отредактирована!")
        else:
            log.error("Данные об игре изменить не удалось!")

class Games_Output: # Класс, включающий функцию вывода всего списка игр в базе данных.
    def Output_Games(self) -> None:
        result = outputting_games()
        if result:
            for line_info in result:
                for index in range(1):
                    print(f"Название игры - {line_info[index]} | Издатель - {line_info[index + 1]} | Год издания - {line_info[index + 2]}")
        else:
            log.error("Таблица пустая!")

class MainClass(Add_Game, Search_Game, Remove_Game, Editing_Game, Games_Output):
    def __init__(self, name_prime: str, publisher_prime: str, year_prime: int): # Ранняя инициализация всех функций (свой метод)
        Add_Game.__init__(self, name_prime, publisher_prime, year_prime)
        Search_Game.__init__(self, name_prime, publisher_prime, year_prime)
        Remove_Game.__init__(self, name_prime, publisher_prime, year_prime)
        Editing_Game.__init__(self, name_prime, publisher_prime, year_prime)

        self.argument: int = self.PrintMenu() # Вывод меню при создании экземпляра класса

    @staticmethod
    def Create_Table() -> None: # Статичная функция, не требующая каких-либо аргументов при обращении. Решил сделать через обращение, как к статической функции, а
        creating_a_table()      # не через инициализацию, как в случае с функцией PrintMenu.

    def PrintMenu(self) -> int: # Функция вывода меню и фиксации выбора пользователя
        os.system("cls")
        argument = int(input("        Меню     \n"
                             "1. Добавить игру\n"
                             "2. Найти игру\n"
                             "3. Удалить игру\n"
                             "4. Отредактировать игру\n"
                             "5. Вывести список игр\n"
                             "Ваш выбор: "))
        return argument # переменная, отвечающая за выполнение соответствующей функции

    def Making_Job_Done(self) -> None: # Функция, отвечающая за реализацию действий
        try:
            if self.argument == 1:
                Add_Game.Add(self)
            elif self.argument == 2:
                Search_Game.Search(self)
            elif self.argument == 3:
                Remove_Game.Removing(self)
            elif self.argument == 4:
                Editing_Game.Editing(self)
            elif self.argument == 5:
                Games_Output.Output_Games(self)
            else:
                log.error("Выбран неправильный номер операции!")
        except Exception as error:
            log.error(f"Произошла ошибка! - {error}")

def clear_console() -> None: # Очистка консоли (для красоты)
    sleep(2)
    os.system("cls")

if __name__ == "__main__":
    MainClass.Create_Table() # Создание базы данных в случае, если её нет.
    while True:
        clear_console()
        print("Введите информацию об игре, с которой хотите взаимодействовать!\nЕсли хотите вывести список игр, введите везде '0' (без кавычек), а затем выберите 5-ый пункт")
        try:
            name, publisher, year = input("Введите название игры: "), input("Введите название издателя: "), int(input("Введите год издания игры: "))
            if not name or not publisher: # На случай, если одно из заполняемых полей формата str будет пустым
                raise ValueError
        except ValueError: # На случай, если одно из заполняемых полей будет пустым или все поля будут пустыми.
            log.error("Вы ввели неправильное/ые значение(я) для переменной(ых)!")
            continue

        clear_console()
        Body = MainClass(name, publisher, year)
        Body.Making_Job_Done()
        input("Нажмите ENTER, чтобы продолжить...")