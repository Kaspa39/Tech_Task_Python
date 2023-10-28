import sqlite3 as sqlite
from loguru import logger as log

def creating_a_table() -> None: # Функция создания базы данных в случае, если её не будет.
    try:
        connection = sqlite.connect("database.db")
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Games (
                        name TEXT,
                        publisher TEXT,
                        year INTEGER
                        )''')

        connection.commit()
        connection.close()

    except sqlite.Error as error:
        log.error(f"Произошла ошибка! - {error}")

def adding_a_game(name: str, publisher: str, year: int) -> bool: # Функция добавления игры в базу данных.
    try:
        connection = sqlite.connect("database.db")
        cursor = connection.cursor()

        task = '''INSERT INTO Games (name, publisher, year) VALUES (?, ?, ?)'''
        data = (name, publisher, year)

        cursor.execute(task, data)

        connection.commit()
        connection.close()

        return True

    except sqlite.Error as error:
        log.error(f"Произошла ошибка! - {error}")
        return False

def searching_a_game(name: str, publisher: str, year: int) -> list[str]: # Функция поиска игры в базе данных
    try:
        connection = sqlite.connect("database.db")
        cursor = connection.cursor()

        task = '''SELECT name, publisher, year FROM Games WHERE name = ? AND publisher = ? AND year = ?'''
        data = (name, publisher, year)

        cursor.execute(task, data)
        result = cursor.fetchone()

        connection.close()

        return result

    except sqlite.Error as error:
        log.error(f"Произошла ошибка! - {error}")

def removing_a_game(name: str, publisher: str, year: int) -> bool: # Функция удаления игры из базы данных
    try:
        connection = sqlite.connect("database.db")
        cursor = connection.cursor()

        task = '''DELETE FROM Games WHERE name = ? AND publisher = ? AND year = ?'''
        data = (name, publisher, year)

        cursor.execute(task, data)

        connection.commit()
        connection.close()

        return True

    except sqlite.Error as error:
        log.error(f"Произошла ошибка! - {error}")
        return False

def editing_a_game(name: str, publisher: str, year: int, new_name: str, new_publisher: str, new_year: int) -> bool: # Функция редактирования данных об игре в базе данных
    try:
        connection = sqlite.connect("database.db")
        cursor = connection.cursor()

        # Действия для проверки наличия игры в базе данных
        checkup_task = '''SELECT * FROM Games WHERE name = ? AND publisher = ? AND year = ?'''
        checkup_data = (name, publisher, year)

        cursor.execute(checkup_task, checkup_data)
        check = cursor.fetchone()
        # --------------------------------------------- #
        if check: # В случае, если она есть в базе данных, выполняется обновление данных об игре.
            task = '''UPDATE Games SET name = ?, publisher = ?, year = ? WHERE name = ? AND publisher = ? AND year = ?'''
            data = (new_name, new_publisher, new_year, name, publisher, year)

            cursor.execute(task, data)

            connection.commit()
            connection.close()

            return True
        else:
            log.error("Такой игры нет!")

    except sqlite.Error as error:
        log.error(f"Произошла ошибка! - {error}")
        return False


def outputting_games() -> list: # Функция вывода списка всех игр из базы данных
    try:
        connection = sqlite.connect("database.db")
        cursor = connection.cursor()

        task = '''SELECT * FROM Games'''

        cursor.execute(task)
        result = cursor.fetchall()

        connection.close()

        return result # Возвращаем список со всеми играми

    except sqlite.Error as error:
        log.error(f"Произошла ошибка! - {error}")