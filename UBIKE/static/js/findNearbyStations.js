function findNearbyStations() {
    // 確認瀏覽器是否支援地理定位
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            // 獲取用戶的經緯度
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            
            // 發送請求到後端以獲取附近的 YouBike 站點
            fetch(`/nearby?lat=${latitude}&lng=${longitude}`)
                .then(response => response.json())
                .then(data => {
                    // 清空之前的結果
                    let resultsDiv = document.getElementById('results');
                    resultsDiv.innerHTML = '';

                    if (data.length > 0) {
                        // 顯示每個站點的信息
                        data.forEach(station => {
                            resultsDiv.innerHTML += `<p>站點名稱: ${station.sna}, 地址: ${station.ar}, 可租借: ${station.available_rent_bikes}, 可歸還: ${station.available_return_bikes}</p>`;
                        });
                    } else {
                        resultsDiv.innerHTML = '<p>附近沒有找到站點。</p>';
                    }
                })
                .catch(error => {
                    console.error('Error fetching data:', error);
                    let resultsDiv = document.getElementById('results');
                    resultsDiv.innerHTML = '<p>無法獲取站點信息。</p>';
                });
        }, function(error) {
            console.error('Error getting location:', error);
            alert('無法獲取您的位置，請確保您的瀏覽器允許地理定位。');
        });
    } else {
        alert("瀏覽器不支援地理定位功能。");
    }
}
