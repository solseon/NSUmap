import folium   # folium을 호출

class building: # 건물 이름, 위치, 마킹 클래스
    def __init__(self, name, location): 
        self.name = name    # 이름변수
        self.location = location    # 위치변수[위도,경도]
    def marking(self, color, icon):   
        return folium.Marker(location = self.location,
        popup=self.name,
        icon=folium.Icon(color=color,icon=icon)
        )
        
        
center = [36.908, 127.143619452225] # 남서울대학교의 [위도, 경도] 불러오는 함수
m = folium.Map(location=center, zoom_start=15.5) # m 변수 지정, 남서울대학교, 화면 해상도 15.5

# 학관 객체생성 (이름, 위도,경도 저장)
bon = building("본관", [36.9072014, 127.1430552]) # 본관 
sanggyeong = building("상경학관", [36.90818157832219, 127.14407494870781]) # 상경학관 
hwajeong = building("화정관", [36.907897270555814, 127.14147090911865]) # 화정관
engineering1 = building("공학1관", [36.907140585234814, 127.14252819637]) # 공학1관
engineering2 = building("공학2관", [36.90728642610151, 127.14364399532019]) # 공학2관
healthcare = building("보건의료학관", [36.90817393627746, 127.1450811624527]) # 보건의료학관
molding = building("조형학관", [36.90863133961879, 127.14494140543114]) # 조형학관
humanities = building("인문사회학관", [36.90908220639218, 127.14487166799675]) # 인문사회학관
designinformation = building("디자인정보관", [36.90962468046938, 127.14562536872994]) # 디자인정보관
twentyone = building("21세기개발관", [36.90995186491852, 127.14474856853485]) # 21세기개발관
knowledgeinformation = building("지식정보관", [36.91061167503247, 127.14485084049954]) # 지식정보관
gym = building("성암문화체육관", [36.909789150342704, 127.14694525959654]) # 성암문화체육관
Elim1 = building("제1엘림생활관", [36.90870757810947, 127.14732843829314]) # 제1엘림생활관
Elim2 = building("제2엘림생활관", [36.908512796802036, 127.14654564857483]) # 제2엘림생활관
childwelfare = building("아동복지학관", [36.91098784498547, 127.14109966412538]) # 아동복지학관
library = building("성암기념중앙도서관", [36.90895245536589, 127.14343965053558]) # 성암기념중앙도서관
studentwelfare = building("학생복지학관", [36.90974808548412, 127.14359297462225]) # 학생복지학관
learningsupport = building("교수학습지원센터", [36.91020060473758, 127.14348568626166]) # 교수학습지원센터


markinglist = list() # 건물 마킹을 저장해주는 리스트

# 건물 마킹
markinglist.append(bon.marking("blue", "circle")) # 본관
markinglist.append(sanggyeong.marking("blue", "circle")) # 상경학관
markinglist.append(hwajeong.marking("blue", "circle")) # 화정관
markinglist.append(engineering1.marking("blue", "circle")) # 공학1관
markinglist.append(engineering2.marking("blue", "circle")) # 공학2관
markinglist.append(healthcare.marking("blue", "circle")) # 보건의료학관
markinglist.append(molding.marking("blue", "circle")) # 조형학관
markinglist.append(humanities.marking("blue", "circle")) # 인문사회학관
markinglist.append(designinformation.marking("blue", "circle")) # 디자인정보관
markinglist.append(twentyone.marking("blue", "circle")) # 21세기개발관
markinglist.append(knowledgeinformation.marking("blue", "circle")) # 지식정보관
markinglist.append(gym.marking("blue", "circle")) # 성암문화체육관
markinglist.append(Elim1.marking("blue", "circle")) # 제1엘림생활관
markinglist.append(Elim2.marking("blue", "circle")) # 제2엘림생활관
markinglist.append(childwelfare.marking("blue", "circle")) # 아동복지학관
markinglist.append(library.marking("blue", "circle")) # 성암기념중앙도서관
markinglist.append(studentwelfare.marking("blue", "circle")) # 학생복지학관
markinglist.append(learningsupport.marking("blue", "circle")) # 교수학습지원센터


for mark in markinglist:    # 리스트에 저장된 마킹 추가
    mark.add_to(m)

m # 지도 출력




    