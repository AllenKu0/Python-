import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ec2_json_detail= []
# ec2_item = {
#     1 : '執行個體名稱',
#     2 : '執行個體系列',
#     3 : '執行個體類別',
#     4 : 'vCPU',
#     5 : '記憶體',
#     6 : '網路效能',
#     7 : '儲存',
#     8 : '隨需每小時成本',
#     9 : 'CurrentGeneration',
#     10 : 'Potential saving',
# }

ec2_item = {
    1 : 'InstanceName',
    2 : 'InstanceFamily',
    3 : 'InstanceType',
    4 : 'vCPU',
    5 : 'Memory',
    6 : 'Network',
    7 : 'Storage',
    8 : 'OnDemandHourlyCost',
    9 : 'CurrentGeneration',
    10 : 'Potential saving',
}

def get_source_with_soup(driver):
    pagesource = driver.page_source
    soup = BeautifulSoup(pagesource, 'html.parser')
    return soup

def get_ec2_instance_detail():
    driver = webdriver.Chrome("D:\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    driver.get("https://calculator.aws/#/createCalculator/ec2-enhancement")
    while True:
        try:
            for i in range(1, 3):
                # button = driver.find_element(By.XPATH, f'//button[@aria-label="所有頁面的第 {i} 頁"]')
                # button.click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//button[@aria-label="所有頁面的第 {i} 頁"]'))).click()
                if get_source_with_soup(driver).find('body').tbody.find('tr').find('td').text == "正在載入執行個體正在載入執行個體":
                    raise Exception("正在載入執行個體正在載入執行個體")
                ec2_instances = get_source_with_soup(driver).find('body').tbody.find_all('tr')
                for ec2 in ec2_instances:
                    ec2_json_tmp= {}
                    item = 1
                    for ec2_detail in ec2.find_all('td'):
                        if ec2_detail.text != '' and ec2_detail.span == None:
                            ec2_json_tmp[ec2_item[item]] = ec2_detail.text
                            item+=1
                    ec2_json_detail.append(ec2_json_tmp)
            break
        except Exception as e:
            print(e)
            continue
    return json.dumps(ec2_json_detail,indent=2,ensure_ascii=False)