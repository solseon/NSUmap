class building: # 건물 이름, 위치, 마킹 클래스
    def __init__(self, name, location): 
        self.name = name    # 이름변수
        self.location = location    # 위치변수[위도,경도]
    def marking(self, color, icon):   
        return folium.Marker(location = self.location,
        popup=self.name,
        icon=folium.Icon(color=color,icon=icon)
        )

building("본관", [36.9072014, 127.1430552]) #본관
building("상경학관", [36.90818157832219, 127.14407494870781]) #상경학관

markinglist = [
    mainbuilding.marking("blue", "circle"),
    sanggyung.marking("red", "circle")
]