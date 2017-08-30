# coding:utf-8
import requests
import re
from bs4 import BeautifulSoup

host_url = "http://www.shiyanlou.com{}"

course_count = 0
study_num = 0

def get_course_link(url):
	res = requests.get('http://www.shiyanlou.com/courses/')
	soup = BeautifulSoup(res.text, 'lxml')
	course = soup.find_all('div', {'class': 'col-md-3', 'class': 'col-sm-6', 'class': 'course'})

	for i in course:
		global course_count
		global study_num
		course_count = course_count + 1
		href = i.find('a', {'class': 'course-box'}).get('href')
		title = i.find('div', {'class': 'course-name'}).get_text()
		study_people = i.find('span', {'class': 'course-per-num', 'class': 'pull-left'}).get_text()
		study_people = re.sub("\D", "", study_people)
		study_num = study_num + int(study_people)
		try:
			tag = i.find('span', {'class': 'course-per-num', 'class': 'pull-right'}).get_text()
		except:
			tag = "Course"
		print("{}    peoples:{}    {}   course link:{}\n".format(tag, study_people, title, host_url.format(href) ))


def main():
	res = requests.get('http://www.shiyanlou.com/courses/')
	soup = BeautifulSoup(res.text, 'lxml')
	course_link = "https:www.shiyanlou.com/courses/?course_type=all&tag=all&fee=all&page={}"
	page = soup.find_all('ul', {'class': 'pagination'})
	if len(page)<1:
		print('Failed to fetch all pages')
		return None
	li_num = page[0].find_all('li')
	page_num = 0

	for i in li_num:
		try:
			li_num = int(i.find('a').get_text())
		except:
			li_num = 0
		if li_num > page_num:
			page_num = li_num

	for i in range(1, page_num + 1):
		get_course_link(course_link.format(i))
if __name__ == "__main__":
	main()
