// 替換為你的 Mapbox Token
mapboxgl.accessToken =
	"pk.eyJ1IjoieXVubmxpIiwiYSI6ImNtNHdkZzR6cDAzaWEycXIwNGt2bXFvcnEifQ.0Or6vVLBUGV5xB3E235COQ";

// 初始化 Mapbox 地圖
const map = new mapboxgl.Map({
	container: "map", // 對應 HTML 中的地圖容器 ID
	style: "mapbox://styles/mapbox/streets-v11",
	center: [121.54522, 25.108595], // 台北市中心經緯度
	zoom: 12, // 起始縮放等級
});

map.on("load", () => {
	fetch("./violations.geojson")
		.then((response) => response.json())
		.then((data) => {
			const coordinates = data.features.map(
				(feature) => feature.geometry.coordinates
			);
			const uniqueCoordinates = new Set();
			const offset = 0.0001; // 每次微調的偏移量
			const adjustedData = data.features.map((feature) => {
				let [lng, lat] = feature.geometry.coordinates;
				while (uniqueCoordinates.has(`${lng},${lat}`)) {
					lng += offset;
					lat += offset;
				}
				uniqueCoordinates.add(`${lng},${lat}`);
				feature.geometry.coordinates = [lng, lat];
				return feature;
			});

			map.addSource("violations", {
				type: "geojson",
				data: {
					type: "FeatureCollection",
					features: adjustedData,
				},
			});

			map.addLayer({
				id: "violations-layer",
				type: "circle",
				source: "violations",
				paint: {
					"circle-radius": 8,
					"circle-color": [
						"match",
						["get", "speed_category"],
						"超速 >= 10km/h",
						"#F49F36",
						"嚴重超速 >= 40km/h",
						"#F5C860",
						"#F65658",
					],
				},
			});
			console.log("重複的地點已修正");
		});
});
