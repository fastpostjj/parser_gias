import xlwt
import os


def save_xslx(filename_xls='tab.xlsx', data=[]):
    # Сохранение в файл
    if data:
        if os.path.isfile(filename_xls):
            os.remove(filename_xls)
        wb = xlwt.Workbook()
        ws = wb.add_sheet('sheet')

        # Создаем объект стиля ячейки
        style_bold = xlwt.XFStyle()

        # Создаем объект шрифта
        font = xlwt.Font()
        font.name = 'Arial'
        font.bold = True
        font.underline = True
        # Задаем цвет шрифта
        font.colour_index = xlwt.Style.colour_map['black']

        # Применяем шрифт к стилю
        style_bold.font = font

        # Задаем формат числовой ячейки
        numeric_style = xlwt.XFStyle()
        # numeric_style.num_format_str = '0.00'
        # Задаем формат числовой ячейки с разделителем тысяч
        numeric_style.num_format_str = '#,##0.00'

        # Задаем формат числовой ячейки
        numeric_style_int = xlwt.XFStyle()
        numeric_style_int.num_format_str = '0'

        style_alignment = xlwt.XFStyle()
        style_alignment.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT

        style_date = xlwt.XFStyle()

        # Задаем формат даты для ячейки
        style_date.num_format_str = 'DD-MM-YYYY'  # Формат даты: день-месяц-год

        # Формат для гиперссылки
        hyperlink_style = xlwt.easyxf('font: underline single, color blue;')
        hyperlink_style.alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT

        counter_row = 0

        # Записываем заголовки
        ws.write(0, 0, 'Предмет закупки', style_bold)
        # Устанавливаем автоширину для ячейки
        # 256 - ширина колонки по умолчанию
        ws.col(0).width = 256 * 2 * len('Предмет закупки')

        ws.write(
            0,
            1,
            'Наименование заказчика/организатора закупки',
            style_bold
            )
        ws.col(1).width = 256 * len(
            'Наименование заказчика/организатора закупки'
            )

        ws.write(0, 2, 'Место нахождения заказчика/организатора', style_bold)
        ws.col(2).width = 256 * len('Место нахождения заказчика/организатора')

        ws.write(0, 3, 'Номер', style_bold)
        ws.write(0, 4, 'Ориентировочная стоимость', style_bold)
        ws.write(0, 5, 'Дата окончания приема предложений', style_bold)
        ws.write(0, 6, 'Время подачи', style_bold)
        ws.write(0, 7, 'Тип закупки', style_bold)
        ws.write(0, 8, 'Дата размещения', style_bold)
        for data_row in data:
            counter_row += 1
            if 'title' in data_row:
                if 'url' in data_row:
                    # Добавляем гиперссылку в ячейку
                    click = data_row["url"]
                    name = data_row["title"]
                    ws.write(counter_row, 0, xlwt.Formula(
                        f'HYPERLINK("%s";"{name}")' % click),
                        hyperlink_style
                        )
                else:
                    ws.write(counter_row, 0, data_row['title'])

            if 'name' in data_row:
                ws.write(counter_row, 1, data_row['name'], style_alignment)
            if 'adress' in data_row:
                ws.write(counter_row, 2, data_row['adress'], style_alignment)
            if 'number' in data_row:
                ws.write(counter_row, 3, data_row['number'], numeric_style_int)
            if 'amount' in data_row:
                ws.write(counter_row, 4, data_row['amount'], numeric_style)
            if 'date_before' in data_row:
                ws.write(counter_row, 5, data_row['date_before'], style_date)
            if 'procedure_type' in data_row:
                ws.write(counter_row, 7, data_row['procedure_type'])
            if 'data_posting' in data_row:
                ws.write(
                    counter_row,
                    8,
                    data_row['data_posting'][0:10],
                    style_date
                    )
        try:
            wb.save(filename_xls)
            return data
        except Exception as error:
            print("Ошибка сохранения в файл:", error)


if __name__ == "__main__":
    data = [
        {'url': 'https://gias.by/gias/#/purchase/current/a6e0b5c9-8a68-4779-bfa5-195db44e2b32', 'title': 'Закупка медицинских расходников', 'name': 'Войсковая часть 02102', 'adress': '222520, Минская обл., г. Борисов, пр-т Революции 44', 'number': '2549188', 'amount': 1090.00, 'date_before': '11.05.2025', 'data_posting': '08.12.2023 17:39', 'procedure_type': 'Закупка из одного источника'}, {'url': 'https://gias.by/gias/#/purchase/current/bd2f52cb-13c8-436d-bd27-b92480173a24', 'title': 'Перчатки медицинские нестерильные', 'name': 'Государственное учреждение "Республиканский реабилитационный центр для детей-инвалидов"', 'adress': '220049, г. Минск, ул. Севастопольская,56', 'number': '2543864', 'amount': 2145.00, 'date_before': '15.03.1956', 'data_posting': '07.12.2023 14:09', 'procedure_type': 'Закупка из одного источника'}, {'url': 'https://gias.by/gias/#/purchase/current/f36c5880-8a28-43bf-8264-404fae67db41', 'title': 'Перчатки медицинские, контейнеры медицинские', 'name': 'УЗ "13-я городская детская клиническая поликлиника"', 'adress': '220024, г. Минск, ул. Кижеватова, 60, корп. 1', 'number': '2543189', 'amount': 1300.00, 'date_before': '-', 'data_posting': '07.12.2023 11:39', 'procedure_type': 'Закупка из одного источника'}, {'url': 'https://gias.by/gias/#/purchase/current/2619ab08-a2a0-4d0f-8ea7-e7a5e83301a7', 'title': 'Перчатки нитриловые смотровые нестерильные', 'name': 'Учреждение здравоохранения "21-я центральная районная поликлиника Заводского района г. Минска"', 'adress': '220026, г. Минск, ул. Филатова, 13', 'number': '2541987', 'amount': '10 385,00 BYN', 'date_before': '-', 'data_posting': '06.12.2023 18:14', 'procedure_type': 'Закупка из одного источника'}, {'url': 'https://gias.by/gias/#/purchase/current/bd1fec2f-738e-4fc1-9d8d-3c11104c5fde', 'title': 'перчатки диэлектрические', 'name': 'Государственное учреждение "Республиканский научно-практический центр пульмонологии и фтизиатрии"', 'adress': '220053, Минск, Долгиновский тракт, 157', 'number': '2541497', 'amount': '200,00 BYN', 'date_before': '-', 'data_posting': '06.12.2023 16:48', 'procedure_type': 'Закупка из одного источника'}, {'url': 'https://gias.by/gias/#/purchase/current/537b2874-6546-443c-9f8a-a705582fd46c', 'title': 'Дезинфицирующие средства, перчатки', 'name': 'Учреждение "Дрибинский районный центр социального обслуживания населения"', 'adress': '213971, Могилевская обл., г.п. Дрибин, ул. Темнолесская, д. 16', 'number': '2540526', 'amount': '728,86 BYN', 'date_before': '-', 'data_posting': '06.12.2023 14:51', 'procedure_type': 'Закупка из одного источника'}, {'url': 'https://gias.by/gias/#/purchase/current/6c8f5e9b-c9aa-4459-92c5-d48886827d35', 'title': 'Перчатки медицинские одноразовые', 'name': 'Государственное учреждение здравоохранения "Борисовский специализированный дом ребенка"', 'adress': '222512, Минская обл., Борисов, пер. Зеленый, 12', 'number': '2538814', 'amount': '500,00 BYN', 'date_before': '-', 'data_posting': '06.12.2023 09:15', 'procedure_type': 'Закупка из одного источника'}, {'url': 'https://gias.by/gias/#/purchase/current/19dcb9a1-4084-44d9-8cfa-e5be297f340d', 'title': 'перчатки медицинские смотровые', 'name': 'Учреждение "Речицкая районная ветеринарная станция"', 'adress': '247500, Гомельская обл., г. Речица, ул. Набережная, 83', 'number': '2538756', 'amount': '602,52 BYN', 'date_before': '-', 'data_posting': '06.12.2023 09:00', 'procedure_type': 'Закупка из одного источника'}, {'url': 'https://gias.by/gias/#/purchase/current/52b10b1b-3c9b-4dc7-a494-266bf807e91f', 'title': 'Закупка перчаток медицинских (нитриловых)', 'name': 'Государственное учреждение "Территориальный центр социального обслуживания населения Любанского района"', 'adress': '223812, Минская обл., Любань, пер. Полевой, 3', 'number': '2537504', 'amount': '85,00 BYN', 'date_before': '-',
        'data_posting': '05.12.2023 16:01', 'procedure_type': 'Закупка из одного источника'}, {'url': 'https://gias.by/gias/#/purchase/current/4580414f-10db-4719-ac35-644a51158ad3', 'title': 'Перчатки нитриловые', 'name': 'ГУ "Республиканский центр гигиены, эпидемиологии и общественного здоровья"', 'adress': '220099, г. Минск, ул. Казинца, д. 50', 'number': '2536612', 'amount': 1297.00, 'date_before': '-', 'data_posting': '05.12.2023 14:09', 'procedure_type': 'Закупка из одного источника'}
        ]
    save_xslx(filename_xls='test.xlsx', data=data)
