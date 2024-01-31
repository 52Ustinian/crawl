"""
用useragent进行反爬
获取Ajax请求的数据，获得请求参数
for循环进行不同参数
"""
import requests
import pandas as pd
url="http://tianqi.2345.com/Pc/GetHistory"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}
#爬取单个表格
def craw_table(year,month):
    # 提供年份和月份爬取对应表格数据
    params = {
        "areaInfo[areaId]": "59287",
        "areaInfo[areaType]": "2",
        "date[year]": year,
        "date[month]": month
    }
    res = requests.get(url, headers=headers, params=params)
    # print(res.status_code)
    data = res.json()["data"]
    # print(data)
    df = pd.read_html(data)[0]  # 第一个表格
    # print(df)
    return df

list=[]
for year in range(2011,2024):
    for month in range(1,13):
        df=craw_table(year,month)
        list.append(df)

pd.concat(list).to_excel('广州最近十年天气.xlsx',index=False)