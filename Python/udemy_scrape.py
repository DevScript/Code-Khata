from bs4 import BeautifulSoup  #Importing the Beautiful Soup Library
import requests                #Importing the requests library
import time                    #Importing the time library
import csv                     #Importing the csv module
import json                    #Importing the JSON library

host = 'https://www.udemy.com'  #create website url for the site you want to search for
courses_api_endpoint = '/api-2.0/discovery-units/all_courses/?p=1&page_size=16&category_id=%d&source_page=category_page&locale=en_US&currency=eur&navigation_locale=en_US&skip_price=true&sos=pc&fl=cat'   #creating course api end point
prices_api_endpoint = '/api-2.0/pricing/?course_ids=%s&fields[pricing_result]=price'     #creating price point endpoint
headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)'}   #creating headers for the api for HTTPS data

response = requests.get(host, headers=headers)      #getting the response from the udemy website
front_page_soup = BeautifulSoup(response.text, 'lxml') #using beautiful soup object creating lxml file of the response
top_categories = front_page_soup.select('a[data-purpose="category-card-title-link"]')   #selecting the required data for writing to the csv file

with open('udemy.csv', 'w') as file:
    write = csv.writer(file)
    write.writerow(['No.',
                    'Category',
                    'URL',
                    'Name',
                    'Description',
                    'Author',
                    'Rating',
                    'Price',
                    ])             #creating the udemy.csv file in write row and specify the header(first row) names using writerow function
    index = 0
    for top_category in top_categories:      
        category_name = top_category.text
        category_url = host + top_category['href']     #Looping through top categories course list file to get the name and url of the category

        response = requests.get(category_url, headers=headers)  #The url of the course category is taken to get the course name
        category_soup = BeautifulSoup(response.text, 'lxml')   #using beautiful soup object creating lxml file of the response
        page_object = json.loads(category_soup.find('div', class_='ud-component--category--category')['data-component-props'])  #converting the json string to python dictionary
        category_id = page_object['pageObject']['id']   #finding id element from the python dictionary

        response = requests.get(host + courses_api_endpoint % category_id, headers=headers) #creating a request with the host course end point and category id to get the courses
        data = json.loads(response.text)  #converting the json string to python dictionary
        courses = data['unit']['items']   #finding elements in the python dictionary
        courses_list = []
        ids = []
        for course in courses:
            index += 1
            id = str(course['id'])
            name = course['title']
            url = host + course['url']
            description = course['headline']
            rating = course['rating']
            author = ', '.join([instructor['display_name'] for instructor in course['visible_instructors']])
            courses_list.append([index, category_name, url, name, description, author, rating, ''])
            ids.append(id)                                                                                 #finding all the details about the course by looping through the dictionary file
        
        ids_str = ','.join(ids)
        response = requests.get(host + prices_api_endpoint % ids_str, headers=headers)
        data = json.loads(response.text)
        prices = data['courses']
        for i in range(len(ids)):
            courses_list[i][-1] = prices[ids[i]]['price']['price_string']

        write.writerows(courses_list)                                                                    #writing rows of the data obtained to the csv file generated in the start of the file
