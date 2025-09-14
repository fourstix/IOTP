from __future__ import print_function
from Adafruit_Thermal import *
from datetime import date
import calendar
import urllib.request
import json

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
def getLink(dailyOrHourly):
    latitude = "35.9267" #limit to four decimal digits
    longitude = "-78.8242" #limit to four decimal digits
    mainLink = "https://api.weather.gov/points/" + latitude + "," + longitude
    response_main = urllib.request.urlopen(mainLink)
    raw_data_main = response_main.read().decode()
    data_main = json.loads(raw_data_main)
    properties_main = data_main['properties']
    dailyLink = properties_main["forecast"]
    hourlyLink = properties_main["forecastHourly"]
    if dailyOrHourly == "daily":
        return dailyLink
    elif dailyOrHourly == "hourly":
        return hourlyLink

url_daily = getLink("daily")
response_daily = urllib.request.urlopen(url_daily)
# status & reason
# print(response_daily.status, response_daily.reason)

raw_data_daily = response_daily.read().decode()
data_daily = json.loads(raw_data_daily)
forecast_periods_daily = data_daily['properties']['periods']


current_period_isDayTime = forecast_periods_daily[0]['isDaytime']

if current_period_isDayTime:
    day_index = 0
    night_index = 1
else:
    day_index = 1
    night_index = 0

day_name = forecast_periods_daily[day_index]['name']
hi_temp = forecast_periods_daily[day_index]['temperature']
night_name = forecast_periods_daily[night_index]['name']
lo_temp = forecast_periods_daily[night_index]['temperature']
current_detailed_forecast = forecast_periods_daily[0]['detailedForecast']

url_hourly = getLink("hourly")
response_hourly = urllib.request.urlopen(url_hourly)
# status & reason
#print(response_hourly.status, response_hourly.reason)

raw_data_hourly = response_hourly.read().decode()
data_hourly = json.loads(raw_data_hourly)
forecast_periods_hourly = data_hourly['properties']['periods']
temperature = forecast_periods_hourly[0]['temperature']

d = date.today()
week_day = calendar.day_name[date(d.year,d.month,d.day).weekday()]
month_text = calendar.month_name[d.month]
printer.underlineOn()
printer.println("It's " + week_day + ", " + month_text + " " + str(d.day) + "\n")
printer.underlineOff()
printer.boldOn()
printer.println(day_name + "'s Forecast \n")
printer.boldOff()
printer.print("Current temperature: " + str(temperature) + " F \n")
printer.print("High temperature: " + str(hi_temp) + " F \n")
printer.print("Low temperature: " + str(lo_temp) + " F \n")
printer.println(current_detailed_forecast + "\n")

# show next three days
for idx in range(2, 8):
  p_name = forecast_periods_daily[idx]['name']
  p_temp = forecast_periods_daily[idx]['temperature']
  p_fore = forecast_periods_daily[night_index]['shortForecast']
  printer.boldOn()
  printer.println(p_name)
  printer.boldOff()
  printer.println(p_fore + " " + str(p_temp) + " F")

printer.feed(3)
