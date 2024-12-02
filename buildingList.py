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
