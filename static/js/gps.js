jQuery(document).ready(function() {

    // 실시간 위치정보를 loc 변수에 저장한 뒤 해당 내용을 web console창에 띄움
    navigator.geolocation.getCurrentPosition(function(position) {
    var lat = position.coords.latitude
    var long = position.coords.longitude;

    console.log(lat, long)
    var state = {"lat": lat, "long": long}

    $("#location").click(function(){
        location.href = "/restaurant/search?latitude="+ lat + "&longitude=" + long

    })
    })
});


    /*
    // 위치정보를 가져오지 못했을 경우 실행되는 함수
    navigator.geolocation.getCurrentPosition(success, function(error) {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                // 사용자가 위치정보 사용을 허용하지 않았을 때
                break;
            case error.POSITION_UNAVAILABLE:
                // 위치 정보 사용이 불가능할 때
                break;
            case error.TIMEOUT:
                // 위치 정보를 가져오려 시도했지만, 시간이 초과되었을 때
                break;
            case error.UNKNOWN_ERROR:
                // 기타 알 수 없는 오류가 발생하였을 때
                break;
            }
    });
*/