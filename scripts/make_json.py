import os
import json
import re

'''
Go through the data directory and parse run and event
information etc. from the file names and write out to json.

Also determine how many files we have and how many are
unique.

'''

base_dir = os.path.abspath('../')
data_dir = os.path.join(base_dir, 'app', 'static', 'data')

events = []

gif_files = [fn for fn in os.listdir(data_dir) if fn.endswith('.gif')]

for gif in gif_files:
    
    run_event = gif.split('.')[0].split('_')
    
    view = ''

    if 'side' in gif:
        view = 'side'
    elif 'end' in gif:
        view = 'end'
    elif 's' in run_event[0]:
        view = 'side'
    elif 'x' in run_event[0]:
        view = 'end'
    else:
        view = 'end'
    
    run = int(re.sub(r"\D", "", run_event[0]))
    event = int(re.sub(r"\D", "", run_event[1]))
    
    events.append({
        'run': run,
        'event': event,
        'file_name': gif,
        'view': view,
    })
    
json_file_name = 'data.json'
    
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
