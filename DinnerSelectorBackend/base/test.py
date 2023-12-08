from bs4 import BeautifulSoup as Soup
from selenium import webdriver
# 獲取網頁原始碼
url = "https://www.google.com/maps/place/%E7%89%9B%E8%82%89%E9%BA%B5%E8%88%98/@25.0155497,121.4159079,17z/data=!3m1!4b1!4m6!3m5!1s0x34681d9606a67625:0x673430f45a99a78!8m2!3d25.0155497!4d121.4159079!16s%2Fg%2F11f9wtt70q?hl=zh-TW&entry=ttu"
driver = webdriver.Chrome()
driver.get(url)

soup = Soup(driver.page_source,"lxml")
# 獲取評論資料框架
all_reviews = soup.find_all(class_ = 'jftiEf fontBodyMedium')
# 以第一則評論為例
ar = all_reviews[1] # 第幾則評論
print(all_reviews[1])
# # 評論者名稱
# reviewer_name = ar.find(class_ = "section-review-title").text


# # 評論者代稱＆評論數
# subtitle_review = ar.find(class_ = "section-review-subtitle").text

# # 評論星數
# star_review = str(ar.find(class_ = "section-review-stars").get('aria-label').strip().strip("顆星"))

# # 評論時間
# date_review = ar.find(class_ = "section-review-publish-date").text

# # 評論內容
text_review = ar.find(class_ = "MyEned").text
print(text_review)
driver.close()