USE YouBike2DB;
GO

CREATE TABLE Station (
    sno NVARCHAR(20) PRIMARY KEY, -- ���I�N��
    sna NVARCHAR(100),            -- ��������W��
    sarea NVARCHAR(50),           -- �����ϰ�
    latitude FLOAT,               -- �n��
    longitude FLOAT,              -- �g��
    ar NVARCHAR(200),             -- �a�I
    sareaen NVARCHAR(50),         -- �����ϰ�^��
    snaen NVARCHAR(100),          -- �����W�٭^��
    aren NVARCHAR(200)            -- �a�}�^��
);
GO

CREATE TABLE StationData (
    dataID INT PRIMARY KEY IDENTITY(1,1), -- �ۼW�D��
    sno NVARCHAR(20) FOREIGN KEY REFERENCES Station(sno), -- �~��A�Ѧ� Station ��
    total INT,                      -- �����`������
    available_rent_bikes INT,       -- �����ثe�����ƶq
    available_return_bikes INT,     -- �Ŧ�ƶq
    act BIT,                        -- �����T�Ϊ��A
    mday DATETIME,                  -- ��Ƨ�s�ɶ�
    srcUpdateTime DATETIME,         -- YouBike2.0�t�εo����Ƨ�s���ɶ�
    updateTime DATETIME,            -- �j�ƾڥ��x�g�L�B�z��N��Ʀs�JDB���ɶ�
    infoTime DATETIME,              -- �U�����ӷ���Ƨ�s�ɶ�
    infoDate DATE,                  -- �U�����ӷ���Ƨ�s���
    timestamp DATETIME DEFAULT GETDATE() -- ���J��ƪ��ɶ��W�O�A�w�]�Ȭ���e�ɶ�
);
GO

