import pymysql
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

class MySQLConnector:
    def __init__(self, host, port, user, password, database):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, sql, params=None):
        # 无需主动关闭，每次定期链接
        self.connection.ping(reconnect=True)
        self.cursor.execute(sql, params)
    
        result = self.cursor.fetchall()
        return result

    def execute_update(self, sql, params=None):
        self.connection.ping(reconnect=True)
        self.cursor.execute(sql, params)
        self.connection.commit()
        return self.cursor.rowcount
    def create_database_if_not_exists(self, sql):
        self.connection.ping(reconnect=True)
        self.cursor.execute(sql)

# 创建 MySQL 连接器对象
connector = MySQLConnector(
    host     = MYSQL_HOST,
    port     = MYSQL_PORT,
    user     = MYSQL_USER,
    password = MYSQL_PASSWORD,
    database = MYSQL_DATABASE
)
