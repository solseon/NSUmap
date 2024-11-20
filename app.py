import os
import folium
import csv
from flask import Flask, render_template, request
from folium.plugins import MarkerCluster

app = Flask(__name__)

# CSV 파일에서 읽어서 buildings 딕셔너리 생성하기
def load_buildings():
    buildings = {}
    file_path = os.path.join(app.root_path, 'static', 'sample.csv')  # 절대 경로 사용
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # 빈 행을 처리하기 위해
                name, lat, lon = row[0], float(row[1]), float(row[2])
                buildings[name] = [lat, lon]
    return buildings

@app.route("/route", methods=["GET", "POST"])
def route():
    start = None
    end = None
    map_html = None
    error_message = None
    buildings = load_buildings()  # CSV 파일에서 읽어온 건물 정보

    if request.method == "POST":
        start = request.form.get('start')
        end = request.form.get('end')

        # 입력값을 소문자로 변환하여 비교 (대소문자 구분 없애기)
        start = start.strip().lower()
        end = end.strip().lower()

        # buildings 딕셔너리의 모든 키를 출력하여 확인하기
        print("빌딩 목록:", buildings.keys())

        # 건물 목록에서 소문자로 변환하여 키를 찾기
        start_coords = buildings.get(start)
        end_coords = buildings.get(end)

        if start_coords and end_coords:
            # folium 지도 생성
            m = folium.Map(location=start_coords, zoom_start=18)

            # 출발지와 도착지 마커 추가
            folium.Marker(start_coords, popup=f"출발지: {start}").add_to(m)
            folium.Marker(end_coords, popup=f"도착지: {end}").add_to(m)

            # 출발지에서 도착지로 경로를 그리는 코드
            folium.PolyLine([start_coords, end_coords], color="blue", weight=2.5, opacity=1).add_to(m)

            # HTML로 변환하여 지도 포함
            map_html = m._repr_html_()
        else:
            # 출발지 또는 도착지를 찾지 못한 경우
            error_message = f"입력한 출발지 또는 도착지를 찾을 수 없습니다: {start}, {end}"

    return render_template('route_map.html', start=start, end=end, map_html=map_html, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
