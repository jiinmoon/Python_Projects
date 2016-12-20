# Webscraping Soups being served in UVic

from bs4 import BeautifulSoup
import requests, re

url = "http://www.uvic.ca/services/food/home/events/current/todays-soups.php"

def main():
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "lxml")

  summary = soup.find("div",{'class':'expand-collapse'})

  places = []
  soups = []
  for s in summary.find_all('h3'):
      text = re.sub('<[^<]+?>', '', str(s))
      places.append(text)
      
  for s in summary.find_all('div'):
      text = re.sub('<[^<]+?>', '', str(s))
      soups.append(text.strip().replace('\n', ', '))
      
  result = [(place, soup) for place, soup in zip(places, soups)]

  for x in result:
    print("Where: [{}] | Soups offered: [{}]".format(x[0], x[1]))

if __name__ == '__main__':
  main()