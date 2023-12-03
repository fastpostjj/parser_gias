"""
определить версию Chrome:
chrome://settings/help

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


# URL = "https://selectel.ru/blog/courses/"
# URL = "https://gias.by/gias/#/"
URL = "https://gias.by/gias/#/purchase/current?extended"
search_text = "Андрей"
date_start = "01.12.2023 00:00"
date_end = "15.12.2023"

# browser = wd.Chrome("/usr/bin/chromedriver/")
# driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')
# driver = webdriver.Chrome(r'C:\Users\fastp\Downloads\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome()
driver.get(URL)
time.sleep(10)

try:
    # Явное ожидание элемента с полем ввода даты начала в течение 10 секунд
    start_date_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Начальная дата']"))
    )
    """

    # start_date_input = driver.find_element(
    #     By.XPATH,
    # #     "//input[@placeholder='Начальная дата']//span[@aria-label='22 ноября 2023 г.']"
    #     "//input[@placeholder='Начальная дата']//span[@aria-label='01.11.2023 00:00']"
    # )
    start_date_input.click()  # Открываем календарь

    # ввод даты выбором из календаря
    # start_date_input1 = driver.find_element(
    #     By.XPATH,
    #     "/html/body/div[8]/div/div/div/div/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[7]/div"
    # )
    # start_date_input1.click()

    # start_date_input.clear()
    start_date = datetime.strptime("01.11.2023 00:00", "%d.%m.%Y %H:%M")
    start_date_formatted = start_date.strftime("%d.%m.%Y %H:%M")
    start_date_input.send_keys(start_date_formatted)
    start_date_input.send_keys(Keys.RETURN)
    input_value_start = start_date_input.get_attribute('value')
    print("Присвоение input_value_start=", input_value_start)

    driver.execute_script("arguments[0].value = '01.11.2023 00:00'", start_date_input)
    input_value_start = start_date_input.get_attribute('value')
    print("После скрипта input_value_start=", input_value_start)




    # # Явное ожидание появления элемента
    # selected_date_element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((
    #         By.CSS_SELECTOR,
    #         ".ant-calendar-in-range-cell div[title='3 декабря 2023 г.']"))
    # )
    # # Нахождение определенной даты в календаре и выбор ее
    # # selected_date_element = driver.find_element(
    # #     By.CSS_SELECTOR,
    # #     ".ant-calendar-in-range-cell div[title='2 ноября 2023 г.']"
    # # )
    # selected_date_element.click()

    # Явное ожидание элемента с полем ввода даты окончания в течение 10 секунд
    end_date_input = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Конечная дата']"))
    )
    end_date_input1 = driver.find_element(
        By.XPATH,
        "/html/body/div[8]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[1]/div"
    )
    end_date_input1.click()
    input_value_end = end_date_input.get_attribute('value')
    print("input_value_end=", input_value_end)

    # # end_date_input.send_keys(Keys.RETURN)
    # # end_date_input.clear()
    # end_date_input.send_keys("30.11.2023 00:00")
    # end_date_input.send_keys(Keys.RETURN)
    end_date_input_all = driver.find_elements(
        # By.XPATH,
        # "/html/body/div[8]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/div"
        By.CLASS_NAME,
        'ant-calendar-date'
    )
    # for end_date in end_date_input_all:
    #     # print("end_date=", end_date, end_date.__dict__)
    #     print("end_date.text=", end_date.text)
    #     # end_date.click()

    ok_button = driver.find_element(By.CLASS_NAME,
                                    #   "ant-calendar-ok-btn.ant-calendar-ok-btn-disabled")
                                    "ant-calendar-ok-btn")
    ok_button.click()
    # ok_button.send_keys(Keys.RETURN)

    """
except Exception as error:
    print("Try load the calendar. Error: ", type(error), error)

for i in range(10):
    try:
        """
        <ul class="ant-select-selection__rendered" role="menubar">
        <li class="ant-select-search ant-select-search--inline"><span
        class="ant-select-search__field__wrap"><input type="text"
        class="ant-select-search__field" aria-label="filter select" aria-autocomplete="list" aria-multiline="false" value="" style="width: 4px;" aria-controls="rc-tree-select-list_1"><span
        class="ant-select-search__field__mirror">&nbsp;</span></span></li></ul>
        """
        element_categories = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="filter select"]')
        element_categories.click()
        # Ждем загрузки чекбоксов
        checkboxes = WebDriverWait(driver, 30).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, 'ant-select-tree-treenode-switcher-close'))
        )
        break
    except Exception as error:
        print("Попытка загрузки чекбоксов № ", i + 1, " Ошибка ", error)

try:
    desired_titles = ["Безопасность"]
    desired_subcategory = [
        "Медицинский инструмент",
        "Медицинское оборудование / комплектующие",
        "Расходные материалы"
        ]

    for checkbox in checkboxes:
        title_element = checkbox.find_element(By.CLASS_NAME, 'ant-select-tree-title')
        title = title_element.text

        if title in desired_titles:
            checkbox.find_element(By.CLASS_NAME, 'ant-select-tree-checkbox').click()
            print("title=", title)
        else:
            # sub_checkboxes = WebDriverWait(driver, 10).until(
            #     EC.visibility_of_all_elements_located((By.CLASS_NAME, 'ant-select-tree-treenode-switcher-close'))
            # )
            # check_box1 = checkbox.find_elements(By.CLASS_NAME, "ant-select-tree-child-tree")
            # check_box2 = checkbox.find_elements(By.CLASS_NAME, "ant-select-tree-checkbox")

            switcher = checkbox.find_element(By.CLASS_NAME, 'ant-select-tree-switcher')
            switcher.click()

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'ant-select-tree-child-tree-open'))
            )

            sub_checkboxes = checkbox.find_elements(By.CSS_SELECTOR, '.ant-select-tree-child-tree-open .ant-select-tree-checkbox-inner')
            sub_titles = checkbox.find_elements(By.CSS_SELECTOR, '.ant-select-tree-child-tree-open .ant-select-tree-title')

            for i in range(len(sub_checkboxes)):
                if sub_titles[i].text in desired_subcategory:
                    sub_checkboxes[i].click()
                    print("sub_titles[i].text=", sub_titles[i].text)

except Exception as error:
    print("Ошибка загрузки checkboxe. Error: ", type(error), error)
    if title:
        print("title=", title)
    if i and sub_titles[i] and sub_titles[i].text:
        print("sub_titles[i].text=", sub_titles[i].text)


try:
    # Ждем загрузки элемента ввода
    element_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ant-input'))
    )

    # Поле поиска
    # elem = driver.find_element(By.CLASS_NAME, 'ant-input.ant-input-lg')
    # elem = driver.find_element(By.ID, "contextTextSearch")
    element_input = driver.find_element(By.CLASS_NAME, 'ant-input')
    element_input.send_keys(search_text)
    element_input.send_keys(Keys.RETURN)
except Exception as error:
    print("Try load the input. Error: ", type(error), error)

# После ответа страницы, вы получите результат, если таковой ожидается.
# Чтобы удостовериться, что мы получили какой-либо результат, добавим утверждение:

assert "No results found." not in driver.page_source

# В завершение, окно браузера закрывается. Вы можете также
# вызывать метод quit вместо close. Метод quit закроет браузер
# полностью, в то время как close закроет одну вкладку. Однако,
# в случае, когда открыта только одна вкладка, по умолчанию большинство
#  браузеров закрывается полностью:
time.sleep(15)
driver.close()

"""
<span title="Культура" class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-open"><span class="ant-select-tree-title">Культура</span></span>
<ul class="ant-select-tree-child-tree ant-select-tree-child-tree-open" data-expanded="true" role="group"><li class="ant-select-tree-treenode-switcher-close" role="treeitem"><span class="ant-select-tree-switcher ant-select-tree-switcher-noop"></span><span class="ant-select-tree-checkbox"><span class="ant-select-tree-checkbox-inner"></span></span><span title="Другое" class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"><span class="ant-select-tree-title">Другое</span></span></li><li class="ant-select-tree-treenode-switcher-close" role="treeitem"><span class="ant-select-tree-switcher ant-select-tree-switcher-noop"></span><span class="ant-select-tree-checkbox"><span class="ant-select-tree-checkbox-inner"></span></span><span title="Концерты / выставки / экспозиции" class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"><span class="ant-select-tree-title">Концерты / выставки / экспозиции</span></span></li><li class="ant-select-tree-treenode-switcher-close" role="treeitem"><span class="ant-select-tree-switcher ant-select-tree-switcher-noop"></span><span class="ant-select-tree-checkbox"><span class="ant-select-tree-checkbox-inner"></span></span><span title="Мебель для театральных / кино- / видеозалов" class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"><span class="ant-select-tree-title">Мебель для театральных / кино- / видеозалов</span></span></li><li class="ant-select-tree-treenode-switcher-close" role="treeitem"><span class="ant-select-tree-switcher ant-select-tree-switcher-noop"></span><span class="ant-select-tree-checkbox"><span class="ant-select-tree-checkbox-inner"></span></span><span title="Музыкальные инструменты" class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"><span class="ant-select-tree-title">Музыкальные инструменты</span></span></li><li class="ant-select-tree-treenode-switcher-close" role="treeitem"><span class="ant-select-tree-switcher ant-select-tree-switcher-noop"></span><span class="ant-select-tree-checkbox"><span class="ant-select-tree-checkbox-inner"></span></span><span title="Оборудование для театральных / кино- / видеозалов" class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"><span class="ant-select-tree-title">Оборудование для театральных / кино- / видеозалов</span></span></li><li class="ant-select-tree-treenode-switcher-close" role="treeitem"><span class="ant-select-tree-switcher ant-select-tree-switcher-noop"></span><span class="ant-select-tree-checkbox"><span class="ant-select-tree-checkbox-inner"></span></span><span title="Произведения декоративно-прикладного искусства / реставрация" class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"><span class="ant-select-tree-title">Произведения декоративно-прикладного искусства / реставрация</span></span></li><li class="ant-select-tree-treenode-switcher-close" role="treeitem"><span class="ant-select-tree-switcher ant-select-tree-switcher-noop"></span><span class="ant-select-tree-checkbox"><span class="ant-select-tree-checkbox-inner"></span></span><span title="Произведения изобразительного искусства / реставрация" class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"><span class="ant-select-tree-title">Произведения изобразительного искусства / реставрация</span></span></li><li class="ant-select-tree-treenode-switcher-close" role="treeitem"><span class="ant-select-tree-switcher ant-select-tree-switcher-noop"></span><span class="ant-select-tree-checkbox"><span class="ant-select-tree-checkbox-inner"></span></span><span title="Сувениры / государственная атрибутика / награды / знаки отличия" class="ant-select-tree-node-content-wrapper ant-select-tree-node-content-wrapper-normal"><span class="ant-select-tree-title">Сувениры / государственная атрибутика / награды / знаки отличия</span></span></li></ul>
"""
"""
календарь
<div class="ant-calendar-picker-container ant-calendar-picker-container-placement-bottomLeft"
style="left: 48px; top: 510px;">
<div class="ant-calendar-time ant-calendar-range-with-ranges ant-calendar ant-calendar-range"
tabindex="0"><div class="ant-calendar-panel"><div class="ant-calendar-date-panel">
<div class="ant-calendar-range-part ant-calendar-range-left">
<div class="ant-calendar-input-wrap">
<div class="ant-calendar-date-input-wrap">
<input class="ant-calendar-input " placeholder="Начальная дата" value="01.11.2023 00:00">
</div></div><div style="outline: none;">
<div class="ant-calendar-header">
<div style="position: relative;">
<a class="ant-calendar-prev-year-btn" role="button" title="Предыдущий год (Control + left)"></a><a class="ant-calendar-prev-month-btn" role="button" title="Предыдущий месяц (PageUp)"></a><span class="ant-calendar-my-select"><a class="ant-calendar-month-select" role="button" title="Выбрать месяц">нояб.</a><a class="ant-calendar-year-select" role="button" title="Выбрать год">2023</a></span></div></div><div class="ant-calendar-body"><table class="ant-calendar-table" cellspacing="0" role="grid"><thead><tr role="row"><th role="columnheader" title="пн" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">пн</span></th><th role="columnheader" title="вт" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">вт</span></th><th role="columnheader" title="ср" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">ср</span></th><th role="columnheader" title="чт" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">чт</span></th><th role="columnheader" title="пт" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">пт</span></th><th role="columnheader" title="сб" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">сб</span></th><th role="columnheader" title="вс" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">вс</span></th></tr></thead><tbody class="ant-calendar-tbody"><tr role="row" class="ant-calendar-active-week"><td role="gridcell" title="30 октября 2023 г." class="ant-calendar-cell ant-calendar-last-month-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">30</div></td><td role="gridcell" title="31 октября 2023 г." class="ant-calendar-cell ant-calendar-last-month-cell ant-calendar-last-day-of-month"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">31</div></td><td role="gridcell" title="1 ноября 2023 г." class="ant-calendar-cell ant-calendar-selected-start-date ant-calendar-selected-day"><div class="ant-calendar-date" aria-selected="true" aria-disabled="false">1</div></td><td role="gridcell" title="2 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">2</div></td><td role="gridcell" title="3 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">3</div></td><td role="gridcell" title="4 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">4</div></td><td role="gridcell" title="5 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">5</div></td></tr><tr role="row" class=""><td role="gridcell" title="6 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">6</div></td><td role="gridcell" title="7 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">7</div></td><td role="gridcell" title="8 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">8</div></td><td role="gridcell" title="9 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">9</div></td><td role="gridcell" title="10 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">10</div></td><td role="gridcell" title="11 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">11</div></td><td role="gridcell" title="12 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">12</div></td></tr><tr role="row" class=""><td role="gridcell" title="13 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">13</div></td><td role="gridcell" title="14 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">14</div></td><td role="gridcell" title="15 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">15</div></td><td role="gridcell" title="16 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">16</div></td><td role="gridcell" title="17 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">17</div></td><td role="gridcell" title="18 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">18</div></td><td role="gridcell" title="19 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">19</div></td></tr><tr role="row" class=""><td role="gridcell" title="20 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">20</div></td><td role="gridcell" title="21 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">21</div></td><td role="gridcell" title="22 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">22</div></td><td role="gridcell" title="23 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">23</div></td><td role="gridcell" title="24 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">24</div></td><td role="gridcell" title="25 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">25</div></td><td role="gridcell" title="26 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">26</div></td></tr><tr role="row" class="ant-calendar-current-week ant-calendar-active-week"><td role="gridcell" title="27 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">27</div></td><td role="gridcell" title="28 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">28</div></td><td role="gridcell" title="29 ноября 2023 г." class="ant-calendar-cell ant-calendar-in-range-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">29</div></td><td role="gridcell" title="30 ноября 2023 г." class="ant-calendar-cell ant-calendar-selected-end-date ant-calendar-last-day-of-month ant-calendar-selected-day"><div class="ant-calendar-date" aria-selected="true" aria-disabled="false">30</div></td><td role="gridcell" title="1 декабря 2023 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">1</div></td><td role="gridcell" title="2 декабря 2023 г." class="ant-calendar-cell ant-calendar-today ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">2</div></td><td role="gridcell" title="3 декабря 2023 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">3</div></td></tr><tr role="row" class=""><td role="gridcell" title="4 декабря 2023 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">4</div></td><td role="gridcell" title="5 декабря 2023 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">5</div></td><td role="gridcell" title="6 декабря 2023 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">6</div></td><td role="gridcell" title="7 декабря 2023 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">7</div></td><td role="gridcell" title="8 декабря 2023 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">8</div></td><td role="gridcell" title="9 декабря 2023 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">9</div></td><td role="gridcell" title="10 декабря 2023 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">10</div></td></tr></tbody></table></div></div></div><span class="ant-calendar-range-middle">-</span><div class="ant-calendar-range-part ant-calendar-range-right"><div class="ant-calendar-input-wrap">
<div class="ant-calendar-date-input-wrap">
<input class="ant-calendar-input " placeholder="Конечная дата" value="30.11.2023 23:59">
</div></div><div style="outline: none;"><div class="ant-calendar-header"><div style="position: relative;"><span class="ant-calendar-my-select"><a class="ant-calendar-month-select" role="button" title="Выбрать месяц">дек.</a><a class="ant-calendar-year-select" role="button" title="Выбрать год">2023</a></span><a class="ant-calendar-next-month-btn" title="Следующий месяц (PageDown)"></a><a class="ant-calendar-next-year-btn" title="Следующий год (Control + right)"></a></div></div><div class="ant-calendar-body"><table class="ant-calendar-table" cellspacing="0" role="grid"><thead><tr role="row"><th role="columnheader" title="пн" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">пн</span></th><th role="columnheader" title="вт" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">вт</span></th><th role="columnheader" title="ср" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">ср</span></th><th role="columnheader" title="чт" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">чт</span></th><th role="columnheader" title="пт" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">пт</span></th><th role="columnheader" title="сб" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">сб</span></th><th role="columnheader" title="вс" class="ant-calendar-column-header"><span class="ant-calendar-column-header-inner">вс</span></th></tr></thead><tbody class="ant-calendar-tbody"><tr role="row" class="ant-calendar-current-week"><td role="gridcell" title="27 ноября 2023 г." class="ant-calendar-cell ant-calendar-last-month-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">27</div></td><td role="gridcell" title="28 ноября 2023 г." class="ant-calendar-cell ant-calendar-last-month-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">28</div></td><td role="gridcell" title="29 ноября 2023 г." class="ant-calendar-cell ant-calendar-last-month-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">29</div></td><td role="gridcell" title="30 ноября 2023 г." class="ant-calendar-cell ant-calendar-last-month-cell ant-calendar-last-day-of-month"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">30</div></td><td role="gridcell" title="1 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">1</div></td><td role="gridcell" title="2 декабря 2023 г." class="ant-calendar-cell ant-calendar-today"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">2</div></td><td role="gridcell" title="3 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">3</div></td></tr><tr role="row" class=""><td role="gridcell" title="4 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">4</div></td><td role="gridcell" title="5 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">5</div></td><td role="gridcell" title="6 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">6</div></td><td role="gridcell" title="7 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">7</div></td><td role="gridcell" title="8 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">8</div></td><td role="gridcell" title="9 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">9</div></td><td role="gridcell" title="10 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">10</div></td></tr><tr role="row" class=""><td role="gridcell" title="11 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">11</div></td><td role="gridcell" title="12 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">12</div></td><td role="gridcell" title="13 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">13</div></td><td role="gridcell" title="14 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">14</div></td><td role="gridcell" title="15 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">15</div></td><td role="gridcell" title="16 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">16</div></td><td role="gridcell" title="17 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">17</div></td></tr><tr role="row" class=""><td role="gridcell" title="18 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">18</div></td><td role="gridcell" title="19 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">19</div></td><td role="gridcell" title="20 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">20</div></td><td role="gridcell" title="21 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">21</div></td><td role="gridcell" title="22 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">22</div></td><td role="gridcell" title="23 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">23</div></td><td role="gridcell" title="24 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">24</div></td></tr><tr role="row" class=""><td role="gridcell" title="25 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">25</div></td><td role="gridcell" title="26 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">26</div></td><td role="gridcell" title="27 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">27</div></td><td role="gridcell" title="28 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">28</div></td><td role="gridcell" title="29 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">29</div></td><td role="gridcell" title="30 декабря 2023 г." class="ant-calendar-cell"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">30</div></td><td role="gridcell" title="31 декабря 2023 г." class="ant-calendar-cell ant-calendar-last-day-of-month"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">31</div></td></tr><tr role="row" class=""><td role="gridcell" title="1 января 2024 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">1</div></td><td role="gridcell" title="2 января 2024 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">2</div></td><td role="gridcell" title="3 января 2024 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">3</div></td><td role="gridcell" title="4 января 2024 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">4</div></td><td role="gridcell" title="5 января 2024 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">5</div></td><td role="gridcell" title="6 января 2024 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">6</div></td><td role="gridcell" title="7 января 2024 г." class="ant-calendar-cell ant-calendar-next-month-btn-day"><div class="ant-calendar-date" aria-selected="false" aria-disabled="false">7</div></td></tr></tbody></table></div></div></div></div><div class="ant-calendar-footer ant-calendar-range-bottom ant-calendar-footer-show-ok"><div class="ant-calendar-footer-btn"><div class="ant-calendar-footer-extra ant-calendar-range-quick-selector"><span class="ant-tag ant-tag-blue">1 день</span><span class="ant-tag ant-tag-blue">3 дня</span><span class="ant-tag ant-tag-blue">1 неделя</span><span class="ant-tag ant-tag-blue">2 недели</span><span class="ant-tag ant-tag-blue">1 месяц</span><span class="ant-tag ant-tag-blue">Прошлый месяц</span></div><a class="ant-calendar-time-picker-btn" role="button">Выбрать время</a><a class="ant-calendar-ok-btn" role="button">Ok</a></div></div></div></div></div>
"""
"""
пустой календарь
<div style="position: absolute; top: 0px; left: 0px; width: 100%;"><div><div class="ant-dropdown  ant-dropdown-placement-bottomRight  ant-dropdown-hidden"><div class="ant-table-filter-dropdown"><div style="padding: 8px;"><span class="ant-calendar-picker" tabindex="0" style="margin-bottom: 8px; display: block;"><span class="ant-calendar-picker-input ant-input"><input readonly="" placeholder="Начальная дата" class="ant-calendar-range-picker-input" tabindex="-1" value=""><span class="ant-calendar-range-picker-separator"> - </span><input readonly="" placeholder="Конечная дата" class="ant-calendar-range-picker-input" tabindex="-1" value=""><i aria-label="icon: calendar" class="anticon anticon-calendar ant-calendar-picker-icon"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="calendar" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M880 184H712v-64c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H384v-64c0-4.4-3.6-8-8-8h-56c-4.4 0-8 3.6-8 8v64H144c-17.7 0-32 14.3-32 32v664c0 17.7 14.3 32 32 32h736c17.7 0 32-14.3 32-32V216c0-17.7-14.3-32-32-32zm-40 656H184V460h656v380zM184 392V256h128v48c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8v-48h256v48c0 4.4 3.6 8 8 8h56c4.4 0 8-3.6 8-8v-48h128v136H184z"></path></svg></i></span></span><button type="button" class="ant-btn ant-btn-primary ant-btn-sm" style="width: 90px; margin-right: 8px;"><i aria-label="icon: search" class="anticon anticon-search"><svg viewBox="64 64 896 896" focusable="false" class="" data-icon="search" width="1em" height="1em" fill="currentColor" aria-hidden="true"><path d="M909.6 854.5L649.9 594.8C690.2 542.7 712 479 712 412c0-80.2-31.3-155.4-87.9-212.1-56.6-56.7-132-87.9-212.1-87.9s-155.5 31.3-212.1 87.9C143.2 256.5 112 331.8 112 412c0 80.1 31.3 155.5 87.9 212.1C256.5 680.8 331.8 712 412 712c67 0 130.6-21.8 182.7-62l259.7 259.6a8.2 8.2 0 0 0 11.6 0l43.6-43.5a8.2 8.2 0 0 0 0-11.6zM570.4 570.4C528 612.7 471.8 636 412 636s-116-23.3-158.4-65.6C211.3 528 188 471.8 188 412s23.3-116.1 65.6-158.4C296 211.3 352.2 188 412 188s116.1 23.2 158.4 65.6S636 352.2 636 412s-23.3 116.1-65.6 158.4z"></path></svg></i><span>Поиск</span></button><button type="button" class="ant-btn ant-btn-sm" style="width: 90px;"><span>Сбросить</span></button></div></div></div></div></div>
"""