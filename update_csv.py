import json
import csv

# 讀取 GeoJSON 文件
with open('/Users/liyunyun/Documents/GitHub/Taipei-City-Dashboard/Taipei-City-Dashboard-FE/public/mapData/violations.geojson', 'r', encoding='utf-8') as geojson_file:
    geojson_data = json.load(geojson_file)

# 創建一個查找字典，基於唯一屬性（例如 Device_ID 和 Violation_Time）
geojson_lookup = {
    (feature['properties']['Device_ID'], feature['properties']['Violation_Time']): feature['properties']['speed_category']
    for feature in geojson_data['features']
}

# 讀取原始 CSV 文件，並更新 speed_category 欄位
updated_rows = []
with open('/Users/liyunyun/Desktop/violations3-1.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # 根據唯一屬性找到對應的 speed_category
        key = (int(row['Device_ID']), row['Violation_Time'])
        row['speed_category'] = geojson_lookup.get(key, "未知")  # 如果找不到，設為 "未知"
        updated_rows.append(row)

# 寫入更新後的 CSV 文件
with open('violations_updated.csv', 'w', encoding='utf-8', newline='') as csv_file:
    fieldnames = list(updated_rows[0].keys())
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(updated_rows)

print("CSV 文件已成功更新！")