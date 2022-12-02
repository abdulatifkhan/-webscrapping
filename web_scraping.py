from bs4 import BeautifulSoup
import requests
import datetime
from csv import writer

access_datetime = datetime.datetime.now()
source_url = "https://kun.uz/uz/news/2022/11/30/parda-ortidagi-xususiylashtirish-yirik-aktivlar-qanday-qilib-ofshor-kompaniyalarga-otib-ketmoqda"

result = requests.get(source_url)
doc = BeautifulSoup(result.text, "html.parser")
tags = doc.find_all("p")


with open("vocabulary.csv", "w", encoding="utf-8", newline="") as f:
    thewriter = writer(f)
    header = ["source_url", "access_datetime", "content", "word"]
    thewriter.writerow(header)

    for tag in tags:
        content = tag.text.strip().replace("‘", "'").replace(
            "’", "'").replace("–", "-").replace("“", '"').replace("”", '"')
        info = [source_url, access_datetime, content, content.split()]
        thewriter.writerow(info)
