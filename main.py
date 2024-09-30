import folium   # folium을 호출

class building:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def marking(self, color, icon):
        return folium.Marker(location = self.location,
        popup=self.name,
        icon=folium.Icon(color=color,icon=icon)
        )
        
        
center = [36.908, 127.143619452225] # 남서울대학교의 [위도, 경도] 불러오는 함수
m = folium.Map(location=center, zoom_start=15.5) # m 변수 지정, 남서울대학교, 화면 해상도 10
mainbuilding = building("본관", [36.9072014, 127.1430552])
sanggyung = building("상경학관", [36.90818157832219, 127.14407494870781])

markinglist = list() 

markinglist.append(mainbuilding.marking("blue", "circle"))
markinglist.append(sanggyung.marking("red", "circle"))

for mark in markinglist:
    mark.add_to(m)

m




    