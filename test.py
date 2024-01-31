import requests
from bs4 import BeautifulSoup

url = "https://calculator.aws/#/createCalculator/ec2-enhancement?ch=cta&cta=lower-pricing-calc"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
           'Cookie':'AMCVS_7742037254C95E840A4C98A6%40AdobeOrg=1; user-preference-for-region-name=us-east-2; s_cc=true; awsccc=eyJlIjoxLCJwIjoxLCJmIjoxLCJhIjoxLCJpIjoiODkzNDEyNzAtMTA2Zi00YWQwLWE1OTItYjc2YWUzZjdlNWViIiwidiI6IjEifQ==; AMCV_7742037254C95E840A4C98A6%40AdobeOrg=1585540135%7CMCIDTS%7C19754%7CMCMID%7C24584763622477459193864873870386222234%7CMCAAMLH-1707274553%7C11%7CMCAAMB-1707274553%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1706676953s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; awsd2c-token-c=eyJraWQiOiIyMTZhM2UyZC1jNjk3LTRiY2UtOTE5Zi1mY2EzNWE0N2Q4NTAiLCJ0eXAiOiJjb20uYXdzLmFtYXpvbi5kMmMudnMrSldUIiwiYWxnIjoiUlMyNTYifQ.eyJ2aWQiOiI0YWMzYmYyOS04ZDc1LTIyYTktNjMxMS00NWMzN2QwN2RkYTAiLCJpc3MiOiJodHRwczpcL1wvdnMuYXdzLmFtYXpvbi5jb20iLCJtaWQiOiIyNDU4NDc2MzYyMjQ3NzQ1OTE5Mzg2NDg3Mzg3MDM4NjIyMjIzNCIsImV4cCI6MTcwNjY3MDM1NSwiaWF0IjoxNzA2NjY5NzU1fQ.FOLHo4irUI7aEZiq1bAY2M1W_n639WBWdH3iUK1GSfp-_8Kapk98zKPmOWfa6XmjwVV27y2CgcK_EEYt63WozVwPUeCMm1BM_rHxBJdhyZN_zqnz8MoIKYDCDruCSiBMXrJGsm0SMuiX2rKRsMdRmoldzYlMyXeXeRv9IEg-ynej5W07v7dTbpJpQm3eFrvvulgui_fBVdZGTTmHAtOSFZrejhU5_JNYst02NUmU32mc5X2Yok9oAVjnjzpo64BKhAtOuDD1NIyPA-xEqX43_a0QcH6RyuhwV-Fj_L0PclyxsPaVfcGMPNArSgKwwH7qxOq9jrWyE5aHaF90_eVbnQ; s_sq=%5B%5BB%5D%5D'}
response = requests.get(url, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
print(soup.find('div',id='root'))