USE YouBike2DB;
GO

CREATE TABLE Station (
    sno NVARCHAR(20) PRIMARY KEY, -- 站點代號
    sna NVARCHAR(100),            -- 場站中文名稱
    sarea NVARCHAR(50),           -- 場站區域
    latitude FLOAT,               -- 緯度
    longitude FLOAT,              -- 經度
    ar NVARCHAR(200),             -- 地點
    sareaen NVARCHAR(50),         -- 場站區域英文
    snaen NVARCHAR(100),          -- 場站名稱英文
    aren NVARCHAR(200)            -- 地址英文
);
GO

CREATE TABLE StationData (
    dataID INT PRIMARY KEY IDENTITY(1,1), -- 自增主鍵
    sno NVARCHAR(20) FOREIGN KEY REFERENCES Station(sno), -- 外鍵，參考 Station 表
    total INT,                      -- 場站總停車格
    available_rent_bikes INT,       -- 場站目前車輛數量
    available_return_bikes INT,     -- 空位數量
    act BIT,                        -- 全站禁用狀態
    mday DATETIME,                  -- 資料更新時間
    srcUpdateTime DATETIME,         -- YouBike2.0系統發布資料更新的時間
    updateTime DATETIME,            -- 大數據平台經過處理後將資料存入DB的時間
    infoTime DATETIME,              -- 各場站來源資料更新時間
    infoDate DATE,                  -- 各場站來源資料更新日期
    timestamp DATETIME DEFAULT GETDATE() -- 插入資料的時間戳記，預設值為當前時間
);
GO

