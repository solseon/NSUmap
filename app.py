import os
import folium
import csv
from flask import Flask, render_template, request
from folium import plugins, CustomIcon, Icon, Popup
from folium.plugins import MarkerCluster
import heapq

app = Flask(__name__)

# CSV 파일에서 읽어서 buildings 딕셔너리 생성하기
def load_buildings():
    buildings = {}
    file_path = os.path.join(app.root_path, 'static', 'sampleTest.csv')  # 절대 경로 사용
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:  # 빈 행을 처리하기 위해
                name, lat, lon = row[0], float(row[1]), float(row[2])
                buildings[name] = [lat, lon]
    return buildings

# 다익스트라 알고리즘을 이용해 최단 경로 찾기
def find_shortest_path(connections, start, end):
    distances = {node: float('inf') for node in connections}
    distances[start] = 0
    priority_queue = [(0, start, [])]  # (거리, 현재 노드, 경로)
    
    while priority_queue:
        current_distance, current_node, path = heapq.heappop(priority_queue)
        print(f"현재 노드: {current_node}, 거리: {current_distance}, 경로: {path}")  # 디버깅 출력
        
        if current_distance > distances[current_node]:
            continue
        
        path = path + [current_node]
        
        if current_node == end:
            print(f"최단 경로 찾음: {path}")
            return path
        
        for neighbor, weight in connections.get(current_node, {}).items():
            distance = current_distance + weight
            
            # 직접 연결된 경로는 제외하도록 처리
            if current_node != start or neighbor != end:
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor, path))
                    print(f"추가 탐색: {neighbor}, 업데이트된 거리: {distance}, 경로: {path}")
    
    print("경로를 찾을 수 없음")
    return None

def find_path_visiting_all(connections, start, end):
    """
    출발지에서 도착지까지 모든 중간 노드를 순차적으로 방문하며 경로를 생성.
    - connections: 연결 정보 딕셔너리
    - start: 시작 노드
    - end: 종료 노드
    """
    current = start
    visited = set()
    path = [start]

    while current != end:
        visited.add(current)
        neighbors = connections.get(current, {})
        
        # 방문하지 않은 이웃 중 가장 가까운 노드 선택
        next_node = None
        min_distance = float('inf')
        for neighbor, distance in neighbors.items():
            if neighbor not in visited and distance < min_distance:
                next_node = neighbor
                min_distance = distance
        
        if next_node is None:  # 더 이상 이동할 곳이 없으면 실패
            print("경로를 완성할 수 없습니다.")
            return None
        
        path.append(next_node)
        current = next_node

    return path

def load_connections():
    connections = {}
    with open(os.path.join(app.root_path, 'static', 'connections.csv'), 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            start_building, end_building, distance = row[0], row[1], float(row[2])
            connections.setdefault(start_building, {})[end_building] = distance
            connections.setdefault(end_building, {})[start_building] = distance
    return connections

def load_places(filename):
    places = []
    file_path = os.path.join(app.root_path, 'static', filename)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 첫 번째 행(헤더)을 건너뜁니다.
        
        for row in reader:
            try:
                # CSV에서 읽은 행(row)의 첫 번째 열을 건물 이름, 두 번째 열을 위도(lat), 세 번째 열을 경도(lon)으로 처리
                name, lat, lon = row[0], row[1], row[2]
                
                # lat와 lon이 숫자값이므로 float로 변환
                lat = float(lat)
                lon = float(lon)
                
                # 유효한 좌표일 경우에만 places 리스트에 추가
                places.append({'name': name, 'coords': [lat, lon]})
            except ValueError:
                # 잘못된 데이터가 있을 경우, 해당 행을 건너뜁니다.
                print(f"잘못된 데이터: {row} (위도나 경도가 잘못된 값입니다.)")
                continue
    
    return places

@app.route("/route", methods=["GET", "POST"])
def route():
    # 빌딩 데이터와 경로 연결 정보 로드
    buildings = load_buildings()
    connections = load_connections()  # 연결 정보 로드
    cafes = load_places('cafe.csv')  # 카페 데이터 로드
    smoking_areas = load_places('smoking_area.csv')  # 흡연장 데이터 로드

    # 기본 지도 설정
    default_coords = list(buildings.values())[0]  # 첫 번째 건물 위치를 사용하여 기본 지도 설정
    m = folium.Map(location=default_coords, zoom_start=16)

    start = None
    end = None
    path_result = None
    error_message = None

    # 길찾기 (POST 요청)
    if request.method == "POST":
        start = request.form.get('start').strip().lower()  # 출발지
        end = request.form.get('end').strip().lower()  # 도착지

        start_coords = buildings.get(start)
        end_coords = buildings.get(end)

        if start_coords and end_coords:
            path = find_path_visiting_all(connections, start, end)  # 경로 찾기
            if path:
                path_result = " -> ".join(path)
                coordinates = [buildings[node] for node in path]

                # 지도에 경로 표시
                folium.PolyLine(coordinates, color="blue", weight=2.5, opacity=1).add_to(m)
                folium.Marker(
                    start_coords, 
                    popup=folium.Popup(f"<pre> {start.capitalize()}</pre>",max_width=300),
                    icon=folium.Icon(color="blue", icon="play")
                ).add_to(m)
                folium.Marker(end_coords, popup=f"도착지: {end.capitalize()}",
                              icon=folium.Icon(color="blue", icon="stop")).add_to(m)
            else:
                error_message = "모든 경로를 방문하는 경로를 찾을 수 없습니다."
        else:
            error_message = f"출발지 또는 도착지 정보가 유효하지 않습니다: {start}, {end}"

    # 카페/흡연장 마커 추가 (GET 요청)
    if request.args.get("show_cafes"):
        for cafe in cafes:
            folium.Marker(cafe['coords'], popup=cafe['name'],
                          icon=folium.Icon(color="green", prefix="fa", icon="coffee")).add_to(m)

    if request.args.get("show_smoking_areas"):
        for smoking_area in smoking_areas:
            folium.Marker(smoking_area['coords'], popup=smoking_area['name'],
                          icon=folium.Icon(color="red", prefix="fa", icon="smoking")).add_to(m)

    map_html = m._repr_html_()

    return render_template(
        'route_map.html',
        map_html=map_html,
        path_result=path_result,
        error_message=error_message,
    )

# 경로 마커들을 저장할 리스트는 글로벌 변수에서 로컬 변수로 변경
@app.route("/reset", methods=["POST"])
def reset():
    # 초기화된 지도 생성 (마커와 경로는 추가하지 않음)
    buildings = load_buildings()
    initial_coords = list(buildings.values())[0]  # 첫 번째 건물 위치 사용
    m = folium.Map(location=initial_coords, zoom_start=16)  # 초기 중심 좌표 설정

    # 경로와 마커 추가하지 않음 (완전 초기 상태)
    path_result = None
    error_message = None

    # 초기화된 지도 HTML 반환
    map_html = m._repr_html_()

    # 초기화된 지도와 경로 결과를 HTML에 전달
    return render_template('route_map.html', map_html=map_html, path_result=path_result, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
