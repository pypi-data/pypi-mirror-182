# python raw sql to excel using XlsrWriter



## Basic Usage
In any View 
import example:

from django_sql_query_to_excel import SqlQueryToExcel

def somefunc_view(): #any view , apiview , view etc
    sql_query = "" #define your sql as show below
    """
        for orm , convert your objects to string queries , 
        sql_query = obj.query.__str__() 
        or simple raw query:
        sql_query = f""" 
                select * from yourtable
            """"

    """
    
    return SqlQueryToExcel.query_to_excel(sql_query) 
    """return to get your response result"""




## Installation

```shell
$ pip install django-sql-query-to-excel
```

## Documentation

"refer basic usage"

## Contribution
Please send your PR 