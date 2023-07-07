# 数据定时录入 (python-sync-data-to-mysql)

> 通过 `schedule` 实现定时任务，利用 `threading` 实现多线程，定期执行 `task` 任务逻辑，将数据利用 `pymysql` 导入数据库


## Prev

```shell
# python --version
Python 3.8.17
# pip --version
pip 23.0.1 from (python 3.8)
```

## Run

- 第一步：pip

```shell
pip install pymysql
pip install schedule
```

- 第二步：config

```shell
# vim config.py

# MySQL 数据库配置 （修改成您自己的配置）
MYSQL_HOST     = 'mysql'
MYSQL_PORT     = 3306
MYSQL_USER     = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DATABASE = 'study_sync_data'
```

- 第三步：mysql 
  - 手动创建库表 [`create_table`](./docs/sql/create_table.sql)
  - 自动创建库表 `python ./init.py`

- 第四步：py

```shell
python ./main.py
```


## DIR

```
├─database 【数据库连接】
│  └─mysql_connector.py
├─docs 【文档】
│  └─sql
├─models 【模型】
│  └─category.py
├─tasks 【任务】
│  └─category.py
|─utils 【工具类】
│  └─thread.py
└─config.py 【配置】
└─main.py 【入口文件】
```



