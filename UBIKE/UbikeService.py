# MVC設計模式(Model/View/Controller)
from models import createConnection
import math
from flask import Flask
import UbikeQuery as ubike
import json
from flask import render_template
from flask import Response,request
import urllib.parse
import requests
# from SQLServerDemo import app

# 建構Flask物件
app = Flask(__name__)

# 首頁 程序...調用page (xxx.html)

# 定義函數 類似Controller(控制流程)
# 沒有對外地圖配置到這一個功能 route路由配置 (端點)
# 外掛擴充功能decorator 裝飾
@app.route('/')
def index():
    # 可以有一些使用者端互動 進行控制用流程
    # 直接調用一個View(html page)結合Model jinja2 template
    # 頁面放py file所在位置下的一個templates 資料夾下
    return render_template('home.html')

# 定義一個服務端點 動態路由配置
@app.route('/ubike/query/<area>/rawdata')
def ubikeSelect(area):    # 呼叫自訂Modules動態查詢結果DataFrame
    data = []
    df = ubike.areaFind(area)
    # df.to_csv('c:/data/bike1.csv', encoding='utf-8-sig')

    # 走訪每一筆 採用row number
    # SINCE int64 是 NumPy 的數據類型，而不是 Python 原生的數據類型，json.dumps() 函數無法直接序列化這些數據類型。
    for row in range(len(df)):
        rec = {
            'index': int(df['sno'].get(row)),
            'area': str(df['sarea'].get(row)),
            'location': str(df['ar'].get(row)),
            'freetotal': int(df['available_rent_bikes'].get(row)),
            'inoutfree': int(df['available_return_bikes'].get(row)),
            'time': str(df['mday'].get(row))
        }
        data.append(rec)

    # 序列化成json
    jstr = json.dumps(data)
    response = Response(jstr, content_type='application/json') 
    return response

# 計算兩個經緯度之間的距離（返回單位：米）
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371000  # 地球半徑，單位：米
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

@app.route('/search', methods=['POST'])
def search():
    lat = float(request.form['latitude'])
    lon = float(request.form['longitude'])
    
    conn = createConnection()
    cursor = conn.cursor(as_dict=True)
    
    # 查詢所有 YouBike 站點資料，包括可借車輛數量及可停車輛數量
    cursor.execute("""
        WITH LatestData AS (
            SELECT 
                sno,
                available_rent_bikes,
                available_return_bikes,
                updateTime,
                ROW_NUMBER() OVER (PARTITION BY sno ORDER BY updateTime DESC) AS rn
            FROM StationData
        )
        SELECT 
            s.sno, 
            s.sna, 
            s.latitude, 
            s.longitude, 
            s.ar,
            ld.available_rent_bikes, 
            ld.available_return_bikes,
            ld.updateTime
        FROM Station s
        JOIN LatestData ld ON s.sno = ld.sno
        WHERE ld.rn = 1
    """)
    stations = cursor.fetchall()

    # 篩選出距離選擇位置200米以內的站點
    nearby_stations = []
    for station in stations:
        station_lat = station['latitude']
        station_lon = station['longitude']
        # station_ar = station['ar']
        distance = calculate_distance(lat, lon, station_lat, station_lon)
        if distance <= 200:
            station['distance'] = format(distance, '.2f')
            nearby_stations.append(station)
    
    conn.close()
    
    return render_template('results.html', stations=nearby_stations)

if __name__ == '__main__':
    app.run(debug=True)
    # 從 API 獲取最新的 YouBike 資料

