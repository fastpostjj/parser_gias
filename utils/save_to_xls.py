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

