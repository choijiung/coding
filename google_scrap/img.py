# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import time
import base64
import random
import string

# 이미지를 수집할 주소
base_url = 'https://www.google.com'
sub_url = '/search?sca_esv=99b72eded8c7f00f&sxsrf=AHTn8zpYsNTChS7coxZo-EHzNVIXDnx6OA:1739433729221&q=자동차&udm=2&fbs=ABzOT_CZsxZeNKUEEOfuRMhc2yCIle3NjqrdI1yz4YBXXweAYROj_ssEdoGUqgqRO4_tQus9UEXRd2cQ6AZUANa6BbAL1BU7uUFls7Lcvyhg4fvOA3MiCQJuDM1QEmowX4VlAldt43rBQKXNdhn9pZsUq1UEix9FiYEkRHJhZE_NDfjrGTOIC7Oe4sAfBs8WiNj9NARzX9Yi&sa=X&ved=2ahUKEwijianMl8CLAxUdr1YBHTKkO20QtKgLegQIExAB&biw=1440&bih=812&dpr=2'
target_url = base_url + sub_url

# 이미지를 저장할 디렉토리 이름
save_dir_name = 'download'

curpath = os.path.dirname(__file__)
save_dir_path = os.path.join(curpath, save_dir_name)
print("저장된 이미지 디렉토리 경로:", save_dir_path)

# 디렉토리가 없으면 생성
if not os.path.exists(save_dir_path):
    os.makedirs(save_dir_path)

# ChromeDriver 다운로드
chrome_driver = ChromeDriverManager().install()
# WebDriver 초기화
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)

try:
    # 웹 페이지 로드
    driver.get(target_url)
    time.sleep(5)  # 페이지가 완전히 로드될 때까지 대기

    # 모든 이미지 태그 찾기
    images = driver.find_elements(By.CLASS_NAME, 'YQ4gaf')

    # 이미지 다운로드
    for img in images:
        img_url = img.get_attribute('src')
        if not img_url:
            continue

        try:
            # data: 로 시작하는 경우, data URL 이므로 base64로 디코딩 이후 다운로드
            if img_url.startswith("data:"):
                # 데이터가 "data:image/png;base64,"으로 시작하므로, 해당 내용을 제거하여 Base64 데이터만 추출
                header, encoded = img_url.split(",", 1)
                # Base64 디코딩
                image_data = base64.b64decode(encoded)
                # 이미지 파일 저장
                extension = header.split('/')[1].split(';')[0]
                random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                filename = random_name + "." + extension
                with open(os.path.join(save_dir_path, filename), 'wb') as f:
                    f.write(image_data)
                continue

            # 상대 경로인 경우 절대 URL로 변환
            if not img_url.startswith(('http://', 'https://')):
                img_url = '/'.join([base_url, img_url])

                # 이미지 데이터 가져오기
                print("img_url", img_url)
                img_response = requests.get(img_url)
                img_response.raise_for_status()  # HTTP 에러가 있는 경우 예외 발생

                # 파일 이름 추출
                img_name = os.path.basename(img_url.split('?')[0])  # 쿼리 스트링 제거
                img_path = os.path.join(save_dir_path, img_name)

                # 이미지 파일 저장
                with open(img_path, 'wb') as f:
                    f.write(img_response.content)
                print(f"Downloaded {img_url} to {img_path}")

        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

finally:
    driver.quit()