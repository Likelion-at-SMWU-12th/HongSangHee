import requests
import json

city = "Venice"
apikey = "a3abc0bf7648f4f7da07f363828bd098"
lang="kr"

api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"


result = requests.get(api)

data=json.loads(result.text)

#print(type(result.text))
#print(data)

print(data["name"], "의 날씨입니다.")
print("날씨는 ", data["weather"][0]["description"], "입니다.")
print("현재 온도는", data["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
print("최저 기온은 ", data["main"]["temp_min"], "입니다.")
print("최고 기온은 ", data["main"]["temp_max"], "입니다.")
print("기압은 ", data["main"]["pressure"], "입니다.")
print("습도는 ", data["main"]["humidity"], "입니다.")
print("🍃바람에 대한 안내입니다.")
print("오늘의 풍향은 ",data["wind"]["deg"],"입니다.")
print("오늘의 풍속은 ",data["wind"]["speed"],"m/s 입니다.")
