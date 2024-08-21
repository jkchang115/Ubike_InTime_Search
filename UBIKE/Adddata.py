import requests
import time
from datetime import datetime
from models import createConnection

def fetch_youbike_data():
    url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
   
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # 將資料插入資料庫
        save_to_db(data)
    else:
        print("獲取資料失敗，狀態碼:", response.status_code)

def save_to_db(data):
    # 建立資料庫連接
    conn = createConnection()
    cursor = conn.cursor()
    
    # 準備插入 Station 的 SQL 語句
    insert_station_query = """
    INSERT INTO Station (sno, sna, sarea, latitude, longitude, ar, sareaen, snaen, aren)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # 準備插入 StationData 的 SQL 語句
    insert_data_query = """
    INSERT INTO StationData (sno, total, available_rent_bikes, available_return_bikes, act, mday, srcUpdateTime, updateTime, infoTime, infoDate)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    for station in data:
        sno = station['sno']
        
        # 檢查該 sno 是否已存在於 Station 表中
        cursor.execute("SELECT 1 FROM Station WHERE sno = %s", (sno,))
        if cursor.fetchone() is None:
            # 如果 sno 不存在，插入新的 Station 記錄
            sna = station['sna']
            sarea = station['sarea']
            latitude = station['latitude']
            longitude = station['longitude']
            ar = station['ar']
            sareaen = station['sareaen']
            snaen = station['snaen']
            aren = station['aren']
            
            cursor.execute(insert_station_query, (sno, sna, sarea, latitude, longitude, ar, sareaen, snaen, aren))
        
        # 插入 StationData 資料
        total = station['total']
        available_rent_bikes = station['available_rent_bikes']
        available_return_bikes = station['available_return_bikes']
        act = station['act']
        mday = datetime.strptime(station['mday'], '%Y-%m-%d %H:%M:%S')
        srcUpdateTime = datetime.strptime(station['srcUpdateTime'], '%Y-%m-%d %H:%M:%S')
        updateTime = datetime.strptime(station['updateTime'], '%Y-%m-%d %H:%M:%S')
        infoTime = datetime.strptime(station['infoTime'], '%Y-%m-%d %H:%M:%S')
        infoDate = datetime.strptime(station['infoDate'], '%Y-%m-%d')
        
        cursor.execute(insert_data_query, (sno, total, available_rent_bikes, available_return_bikes, act, mday, srcUpdateTime, updateTime, infoTime, infoDate))
    
    # 提交變更
    conn.commit()
    
    # 關閉連接
    cursor.close()
    conn.close()
    
    print(f"成功處理 {len(data)} 筆資料")
# next step is to 
if __name__ == "__main__":
    count = 1
    while count<=1:
         # 每 1 分鐘呼叫一次
        fetch_youbike_data()
        count += 1
        # time.sleep(20) 
        
