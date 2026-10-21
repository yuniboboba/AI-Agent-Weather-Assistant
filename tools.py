import requests
import json
from langchain_core.tools import tool


@tool
def get_coordinates(city: str) -> str:
    """查詢城市的地理座標。輸入城市名稱，回傳 JSON 字串，
    包含 latitude、longitude、country。查詢天氣或其他地點相關資訊前，需要先取得座標。"""

    resp = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1, "language": "zh", "format": "json"},
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()

    results = data.get("results")
    if not results:
        return json.dumps({"error": f"找不到城市：{city}"}, ensure_ascii=False)

    place = results[0]
    return json.dumps({
        "name": place["name"],
        "latitude": place["latitude"],
        "longitude": place["longitude"],
        "country": place.get("country", ""),
    }, ensure_ascii=False)

@tool
def get_weather(latitude: float, longitude: float) -> str:
    """根據經緯度查詢今天的天氣預報。使用前需要先呼叫 get_coordinates 取得座標。
    回傳每日與每小時的天氣數據（JSON 字串），包含最高溫、最低溫、降雨機率、風速、紫外線指數等。"""

    resp = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": latitude,
            "longitude": longitude,
            "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max,uv_index_max",
            "hourly": "temperature_2m,precipitation_probability",
            "timezone": "auto",
            "forecast_days": 1,
        },
        timeout=10,
    )
    resp.raise_for_status()
    data = resp.json()

    daily = data["daily"]
    hourly = data["hourly"]

    weather = {
        "date": daily["time"][0],
        "weather_code": daily["weather_code"][0],
        "temp_max": daily["temperature_2m_max"][0],
        "temp_min": daily["temperature_2m_min"][0],
        "rain_prob": daily["precipitation_probability_max"][0],
        "rain_sum": daily["precipitation_sum"][0],
        "wind_max": daily["wind_speed_10m_max"][0],
        "uv_max": daily["uv_index_max"][0],
        "hourly_time": hourly["time"],
        "hourly_rain_prob": hourly["precipitation_probability"],
    }
    return json.dumps(weather, ensure_ascii=False) 