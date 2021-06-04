import os
import json
import re

'''
Go through the data directory and parse run and event
information from the file names and write out to json.

Also determine how many files we have and how many are
unique
'''

events = []

gif_files = [fn for fn in os.listdir('./data') if fn.endswith('.gif')]

for gif in gif_files:

    run_event = gif.split('.')[0].split('_')
    
    run = int(re.sub(r"\D", "", run_event[0]))
    event = int(re.sub(r"\D", "", run_event[1]))
    
    events.append({
        'run': run,
        'event': event,
        'file_name': gif
    })
    
json_file_name = 'opal-gifs.json'
    
json.dump(
    events,
    open(json_file_name, 'w'),
    sort_keys=True,
    indent=4
)

print(
    f'Results written to {json_file_name}'
)
    
event_stats = {}

for e in events:

    run_event = str(e['run'])+'_'+str(e['event'])

    if run_event in event_stats:
        event_stats[run_event] += 1
    else:
        event_stats[run_event] = 1

print(
    len(events),
    'event files'
)

print(
    len(event_stats),
    'unique events'
)
