
from sql_query_to_excel import SqlQueryToExcel

class InitTest:
    def test_sql_query(self):
        query_string = f""" select 1 """
        assert SqlQueryToExcel.query_to_excel(query_string)

