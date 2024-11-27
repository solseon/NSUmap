#다익스트라(출발지, 도착지 직접 연결 제외)
import os
import folium
import csv
from flask import Flask, render_template, request
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


@app.route("/route", methods=["GET", "POST"])
def route():
    start = None
    end = None
    map_html = None
    error_message = None
    buildings = load_buildings()
    path_result = None  # 경로 결과 저장

    # connections.csv에서 연결 정보 읽기
    connections = {}
    with open(os.path.join(app.root_path, 'static', 'connections.csv'), 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            start_building, end_building, distance = row[0], row[1], float(row[2])
            if start_building not in connections:
                connections[start_building] = {}
            connections[start_building][end_building] = distance
            if end_building not in connections:
                connections[end_building] = {}
            connections[end_building][start_building] = distance

    if request.method == "POST":
        start = request.form.get('start')
        end = request.form.get('end')

        start = start.strip().lower()
        end = end.strip().lower()

        start_coords = buildings.get(start)
        end_coords = buildings.get(end)

        if start_coords and end_coords:
            # 경로 자동 생성
            path = find_path_visiting_all(connections, start, end)

            if path:
                # 경로 출력 (콘솔)
                print(f"생성된 경로: {' -> '.join(path)}")
                path_result = " -> ".join(path)  # 경로를 HTML로 표시 가능
                coordinates = [buildings[node] for node in path]
                
                # folium 지도 생성
                m = folium.Map(location=start_coords, zoom_start=18)
                folium.PolyLine(coordinates, color="blue", weight=2.5, opacity=1).add_to(m)

                # 각 노드에 마커 추가
                for node in path:
                    coords = buildings.get(node)
                    folium.Marker(coords, popup=node).add_to(m)

                map_html = m._repr_html_()
            else:
                error_message = "모든 경로를 방문하는 경로를 찾을 수 없습니다."
        else:
            error_message = f"출발지 또는 도착지 정보가 유효하지 않습니다: {start}, {end}"

    return render_template(
        'route_map.html', 
        start=start, 
        end=end, 
        map_html=map_html, 
        error_message=error_message, 
        path_result=path_result  # 경로 결과 전달
    )

if __name__ == "__main__":
    app.run(debug=True)