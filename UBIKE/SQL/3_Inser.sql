-- Insert ��ƽm��
INSERT INTO Station (
    sno, sna, sarea, latitude, longitude, ar, sareaen, snaen, aren
) VALUES (
    '500119084', 
    'YouBike2.0_�O�j�G���ӥ_��', 
    '�O�j���]�հ�', 
    25.01854, 
    121.54309, 
    '�O�j�G���ӪF�n��', 
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
