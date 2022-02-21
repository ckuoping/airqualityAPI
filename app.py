from flask import Flask, render_template, request
from pm25 import PM25
import requests
import math
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# 串接行政院環境保護署API
# https://opendata.epa.gov.tw/api/index.html

PM25_URL = 'https://opendata.epa.gov.tw/api/v1/PM25?%24skip=0&%24top=1000&%24format=json'
# PM25_URL='https://opendata.epa.gov.tw/webapi/Data/ATM00766/?$orderby=SiteId%20desc&$skip=0&$top=1000&format=json'
# 透過request模組取得PM25原始資料
raw_data_list = requests.get(PM25_URL).json()
PM25_list = list(map(lambda data: PM25(data), raw_data_list))


@app.route('/')
def home_page():
    page = request.args.get('page')
    # 如果page不存在，則預設為1；如果存在，則轉整數
    page = int(page) if page else 1

    # 定義一個頁面想呈現的資料長度
    page_item_length = 5

    # 取得最後一頁的頁碼，要無條件進位
    last_page_no = math.ceil(len(PM25_list)/page_item_length)

    # 建立一串列 需要顯示的PM25資料
    result = []

    for i in range(0, page_item_length):
        idx = (page_item_length*(page-1))+i
        print('idx', idx)

        # 若目前預計疊代的索引值超過了串列長度，則跳脫迴圈
        if idx >= len(PM25_list):
            break

        # 透過索引取得對應的資料
        PM25_item = PM25_list[idx]
        # print(PM25_item.id)
        result.append(PM25_item)

    return render_template('home.html', PM25_list=result, last_page_no=last_page_no, current_page=page)


if __name__ == '__main__':
    app.run(debug=True)
