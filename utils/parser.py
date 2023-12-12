"""
Предмет закупки
Наименование заказчика/организатора
Место нахождения заказчика/организатора
Номер
Ориентировочная стоимость
Дата окончания приема предложений

Пусто:
Время подачи
Тип закупки - вид процедуры закупки


Варианты заĸупоĸ:
«Заĸупĸа из одного источниĸа» - соĸращенное название
«ЗОИ»
«Элеĸтронный ауĸцион» - соĸращенное название «ЭА»
«Запрос ценовых предложений» - соĸращенное название
«ЗЦП»

Дата размещения
в поле состояние закупки
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ParserGias:
    parsed_data = []
    def parser(self, driver):
        # Парсинг страницы
        try:
            table_header = driver.find_element(By.CLASS_NAME, "ant-table-thead")  # Находим элемент с классом "ant-table-thead"
            subject_element = table_header.find_element(By.CLASS_NAME, "ant-table-column-title")  # Находим элемент с классом "ant-table-column-title"
            subject_text = subject_element.text  # Извлекаем текстовое содержимое элемента

            table_body = driver.find_element(By.CLASS_NAME, "ant-table-tbody")  # Находим элемент с классом "ant-table-tbody"
            rows = table_body.find_elements(By.CLASS_NAME, "ant-table-row")  # Находим все строки в таблице

            for row in rows:
                link_element = row.find_element(By.TAG_NAME, "a")  # Находим первую ячейку в каждой строке
                link_href = link_element.get_attribute("href")  # Извлекаем значение атрибута "href" ссылки
                cells = row.find_elements(By.TAG_NAME, "td")  # Находим все ячейки в строке
                result_table = []
                for cell in cells:
                    try:
                        result_table.append(cell.text)
                    except Exception as error:
                        print("Ошибка", error, cell)
                        result_table.append('')
                data = {
                    "url": link_href,
                    "title": result_table[0],
                    "name": result_table[1],
                    "adress": result_table[2],
                    "number": result_table[3],
                    "amount": result_table[4],
                    "date_before": result_table[5],
                    }
                """
                Предмет закупки
                Наименование заказчика/организатора закупки
                Место нахождения заказчика/организатора
                Номер
                Ориентировочная стоимость
                Дата окончания приема предложений
                Время подачи
                Тип закупки
                Дата размещения
                """
                data = data | self.parsing_card(link_href)
                self.parsed_data.append(data)
            return self.parsed_data
        except Exception as error:
            print("Ошибка при парсинге страницы закупок: ", error)

    @staticmethod
    def transform(text) -> str:
        """
        Трансформирует теск в сокращение
        Нет такого варианта закупки: Закупка из одного источника
        """
        if text == "Заĸупĸа из одного источниĸа":
            return "ЗОИ"
        elif text == "Электронный аукцион":
            return "ЭА"
        elif text == "Запрос ценовых предложений":
            return "ЗЦП"
        else:
            print(f'Нет такого варианта закупки: {text}')
            return text

    def parsing_card(self, url):
        """
        Парсим карточку закупки.
        Находим на странице:
        - варианты заĸупоĸ
        - дату размещения
        """
        driver = webdriver.Chrome()
        driver.get(url)

        # ждем загрузки карточки
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'ant-card'))
            )
        try:
            element = driver.find_element(
                By.XPATH,
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div/span/span/strong'
                )
            date = element.text
            procedure_type = driver.find_element(
                By.XPATH,
                '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/form/div[3]/div[2]/div/span/span/strong'
                )

            return {
                "data_posting": date,
                "procedure_type": self.transform(procedure_type.text)
                }
        except Exception as error:
            print("Ошибка парсинга карточки закупки url=", url, error)
        driver.close()


def parser(driver):
    parser = ParserGias().parser(driver)


if __name__ == "__main__":
    # print(ParserGias().parsing_card("https://gias.by/gias/#/purchase/current/e9b4e858-8237-49bd-abba-9bb77e41615b"))
    # print(ParserGias().parsing_card("https://gias.by/gias/#/purchase/current/be784b64-b64e-4276-b996-dacdd6c12ca8"))
    print(ParserGias().parsing_card("https://gias.by/gias/#/purchase/current/b3fa72b0-941e-45ae-b322-6664b3322830"))
