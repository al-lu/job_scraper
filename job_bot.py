from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import pyautogui
import time
import csv


# setting driver
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument('--disable-gpu')

# options.add_argument("window-size=398,256")

# creating driver
driver = webdriver.Chrome(options=options)
driver.maximize_window()
url = "https://fi.indeed.com"
driver.get(url)
# searching in a bar
search_bar = driver.find_element_by_name("q")
search_bar.clear()
# type your job, also the location is taken --> ex: data analyst dublin
keyword = "Software developer Oulu"
print("looking for", keyword)
search_bar.send_keys(keyword)
search_bar.send_keys(Keys.RETURN)

driver.current_url


# df = pd.DataFrame(
#     columns=["Title", "Location", "Company"])

# for i in range(0, 10, 10):

# driver.get(
#     "https://fi.indeed.com/jobs?q=junior%20developer%20&l=Oulu&vjk=817b52318deadb9a" + str(i))
# driver.implicitly_wait(5)

# text = "fromage=3"
# element = driver.find_element_by_xpath(
#     '//a[contains(@href, "%s")]' % text).click()

i = 0
while i < 3:

    driver.implicitly_wait(5)

    all_jobs = driver.find_elements_by_class_name('result')
    list_of_lists = []

    for job in all_jobs:

        result_html = job.get_attribute('innerHTML')
        soup = BeautifulSoup(result_html, 'html.parser')
        # list_of_page = []

        try:
            title = soup.find(class_="jobTitle").text
            # list_of_page.append(title)
            print(title)
        except:
            title = ''
            print(title)

        try:
            location = soup.find(class_="companyLocation").text
            # list_of_page.append(location)
            print(location)
        except:
            location = ''
            print(location)

        try:
            company = soup.find(class_="companyName").text.replace(
                "\n", "").strip()
            # list_of_page.append(company)
            print(company)
        except:
            company = ''
            print(company)

        try:
            date = soup.find(class_="date").text
            # list_of_page.append(company)
            print(date)
        except:
            date = ''
            print(date)
        try:
            desc = soup.find(class_="job-snippet").text
            # list_of_page.append(company)
            print(desc)
        except:
            desc = ''
            print(desc)

        jobs = [title, location, company, date, desc]
        list_of_lists.append(jobs)

    with open('filename{}.csv'.format(i), 'w', encoding="utf-8") as file:
        writer = csv.writer(file)
        for row in list_of_lists:
            writer.writerow(row)
    time.sleep(3)
    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    pyautogui.moveTo(710, 540, duration=1)
    time.sleep(2)
    pyautogui.click(710, 540)
    time.sleep(2)
    pyautogui.moveTo(1404, 407, duration=1)
    time.sleep(2)
    pyautogui.click(1404, 407)

    # element = driver.find_element_by_partial_link_text("=Oulu&start=").click()
    # now click on this element using JavaScript
    # self.driver.execute_script("arguments[0].click()", element)
    time.sleep(5)
    i += 1

# driver.find_element_by_class_name('pn').click()
# resultsCol > nav > div > ul > li:nth-child(2) > a

# list_of_lists.append(list_of_page)
# print(list_of_lists)
# # # Creating the DataFrame
# df = pd.DataFrame(list(zip(list_of_lists)), columns=[
#     'title', 'location', 'company'])
# # # Exporting the DataFrame as csv
# df.to_csv('quotes-list.csv', index=True, sep=',')

# saving in csv
# with open("".join([keyword.replace(" ", "-"), ".csv"]), 'w', newline='') as csvfile:
#     fieldnames = ['title', 'location', 'company']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for title, location, company in zip(title, location, company):
#         writer.writerow(
#             {"title": title, "location": location, "company": company})
# print("".join([keyword.replace(" ", "-"), ".csv file available"]))

# try:
#     salary = soup.find(class_="salary").text.replace("\n", "").strip()
#     print(salary)
# except:
#     salary = 'None'
#     print(salary)

# try:
#     sum_div = job.find_elements_by_class_name("summary")[0]
#     sum_div.click()
#     print(sum_div)
# except:
#     close_button = driver.find_elements_by_class_name(
#         "popover-x-button-close")[0]
#     close_button.click()
#     sum_div.click()
# try:
#     jd = driver.find_element_by_css_selector('div#vjs-desc').text
#     print(jd)
# except:
#     print(jd)
#     jd = 'None'

# dataframe = df.append({
#     'Title': title,
#     'Location': location,
#     'Company': company
#     # "Salary": salary,
#     # "Description": jd
# }, True)

# print(dataframe)

# dataframe.to_csv("c.csv", index=False)
