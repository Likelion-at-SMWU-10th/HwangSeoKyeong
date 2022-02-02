import requests
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

city = "Paju"
apikey = "65ecd6da4d7f5711b1d3b3c87c2adf12"
lang = "kr"
units = "metric"
api = f"""http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

result = requests.get(api)
#print(result.text)

data = json.loads(result.text)

print(data["name"], "의 날씨입니다.")
print("날씨는 ", data["weather"][0]["description"], "입니다.")
print("현재 온도는 ", data["main"]["temp"], "입니다.")
print("하지만 체감 온도는 ", data["main"]["feels_like"], "입니다.")
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온는 ", data["main"]["temp_max"], "입니다.")
print("습도는 ", data["main"]["humidity"], "입니다.")
print("기압은 ", data["main"]["pressure"], "입니다.")
print("풍향은 ", data["wind"]["deg"], "입니다.")
print("풍속은 ", data["wind"]["speed"], "입니다.")