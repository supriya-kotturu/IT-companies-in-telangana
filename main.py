from asyncore import read
from bs4 import BeautifulSoup

import csv
import requests

file = open('company_details.csv', 'w', newline="")
writer = csv.writer(file)
## GOOGLE MAPS

# url = "https://www.google.com/maps/search/IT+companies+in+telangana/@17.4823792,78.3920811,13z/data=!3m1!4b1"
# html_text = requests.get(url).text

# # with open('test.html','r') as html_file:
# # content = html_text.read()

# soup = BeautifulSoup(html_text, 'lxml')
# big_cards = soup.find_all('div') #('div', class_="V0h1Ob-haAclf gd9aEe-LQLjdd OPZbO-KE6vqe")
#  #cXedhc
# print(big_cards)

# for card in big_cards : 
#     company_cards = soup.find_all("div", class_='CUwbzc-content gm2-body-2')
#     print(card)
#     for company in company_cards:
#         company_name = company.find('div', class_="qBF1Pd-haAclf").find("div", class_='qBF1Pd gm2-subtitle-alt-1').span.text
#         company_address_card = company.find_all('div', class_="ZY2y6b-RWgCYc")[1]
#         company_address = company_address_card.find_all('span')[7].text
#         company_phone = company_address_card.find_all('span')[19].text
#         print(company_name, "IS AT", company_address, "CONTACT", company_phone )

## NAUKRI PAGE

company_details= []

for i in range(1,5) :
    url=("https://www.naukri2000.com/careers/it_hyderabad.php?pageno=%d" %i)
    html_text= requests.get(url).text
    s= BeautifulSoup(html_text, 'lxml')

    # with open('test.html', 'r') as html_file:
    # s = BeautifulSoup(html_file, 'lxml')
    companies = s.find_all('tr')

    for company in companies :
        try :
            if(company.find('a')):
                company_name = company.find('a').text
                company_address= company.find_all('td')[2].text
                company_details.append([company_name.replace(',','').capitalize().strip(),company_address.capitalize().strip()])
        except IndexError:
            continue

for company_detail in company_details:
    if(company_detail[0] == 'Home' or company_detail[1] == '' or company_detail[0] == 'Here' or company_detail[1] == '#'):
        continue
    else:
        writer.writerow(company_detail)
   


## PIN-CODE.org

for i in range(1,445) :
    url=("https://pin-code.org.in/companies/listing/telangana/page:%d" %i)
    html_text= requests.get(url).text
    s= BeautifulSoup(html_text, 'lxml')

    # with open('test.html', 'r') as html_file:
    # s = BeautifulSoup(html_file, 'lxml')
    companies = s.find_all('div', class_="boxDetails bg-white p-3 mt-3")

    for company in companies :
        try :
            if(company.find('a')):
                company_name = company.find('h5').text.lower()
                company_address= company.find('p').text
                # company_details.append("%s$$ ;%s" %(company_name.replace(',','').strip(), company_address.strip()))
                company_details.append([company_name.replace(',','').capitalize().strip(),company_address.replace('Contact Address: ','').replace('Company ', '').capitalize().strip()])
        except IndexError:
            continue

for company_detail in company_details:
    if(company_detail[0] == 'Home' or company_detail[1] == '' or company_detail[0] == 'Here' or company_detail[1] == '#'):
        continue
    else:
        writer.writerow(company_detail)

print("Collected %d companies and their addresses!" %(len(company_details)))

file.close()

