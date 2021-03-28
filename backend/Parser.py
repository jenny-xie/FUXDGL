from moviepy.editor import *

def splice(start: str, stop: str):
    start = start.lower()
    stop = stop.lower()
    raw = ''
    raw = [x.strip('\n') for x in open('uploads/transcript.vtt', 'r').readlines()]
    raw = [x.lower() for x in raw]
    raw = list(filter(None, raw))
    transcript = []

    count = 0
    time = ''
    speech = ''
    for line in raw[1:]:
        if count == 0:
            time0 = line[:12]
            time1 = line[17:]
            count = 1
        else:
            speech = line
            transcript.append((time0, time1, speech))
            count = 0

    times = []
    start_time = ''
    for speech in transcript:
        if start in speech[2]:
            start_time = speech[0]
        if stop in speech[2]:
            times.append((start_time, speech[1]))

    clip = VideoFileClip('uploads/recording.mp4')
    clips = []
    for segment in times:
        clips.append(clip.subclip(segment[0], segment[1]))
    final = concatenate_videoclips(clips)
    final.write_videofile('spliced.mp4')
    final.close()
    return None