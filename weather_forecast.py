import os
import datetime
import PyRSS2Gen
import httpx
from lxml import etree


cwd = os.path.split(os.path.realpath(__file__))[0]
filepath = f"{cwd}/weather.txt"
url = "http://www.weather.com.cn/weather/101010900.shtml"
agent = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
}
file = open(filepath)
# res = httpx.get(url, headers=agent)
# sel = etree.HTML(res.text)
sel = etree.HTML(file.read())
seven_days = sel.xpath('//*[@id="7d"]/ul/li')
for day in seven_days:
    date = day.xpath("./h1/text()")[0]
    wea = day.xpath("./p[@class='wea']/text()")[0]
    tem_high = day.xpath("./p[@class='tem']/span/text()")[0]
    tem_low = day.xpath("./p[@class='tem']/i/text()")[0].replace("℃", "")
    win = "/".join(day.xpath("./p[@class='win']/em/span/@title"))
    win_level = "/".join(day.xpath("./p[@class='win']/i/text()"))

    forecast = f"{date}{wea}，气温{tem_low}~{tem_high}，{win}{win_level}"
    print(forecast)

rss = PyRSS2Gen.RSS2(
    title="Custom Weather Forecast",
    link="",
    description="weather forecast",
    lastBuildDate=datetime.datetime.now(),
    items=[
        PyRSS2Gen.RSSItem(
            title="PyRSS2Gen-0.0 released",
            link="http://www.dalkescientific.com/news/030906-PyRSS2Gen.html",
            description="Dalke Scientific today announced PyRSS2Gen-0.0, "
            "a library for generating RSS feeds for Python.  ",
            guid=PyRSS2Gen.Guid(
                "http://www.dalkescientific.com/news/" "030906-PyRSS2Gen.html"
            ),
            pubDate=datetime.datetime.now(),
        ),
    ],
)

# rss.write_xml(open("weather_forecast.xml", "w"))
