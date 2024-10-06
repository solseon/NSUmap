import folium   # folium을 호출

class Building: # 건물 이름, 위치, 마킹 클래스
    def __init__(self, name, location): 
        self.name = name    # 이름변수
        self.location = location    # 위치변수[위도, 경도]
        
    def marking(self, color, icon):   
        return folium.Marker(
            location=self.location,
            popup=self.name,
            icon=folium.Icon(color=color, icon=icon)
        )
        
# 남서울대학교 중심 좌표
center = [36.908, 127.143619452225] 
m = folium.Map(location=center, zoom_start=18)

# 건물 정보 저장
bon = Building("본관", [36.9072014, 127.1430552])
sang = Building("상경학관", [36.90818157832219, 127.14407494870781])
bon1 = Building("본관 앞", [36.90755, 127.1430])
sang1 = Building('상경학관 앞',[36.9081 ,127.14391])
bon_sang = Building('본관-상경 삼거리', [36.9077,127.1440])

# 건물 마킹 리스트 생성
markinglist = list()

# 건물 마킹
markinglist.append(bon.marking("blue", "circle"))
markinglist.append(sang.marking("red", "circle"))

# 마킹 추가
for mark in markinglist:
    mark.add_to(m)

# 본관에서 상경학관까지의 경로를 직선으로 그리기
folium.PolyLine(
    locations=[bon.location,bon1.location,bon_sang.location, sang1.location, sang.location],  # 경로에 있는 좌표 리스트
    color="green",  # 선의 색깔
    weight=5,  # 선의 두께
    opacity=0.8  # 선의 투명도
).add_to(m)
m.add_child(folium.LatLngPopup())
# 지도 출력
m