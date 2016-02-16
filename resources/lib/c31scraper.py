from bs4 import BeautifulSoup as bs
import requests
import re


def get_soup(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

    return soup


def get_content(url):
    soup = get_soup(url)
    content = soup.find_all('div', {'class': 'shelf-wrapper clearfix'})
    
    output = []
    for i in content:
        label = i.find('span', {'class': 'branded-page-module-title-text'}).get_text()
        
        if 'Uploads' or 'Popular uploads'  in label:
            found_content = i.find_all('div', {'class': 'yt-lockup-dismissable'})
            
            for k in found_content:
                label_path = k.find('h3', {'class': 'yt-lockup-title '})
                label = label_path.find('a').get('title')

                path = label_path.find('a').get('href')
                path = re.search(r'\=(.*)', path).group(0)

                thumb = k.find('img')['data-thumb']
                thumb = 'http:' + thumb
                
                item = {
                    'label': label,
                    'path': path,
                    'thumbnail': thumb,
                }

                output.append(item)

    return output
#get_content('https://www.youtube.com/channel/UCUNfGu0l8O6FvCsuvJFgHOA/videos')
