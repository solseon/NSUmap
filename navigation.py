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
m = folium.Map(location=center, zoom_start=16)

# 건물 정보 저장
main = Building("본관", [36.90725, 127.1431])
engineering1 = Building("공학1관", [36.9073, 127.1436])
engineering2 = Building("공학2관", [36.9072, 127.1426])
sanggyeong = Building("상경학관", [36.90818157832219, 127.14407494870781]) 
hwajeong = Building("화정관", [36.907897270555814, 127.14147090911865]) # 화정관
healthcare = Building("보건의료학관", [36.90817393627746, 127.1450811624527]) # 보건의료학관
molding = Building("조형학관", [36.90863133961879, 127.14494140543114]) # 조형학관
humanities = Building("인문사회학관", [36.90908220639218, 127.14487166799675]) # 인문사회학관
designinformation = Building("디자인정보관", [36.90962468046938, 127.14562536872994]) # 디자인정보관
twentyone = Building("21세기개발관", [36.90995186491852, 127.14474856853485]) # 21세기개발관
knowledgeinformation = Building("지식정보관", [36.91061167503247, 127.14485084049954]) # 지식정보관
gym = Building("성암문화체육관", [36.909789150342704, 127.14694525959654]) # 성암문화체육관
Elim1 = Building("제1엘림생활관", [36.90870757810947, 127.14732843829314]) # 제1엘림생활관
Elim2 = Building("제2엘림생활관", [36.908512796802036, 127.14654564857483]) # 제2엘림생활관
childwelfare = Building("아동복지학관", [36.91098784498547, 127.14109966412538]) # 아동복지학관
library = Building("성암기념중앙도서관", [36.90895245536589, 127.14343965053558]) # 성암기념중앙도서관
studentwelfare = Building("학생복지학관", [36.90974808548412, 127.14359297462225]) # 학생복지학관
learningsupport = Building("교수학습지원센터", [36.91020060473758, 127.14348568626166]) # 교수학습지원센터
ccpark = Building("CC동산", [36.9069, 127.1433])

# 도로 좌표
main_f = Building("본관 앞", [36.90755, 127.14305])
sanggyeong_f = Building('상경학관 앞',[36.9081 ,127.14391])
main_sanggyeong = Building('본관-상경 삼거리', [36.9077,127.1440])

# 흡연장 정보 저장
smoke_engineering1 = Building("공학1관 흡연장", [36.9072,127.1441])
smoke_engineering2 = Building("공학2관 흡연장", [36.9073, 127.1417])
smokek_sanggyeong = Building("상경학관 흡연장",[36.9082, 127.1443])
smoke_healthcare = Building("보건의료학관 흡연장", [36.9089, 127.1457])
smoke_library = Building("성암기념중앙도서관 흡연장",[36.9088, 127.1435])
smoke_knowledgeinformation = Building("지식정보관 흡연장", [36.9098, 127.1452])
smoke_elem1 = Building("엘림1생활관 흡연장", [36.9093, 127.1476])
smoke_gym = Building("성암문화체육관 흡연장", [36.9100, 127.1474])
smoke_tennis = Building("테니스장 흡연장", [36.9109, 127.1436])
smoke_parking1 = Building("제1주차장 흡연장", [36.9099, 127.1420])
smoke_busstop = Building("버스정류장 흡연장",[36.9107, 127.1420])

# 주차장 정보 저장
parking_bus = Building("버스 주차장", [36.9103, 127.1424])
parking_parking1 = Building("제1주차장", [36.9092, 127.1416])
parking_parking2 = Building("제2주차장", [36.9085, 127.1411])
parking_library = Building("성앙기념중앙도서관 주차장", [36.9090, 127.1440])
parking_studentwelfare = Building("학생복지회관 주차장", [36.9097, 127.1431])
parking_group = Building("동아리방 주차장", [36.9110, 127.1446])
parking_gym = Building("성함문화체육관 주차장", [36.9107, 127.1463])
parking_elem1 = Building("엘림1생활관 주차장", [36.9091, 127.1472])


# 건물 마킹 리스트 생성
markinglist = list()

# 건물 마킹
markinglist.append(main.marking("red", "circle"))
markinglist.append(engineering1.marking("red", "circle"))
markinglist.append(engineering2.marking("red", "circle"))
markinglist.append(sanggyeong.marking("red", "circle"))

markinglist.append(smoke_engineering1.marking("green","circle"))
markinglist.append(smoke_engineering2.marking("green","circle"))
markinglist.append(smokek_sanggyeong.marking("green","circle"))
markinglist.append(smoke_healthcare.marking("green","circle"))
markinglist.append(smoke_library.marking("green","circle"))
markinglist.append(smoke_elem1.marking("green","circle"))
markinglist.append(smoke_gym.marking("green","circle"))
markinglist.append(smoke_knowledgeinformation.marking("green","circle"))
markinglist.append(smoke_tennis.marking("green","circle"))
markinglist.append(smoke_parking1.marking("green","circle"))
markinglist.append(smoke_busstop.marking("green","circle"))

markinglist.append(parking_bus.marking("blue", "circle"))
markinglist.append(parking_parking1.marking("blue", "circle"))
markinglist.append(parking_parking2.marking("blue", "circle"))
markinglist.append(parking_library.marking("blue", "circle"))
markinglist.append(parking_studentwelfare.marking("blue", "circle"))
markinglist.append(parking_group.marking("blue", "circle"))
markinglist.append(parking_gym.marking("blue", "circle"))
markinglist.append(parking_elem1.marking("blue", "circle"))

# 마킹 추가
for mark in markinglist:
    mark.add_to(m)

# 본관에서 상경학관까지의 경로를 직선으로 그리기
folium.PolyLine(
    locations=[main.location,main_f.location,main_sanggyeong.location, sanggyeong_f.location, sanggyeong.location],  # 경로에 있는 좌표 리스트
    color="green",  # 선의 색깔
    weight=5,  # 선의 두께
    opacity=0.8  # 선의 투명도
).add_to(m)
m.add_child(folium.LatLngPopup())
# 지도 출력
m