import requests
import re
import json
from bs4 import BeautifulSoup


def scrape_subjects():
    url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-all-departments"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    subjects = []
    for i in soup.findAll('a'):
        if i.parent.name == 'td':
            subjects.append(i.getText())
    return subjects


def scrape_courses_of(subject):
    url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-department&dept=" + subject
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    scraped_courses = []
    for i in soup.findAll('a'):
        if i.parent.name == 'td':
            course_name = i.getText()
            print(course_name)
            if int(course_name.split()[1][0]) <= 4: # Only check undergraduate courses
                scraped_courses.append(i.getText())
    if len(scraped_courses) > 0:
        ugrad_subjects.append(subject)
    return scraped_courses


def scrape_course(course_title):
    url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-course&dept=" + course_title.split()[0] + "&course=" + course_title.split()[1]
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find('h4').getText()
    prereqs = soup.find('p', text=re.compile('^Pre-reqs')).getText()
    coreqs = soup.find('p', text=re.compile('^Co-reqs')).getText()

    course_dict = {
        "code": course_title,
        "url": url,
        "title": title,
        "prereqs": prereqs,
        "coreqs": coreqs
    }
    return course_dict


ugrad_subjects = []
all_courses = []
all_courses_expanded = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Starting UBCCourseScraper')
    print('Scraping subjects')
    all_subjects = scrape_subjects()
    print(all_subjects)
    print('Scraping courses under each subject')
    for subject in all_subjects:
        courses = scrape_courses_of(subject)
        print(courses)
        all_courses.extend(courses)
    print('Scraping characteristics of each course')
    for course in all_courses:
        data = scrape_course(course)
        all_courses_expanded.append(data)
    print('Done scraping, starting JSON dump')
    print(ugrad_subjects)
    print(all_courses)
    with open("ugrad_subjects.json", "w+") as subject_file:
        json.dump(ugrad_subjects, subject_file, indent=6)
    with open("all_courses.json", "w+") as courses_file:
        json.dump(all_courses, courses_file, indent=6)
    with open("all_courses_expanded.json", "w+") as courses_expanded_file:
        json.dump(all_courses_expanded, courses_expanded_file, indent=6)
    print('Done!')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
