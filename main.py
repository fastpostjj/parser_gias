"""
определить версию Chrome:
chrome://settings/help

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import file_path
from utils.parser_gias import FindProcedures
from utils.save_to_xls import save_xslx


# URL = "https://gias.by/gias/#/"
URL = "https://gias.by/gias/#/purchase/current?extended"


def main():
    driver = webdriver.Chrome()
    driver.get(URL)
    new_object_procedure = FindProcedures(driver)
    driver = new_object_procedure.main_engine()

    # Парсим полученную страницу
    # data = new_object_procedure.parser(driver)
    # if data:
    #     new_object_procedure.list_data += data

    # Проходим циклом по страницам и парсим их
    try:
        # Ждем загрузки кнопок пагинации
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((
            By.CLASS_NAME,
            "ant-pagination"
            )))

        result_data = []
        while True:
            data = new_object_procedure.parser(driver)
            if data:
                result_data += data

            # Нажимаем кнопку next, если она активна
            next_button = driver.find_element(
                By.CLASS_NAME,
                "ant-pagination-next"
                )
            if next_button.get_attribute("aria-disabled") == "true":
                break
            else:
                next_button.click()

            # Ждем загрузки следующей страницы
            wait.until(EC.visibility_of_element_located((
                By.CLASS_NAME,
                "ant-pagination-item-active"
                )))
        if new_object_procedure.list_data:
            save_xslx(
                filename_xls=file_path,
                data=new_object_procedure.list_data
                )
    except Exception as error:
        print("Ошибка парсинга по циклу:", error)
    time.sleep(30)
    driver.close()


if __name__ == "__main__":
    main()
