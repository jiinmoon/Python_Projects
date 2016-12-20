from bs4 import BeautifulSoup as bs
import requests, re, sys, webbrowser


def main(args=[]):
    prof_name = '+'.join(args[1].strip().split())
    school_name = ' '.join(args[2].strip().split())
    url = 'http://www.ratemyprofessors.com/search.jsp?query={}'.format(prof_name)
    response = requests.get(url)

    soup = bs(response.text, 'html.parser')

    datas = []

    for prof in soup.find_all('li', class_='listing PROFESSOR'):
        str_prof = str(prof.contents[1])
        link = re.search(r'href=[\'"]?([^\'" >]+)', str_prof).group(1)
        name = re.search(r'class="main">(.*?)</span>', str_prof).group(1)
        school = re.search(r'class="sub">(.*?)</span>', str_prof).group(1)
        datas += [{'name': name[:-1], 'school': school, 'link': link}]
    
    # Prof Check
    if len(datas) == 0:
        print('Cannot be found.')
        exit()
    
    for prof in datas:
        if school_name in prof['school']:
            url = 'http://www.ratemyprofessors.com{}'.format(prof['link'])
            break
        else:
            url = ''
    
    # School Check
    if len(url) == 0:
        print('Cannot be found.')
        exit()
        
    webbrowser.open(url, new=2)
            

if __name__ == '__main__':
    # Argument Check
    if len(sys.argv) < 3:
        print('Usage: python3 find_my_prof.py <Professor Name> <School Name>')
        exit()
        
    main(sys.argv)