import json

# 讀取 GeoJSON 文件
with open('/Users/liyunyun/Documents/GitHub/Taipei-City-Dashboard/Taipei-City-Dashboard-FE/public/mapData/violations.geojson', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 更新每個點的 speed_category
for feature in data['features']:
    car_speed = feature['properties']['Car_Speed']
    limit_speed = feature['properties']['Limit_Speed']
    speed_difference = car_speed - limit_speed

    # 根據條件設置 speed_category
    if speed_difference >= 40:
        feature['properties']['speed_category'] = "嚴重超速 >= 40km/h"
    elif speed_difference >= 10:
        feature['properties']['speed_category'] = "超速 >= 10km/h"
    else:
        feature['properties']['speed_category'] = "正常速度"

# 保存更新後的 GeoJSON 文件
with open('violations_updated.geojson', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("GeoJSON 文件已成功更新！")