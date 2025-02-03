from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

진짜증수 = -1
등수 = -1
for 페이지인덱스 in range(1,15):
    # 1. URL로 1페이지 방문
    # 페이지인덱스 = 1
    검색쿼리 = "꿀사과"
    shoplink=f"https://msearch.shopping.naver.com/search/all?adQuery=%EA%BF%80%EC%82%AC%EA%B3%BC&origQuery=%EA%BF%80%EC%82%AC%EA%B3%BC&pagingIndex={페이지인덱스}&pagingSize=40&productSet=total&query={검색쿼리}&sort=rel&viewType=list"
    driver.get(shoplink)
    time.sleep(3)

    # 2. 페이지를 4~5번 내림 상품 더 불러오기
    for _ in range(5):
        driver.execute_script("window.scrollBy(0,10000);")
        time.sleep(2)
        
    # 3. 타켓 상품이 페이지에 노출되고 있는지 확인하기
    # 4. 없다면 url로 next page 이동
    try:
        타켓_상품_코드= "88509786643"
        타켓_상품_셀렉터 = f"a[data-i='{타켓_상품_코드}']"
        타켓_상품_엘리먼트 = driver.find_element(By.CSS_SELECTOR, 타켓_상품_셀렉터)
        데이터 = 타켓_상품_엘리먼트.get_attribute('data-nclick')
        print(데이터.split(f"{타켓_상품_코드},r:"))
        print(데이터.split(f"{타켓_상품_코드},r:")[-1])
        등수 = 데이터.split(f"{타켓_상품_코드},r:").split(",")[0]
        print("등수",등수)
        진짜등수 = (int(페이지인덱스) -1) * 40 + int(등수)
        break
    except:
        print(f"{페이지인덱스} 페이지에서 타켓 상품을 못 찾음")
        # Next page 방문 필요
print("내 상품의 진짜 등수는 ", 진짜등수," 등입니다")
print(f"내 상품은 {페이지인덱스} 페이지의 {등수}등에 노출되고 있습니다")        
input()
