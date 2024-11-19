import folium

class building: # 건물 이름, 위치, 마킹 클래스
    def __init__(self, name, location): 
        self.name = name    # 이름변수
        self.location = location    # 위치변수[위도,경도]
    def marking(self, color, icon):   
        return folium.Marker(location = self.location,
        popup=self.name,
        icon=folium.Icon(color=color,icon=icon)
        )
    def markingList(self, data):    # 객체들을 마킹해주는 함수
        hakkwan = List()    # 객체를 담아야하는 리스트 생성
        for i in data:      # hakkwan 리스트에 객체 데이터들을 넣어주는 작업
            hakkwan.append(i)
        return hakkwan # 객체가 담겨있는 리스트 반환