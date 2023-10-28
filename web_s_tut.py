from bs4 import BeautifulSoup
import requests
import time


# _____SCRAPING LOCAL WEBSITE____###########
#
# with open('blog.html', 'r') as html_file:
#     content = html_file.read()
#     print(content)
#
#     soup = BeautifulSoup(content, 'lxml')
#     # soup.prettify())
#     # tags = soup.find_all('li ')
#     # print(tags)
#     post_html_tags = soup.find_all('h3')
#     # print(post_html_tags)
#     for Post in post_html_tags:
#         print(Post.text)
#
# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#     print(content)
#
#     soup = BeautifulSoup(content, 'lxml')
#     # course_html_tags = soup.find_all('h5')
#     # # print(post_html_tags)
#     # for course in course_html_tags:
#     #     print(course.text)
#     course_card = soup.find_all('div', class_='card')
#     for course in course_card:
#         course_name = course.h5.text
#         course_price = course.a.text.split()[-1]
#
#         # print(course_name)
#         # print(course_price)
#
#         print(f"{course_name} costs {course_price}")
#
#
#
#
#
# ################______SCRAPING REAL WEBSITE_____###########

print('Type in some skill that you are not familiar with below:')
unfamiliar_skill = input('>>>>').split()
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    # jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    # print(jobs)
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More Info: {more_info}\n")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting{  time_wait } minutes...')
        time.sleep(time_wait * 60)

