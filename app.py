import folium
from flask import Flask, render_template, request
from folium.plugins import MarkerCluster

app = Flask(__name__)

# 예시로 사용할 건물 위치들
buildings = {
    "본관": [36.90725, 127.1431],
    "공학1관": [36.9073, 127.1436],
    "공학2관": [36.9072, 127.1426],
    "상경학관": [36.90818157832219, 127.14407494870781]
}

@app.route("/route", methods=["GET", "POST"])
def route():
    start = None
    end = None
    map_html = None

    if request.method == "POST":
        start = request.form.get('start')
        end = request.form.get('end')

        # 출발지와 도착지에 대한 좌표 가져오기
        start_coords = buildings.get(start)
        end_coords = buildings.get(end)

        if start_coords and end_coords:
            # folium 지도 생성
            m = folium.Map(location=start_coords, zoom_start=18)

            # 출발지와 도착지 마커 추가
            folium.Marker(start_coords, popup=f"출발지: {start}").add_to(m)
            folium.Marker(end_coords, popup=f"도착지: {end}").add_to(m)

            # 출발지에서 도착지로 경로를 그리는 코드는 추가 가능 (예시로 직선 추가)
            folium.PolyLine([start_coords, end_coords], color="blue", weight=2.5, opacity=1).add_to(m)

            # HTML로 변환하여 지도 포함
            map_html = m._repr_html_()

    return render_template('route_map.html', start=start, end=end, map_html=map_html)

if __name__ == "__main__":
    app.run(debug=True)
