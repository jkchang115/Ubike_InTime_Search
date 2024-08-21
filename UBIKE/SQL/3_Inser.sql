-- Insert 資料練習
INSERT INTO Station (
    sno, sna, sarea, latitude, longitude, ar, sareaen, snaen, aren
) VALUES (
    '500119084', 
    'YouBike2.0_臺大鄭江樓北側', 
    '臺大公館校區', 
    25.01854, 
    121.54309, 
    '臺大鄭江樓東南側', 
    'NTU Dist', 
    'YouBike2.0_NTU Tseng Jiang Hall(North)', 
    'NTU Graduate Institute of Journalism(South)'
);

INSERT INTO StationData (
    sno, total, available_rent_bikes, available_return_bikes, act, mday, srcUpdateTime, updateTime, infoTime, infoDate
) VALUES (
    '500119084', 
    40, 
    35, 
    0, 
    1, 
    '2024-08-12 10:15:16', 
    '2024-08-12 10:20:29', 
    '2024-08-12 10:20:49', 
    '2024-08-12 10:15:16', 
    '2024-08-12'
);
GO
