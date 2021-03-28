import nltk
from bs4 import BeautifulSoup as bs
import requests

transcript = ''
# download webpage
# url = 'https://ufl.zoom.us/rec/play/LzMDLeJHv2Jid0cU37Nr39Q6gwX7NKfrF5uCd9fgxANJIA7olzwLxHZVihpdjmRTfnfs8bCvbjyVDMJc.3B9SJWh-A5VrRSbm'
# r = requests.get(url, allow_redirects=True)
# open('transcript.html', 'wb').write(r.content)
transcript += open('transcript.html', 'r').read()


def createTranscript(raw: str):
    soup = bs(transcript, 'html.parser')
    transcript_list = soup.find_all('ul', {'class': 'transcript-list'})[0]
    for item in transcript_list.contents:
        a = item['aria-label'].split(',')[2:]
        speech = ''.join(a)
        print(speech)
        timeline = item.find_all('div', {'class': 'timeline'})[0]
        time = timeline.find_all('span', {'class': 'time'})[0].string
        print(time)

