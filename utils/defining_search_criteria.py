import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import desired_category, desired_subcategory, search_text, \
      date_start, date_end


class FindProcedures():
    """
    Класс работы с элементами странцы.
    Кликаем на заданные чекбоксы, задаем текст в поле поиска,
    даты начала и конца периода.
    """
    list_data = []

    def __init__(self, driver):
        self._set_parameters()
        self.driver = driver

    def _set_parameters(self):
        self._date_start = date_start
        self._date_end = date_end
        self._desired_category = desired_category
        self._desired_subcategory = desired_subcategory
        self._search_text = search_text

    @property
    def date_start(self):
        return self._date_start

    @date_start.setter
    def date_start(self, value):
        self._date_start = value

    @property
    def date_end(self):
        return self._date_end

    @date_end.setter
    def date_end(self, value):
        self._date_end = value

    @property
    def search_text(self):
        return self._search_text

    @search_text.setter
    def search_text(self, value):
        self._search_text = value

    @property
    def desired_category(self):
        return self._desired_category

    @desired_category.setter
    def desired_category(self, value):
        self._desired_category = value

    @property
    def desired_subcategory(self):
        return self._desired_subcategory

    @desired_subcategory.setter
    def desired_subcategory(self, value):
        self._desired_subcategory = value

    def choose_dates(self):
        try:
            # Календарь
            # Явное ожидание элемента с полем
            # ввода даты начала в течение 10 секунд
            calendar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR,
                    "#dtCreate > span > i > svg"
                    ))
            )

            # Открыть календарь
            calendar.click()

            # Найти и кликнуть на поле начальной даты
            start_date_field = self.driver.find_element(
                By.CSS_SELECTOR,
                "input.ant-calendar-input[placeholder*= 'Начальная дата']"
                )

            # Очистить поле начальной даты
            start_date_field.clear()
            start_date_field.send_keys(self.date_start)
            start_date_field.send_keys(Keys.RETURN)

            # Найти и кликнуть на поле конечной даты
            end_date_field = self.driver.find_element(
                By.CSS_SELECTOR,
                "input.ant-calendar-input[placeholder*= 'Конечная дата']"
                )

            # Очистить поле конечной даты (если требуется)
            end_date_field.clear()

            # Ввести значение конечной даты
            end_date_field.send_keys(self.date_end)
            end_date_field.send_keys(Keys.RETURN)

        except Exception as error:
            print("Ошибка при задании дат в календаре: ", type(error), error)
        finally:
            return self.driver

    def choose_category(self):
        """
        Кликаем на заданные чекбоксы.
        """
        try:
            # Кликаем в поле с чекбоксами
            element_categories = self.driver.find_element(
                By.CSS_SELECTOR,
                'input[aria-label="filter select"]'
                )
            element_categories.click()

            # Ждем загрузки чекбоксов
            checkboxes = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_all_elements_located((
                    By.CLASS_NAME,
                    'ant-select-tree-treenode-switcher-close'
                    ))
            )

            # Проходим циклом по чекбоксам и кликаем на те,
            # которые заданы в config.py
            for checkbox in checkboxes:
                title_element = checkbox.find_element(
                    By.CLASS_NAME,
                    'ant-select-tree-title'
                    )
                title = title_element.text

                if title in self.desired_category:
                    checkbox.find_element(
                        By.CLASS_NAME,
                        'ant-select-tree-checkbox'
                        ).click()
                else:
                    switcher = checkbox.find_element(
                        By.CLASS_NAME,
                        'ant-select-tree-switcher'
                        )
                    switcher.click()

                    WebDriverWait(self.driver, 10).until(
                        EC.visibility_of_element_located((
                            By.CLASS_NAME,
                            'ant-select-tree-child-tree-open'))
                    )
                    sub_checkboxes = checkbox.find_elements(
                        By.CSS_SELECTOR,
                        '.ant-select-tree-child-tree-open .ant-select-tree-checkbox-inner'
                        )
                    sub_titles = checkbox.find_elements(
                        By.CSS_SELECTOR,
                        '.ant-select-tree-child-tree-open .ant-select-tree-title'
                        )

                    for i in range(len(sub_checkboxes)):
                        if sub_titles[i].text in self.desired_subcategory:
                            sub_checkboxes[i].click()

        except Exception as error:
            print("Ошибка загрузки чекбоксов. Error: ", type(error), error)
            exit()
        return self.driver

    def start_search(self):
        """
        Вводим текст для поиска и нажимаем кнопку "Поиск"
        """

        try:
            # Ждем загрузки элемента ввода
            element_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ant-input'))
            )

            # Поле поиска
            element_input = self.driver.find_element(By.CLASS_NAME, 'ant-input')
            element_input.send_keys(self.search_text)
            element_input.send_keys(Keys.RETURN)
        except Exception as error:
            print("Ошибка при вводе текста для поиска: ", type(error), error)
        return self.driver

    def parser(self, driver):
        # Парсинг страницы
        try:

            # Находим элемент с классом "ant-table-tbody"
            table_body = driver.find_element(By.CLASS_NAME, "ant-table-tbody")

            # Находим все строки в таблице
            rows = table_body.find_elements(By.CLASS_NAME, "ant-table-row")

            for row in rows:

                # Находим первую ячейку в каждой строке
                link_element = row.find_element(By.TAG_NAME, "a")

                # Извлекаем значение атрибута "href" ссылки
                link_href = link_element.get_attribute("href")

                # Находим все ячейки в строке
                cells = row.find_elements(By.TAG_NAME, "td")
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
                    "amount": self.transform_amount(result_table[4]),
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
                if self.parsing_card(link_href):
                    data = data | self.parsing_card(link_href)
                else:
                    print("Ошибка link_href=", link_href)
                self.list_data.append(data)
            return self.list_data
        except Exception as error:
            print("Ошибка при парсинге страницы закупок: ", error)

    @staticmethod
    def transform_amount(text):
        """
        Преобразуем строку в число
        """
        number = re.sub(r'[^-\d,.]', '', text)
        number = number.replace(',', '.')
        return float(number)

    @staticmethod
    def transform(text) -> str:
        """
        Трансформирует текст в сокращение
        """
        if text == "Закупка из одного источника":
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
            # element = driver.find_element(
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    '//*[@id="root"]/div/section/section/main/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/div/span/span/strong'
                    ))
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

    def main_engine(self):
        if self.date_start and self.date_end:
            self.choose_dates()
        if self.desired_category or self.desired_subcategory:
            self.choose_category()
        self.start_search()
        return self.driver
