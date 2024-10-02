import folium   # folium을 호출
from buildingList import building # 외부파일 buildingList 로부터 클래스 building 호출
               
center = [36.908, 127.143619452225] # 남서울대학교의 [위도, 경도] 불러오는 함수
m = folium.Map(location=center, zoom_start=15.5) # m 변수 지정, 남서울대학교, 화면 해상도 15.5

for mark in markinglist:    # 리스트에 저장된 마킹 추가
    mark.add_to(m)

m # 지도 출력




    