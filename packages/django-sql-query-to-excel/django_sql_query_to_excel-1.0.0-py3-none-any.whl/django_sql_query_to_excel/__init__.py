
import xlsxwriter
import io
from django.db.utils import OperationalError
from django.db import connection
from django.http import HttpResponse
import traceback



class SqlQueryToExcel:
    @classmethod
    def query_to_excel(cls, query, worksheet_name=None, custom_header=None, color=None):
        try:
            output = io.BytesIO()
            cursor = connection.cursor()
            cursor.execute(query)
                
            header = [row[0] for row in cursor.description]
            if custom_header:
                header = custom_header
            rows = cursor.fetchall()
                # Create an new Excel file and add a worksheet.
            workbook = xlsxwriter.Workbook(output)
            worksheet = workbook.add_worksheet(worksheet_name if worksheet_name else 'output')

            # Create style for cells
            header_cell_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': 'yellow'})
            body_cell_format = workbook.add_format({'border': True})

            # header, rows = fetch_table_data(table_name)

            row_index = 0
            column_index = 0
            # if not custom_header:
            for column_name in header:
                # print('col_name', column_name)
                worksheet.write(row_index, column_index, column_name, header_cell_format)
                column_index += 1

            row_index += 1
            for row in rows:
                column_index = 0
                for column in row:
                    worksheet.write(row_index, column_index, column, body_cell_format)
                    column_index += 1
                row_index += 1

            # Closing workbook
            workbook.close()
            output.seek(0)
            response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            return response
        except OperationalError as err:
            print(f"{traceback.format_exc()}")
        except Exception as err:
            print(f"{traceback.format_exc()}")