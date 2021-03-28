from bs4 import BeautifulSoup as bs
from moviepy.editor import *
import argparse

class Parser:
    def __init__(self, start: str, stop: str):
        self.start = start
        self.stop = stop
        self.raw = ''
        self.raw = [x.strip('\n') for x in open('transcript.txt', 'r').readlines()]
        self.raw = list(filter(None, self.raw))
        self.transcript = []

    def create_transcript(self):
        count = 0
        time = ''
        speech = ''
        for line in self.raw[1:]:
            if count == 0:
                time0 = line[:12]
                time1 = line[17:]
                count = 1
            else:
                speech = line
                self.transcript.append((time0, time1, speech))
                count = 0
                
        # soup = bs(self.raw, 'html.parser')
        # transcript_list = soup.find_all('ul', {'class': 'transcript-list'})[0]
        # for item in transcript_list.contents:
        #     a = item['aria-label'].split(',')[2:]
        #     speech = ''.join(a)
        #     timeline = item.find_all('div', {'class': 'timeline'})[0]
        #     time = timeline.find_all('span', {'class': 'time'})[0].string
        #     self.speech.append(speech)
        #     self.times.append(time)
        #     self.transcript.append((time, speech))

    def get_times(self, transcript: list):
        times = []
        start_time = ''
        for speech in self.transcript:
            if self.start in speech[2]:
                start_time = speech[0]
            if self.stop in speech[2]:
                times.append((start_time, speech[1]))
                print(start_time, speech[1])
        print(times)
        return times

    def splice(self, times: list):
        clip = VideoFileClip('recording.mp4')
        clips = []
        for segment in times:
            clips.append(clip.subclip(segment[0], segment[1]))
        final = concatenate_videoclips(clips)
        final.write_videofile('spliced.mp4')

if __name__ == "__main__":
    # parse = argparse.ArgumentParser()
    #
    # parse.add_argument('start', type = str)
    # parse.add_argument('end', type=str)
    # args = parse.parse_args()

    splice = Parser("Argent", "dainty")
    splice.splice(splice.get_times(splice.create_transcript()))
