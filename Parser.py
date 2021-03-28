import nltk
from bs4 import BeautifulSoup as bs
import requests

class Parser:
    def __init__(self, start: str, stop: str):
        self.start = start
        self.stop = stop
        self.raw = ''
        # download webpage
        # url = 'https://ufl.zoom.us/rec/play/LzMDLeJHv2Jid0cU37Nr39Q6gwX7NKfrF5uCd9fgxANJIA7olzwLxHZVihpdjmRTfnfs8bCvbjyVDMJc.3B9SJWh-A5VrRSbm'
        # r = requests.get(url, allow_redirects=True)
        # open('transcript.html', 'wb').write(r.content)
        self.raw += open('transcript.html', 'r').read()
        self.transcript = []
        self.speech = []
        self.times = []

    def create_transcript(self, raw: str):
        soup = bs(raw, 'html.parser')
        transcript_list = soup.find_all('ul', {'class': 'transcript-list'})[0]
        for item in transcript_list.contents:
            a = item['aria-label'].split(',')[2:]
            speech = ''.join(a)
            timeline = item.find_all('div', {'class': 'timeline'})[0]
            time = timeline.find_all('span', {'class': 'time'})[0].string
            self.speech.append(speech)
            self.times.append(time)
            self.transcript.append((time, speech))

    def get_times(self, transcript: list):
        times = []
        start_time = ''
        for speech in self.transcript:
            if self.start in speech[1]:
                start_time = speech[0]
            if self.end in speech[1]:
                times.append((start_time, speech[0]))
        return times


