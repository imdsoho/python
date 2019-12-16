from functools import wraps

class DBDriver:
    def __init__(self, dbstring):
        print("-3-")
        self.dbstring = dbstring

    def execute(self, query):
        print("-5-")
        return f"{self.dbstring} 에서 쿼리 {query} 실행"

def inject_db_driver(function):
    print("-1-")
    @wraps(function)
    def wrapped(dbstring):
        print("-2- : ", function.__qualname__)
        # 함수의 서명을 변경 - 파라미터가 어떻게 처리되고, 치환되는지 캡슐화한다.
        return function(DBDriver(dbstring))

    return wrapped

@inject_db_driver
def run_query(driver):
    print("-4-")
    return driver.execute("query_statement")


data = run_query("mysql_driver")
print(data)
