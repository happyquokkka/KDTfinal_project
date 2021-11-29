var mapContainer = document.getElementById('map'), // 지도의 중심좌표
    mapOption = {
        center: new kakao.maps.LatLng(33.32141, 126.3148), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다
// 지도를 생성한다
var map = new kakao.maps.Map(mapContainer, mapOption);

// 지도 타입 변경 컨트롤을 생성한다
var mapTypeControl = new kakao.maps.MapTypeControl();

// 지도의 상단 우측에 지도 타입 변경 컨트롤을 추가한다
map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

// 지도에 확대 축소 컨트롤을 생성한다
var zoomControl = new kakao.maps.ZoomControl();

// 지도의 우측에 확대 축소 컨트롤을 추가한다
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);





// 지도에 마커를 표시합니다
var marker1 = new kakao.maps.Marker({
    map: map,
    position: new kakao.maps.LatLng(33.4471343,126.3057656)
});

var marker2 = new daum.maps.Marker({
    map: map,
    position: new daum.maps.LatLng(33.4659677, 126.3206294)
});

var marker3 = new daum.maps.Marker({
    map: map,
    position: new daum.maps.LatLng(33.4718805, 126.3681801)
});

var marker4 = new daum.maps.Marker({
    map: map,
    position: new daum.maps.LatLng(33.4725624, 126.4093289)
});

var marker5 = new daum.maps.Marker({
    map: map,
    position: new daum.maps.LatLng(33.4478775, 126.3012418)
});

var marker6 = new daum.maps.Marker({
    map: map,
    position: new daum.maps.LatLng(33.4659319, 126.3192857)
});

var marker7 = new daum.maps.Marker({
    map: map,
    position: new daum.maps.LatLng(33.4800276, 126.4012957)
});

var marker8 = new daum.maps.Marker({
    map: map,
    position: new daum.maps.LatLng(33.4683238, 126.3401314)
});
var marker9 = new daum.maps.Marker({
    map: map,
    position: new daum.maps.LatLng(33.4601827, 126.4339961)
});
var marker10 = new daum.maps.Marker({
    map: map,
    position: new daum.maps.LatLng(33.4487544,126.307815)
});