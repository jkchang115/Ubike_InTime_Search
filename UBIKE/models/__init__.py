# gloabal
# 引用 flask class
from flask import Flask
import pymssql
# 設定 global variable flask instance 個體物件
# 沒有客製化 Flask網站系統static file 跟樣板引擎路徑 template_folder,
# 預設 static and templates folder
# 建立 Application 物件(可以設定靜態檔案的路徑處理) 預設 static_folder='static',static_path='/static'
app = Flask('__main__')  # don't use system variable __name__

# 配置資料庫連接相關配置
SERVER='localhost'
DATABASE='YouBike2DB'
USERNAME='sa'
PASSWORD='0972779027'
APPICATION_NAME='acct'

# 自訂函數 配合連接組態 產生connection object
def createConnection():
    # use pymssql to generate a connection object
    # setting application name , goal: to use SQL Server Profiler進行Trace(用在效能調校)
    # 可能連接與開啟失敗(SQL SERVER 拋出例外)
    try:
        conn = pymssql.connect(server=SERVER, user=USERNAME, password=PASSWORD, database=DATABASE,appname=APPICATION_NAME)
    except Exception as ex:
        #不須回應UI Q; 拋出例外
        # TODO  自訂程序進行稽核 產生LOGGING
        raise Exception('資料庫連接失敗')
    return conn


# 網站配置端點 URL Routing(配置模組 Controller)
# import models.customerscontroller
# import models.cateproductscontroller