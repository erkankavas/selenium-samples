## IMDP Top Chart

# Create and activate a virtual environment:
# python3 -m venv venv
# source venv/bin/activate  (Mac/Linux)
# venv\Scripts\activate      (Windows)

# Install required dependencies:
# pip3 install selenium webdriver-manager beautifulsoup4

# Run the script:
# python3 imdb-chart.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Tarayıcıyı başlat
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Headless modu kapalı!

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# IMDb'nin en iyi 250 filmler sayfasını aç
url = "https://www.imdb.com/chart/top/"
driver.get(url)

# Sayfanın yüklenmesini bekle (UL listesinin HTML içinde görünmesini bekliyoruz)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ipc-metadata-list"))
    )
except:
    print("Sayfa yüklenmedi, işlem sonlandırılıyor.")
    driver.quit()
    exit()

# Sayfanın HTML kaynağını al
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Tarayıcıyı kapat
driver.quit()

# UL etiketi arayalım
ul_element = soup.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base")

print("Bulunan UL:", ul_element)

if ul_element:
    li_elements = ul_element.find_all("li")
    
    for li in li_elements[:10]:  # İlk 10 filmi yazdır
        title_element = li.find("h3", class_="ipc-title__text")  # Filmin başlığı
        rating_element = li.find("span", class_="ipc-rating-star--rating")  # Puan
        
        title = title_element.text.strip() if title_element else "Başlık Bulunamadı"
        rating = rating_element.text.strip() if rating_element else "Puan Yok"
        
        print(f"Film: {title} - Puan: {rating}")
else:
    print("Film listesi bulunamadı!")
