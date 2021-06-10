import os
import json
import re

'''
Go through the data directory and parse run and event
information etc. from the file names and write out to json.

Also for each run_event combination write out the corresponding
files available for it. 

Also determine how many files we have and how many are
unique.

'''

base_dir = os.path.abspath('../')
data_dir = os.path.join(base_dir, 'app', 'static', 'data')

files = []
events = {}

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

    run_event = f'{run}_{event}'

    if run_event in events:
        events[run_event].append(gif)
    else:
        events[run_event] = [gif]
    
    files.append({
        'run': run,
        'event': event,
        'file_name': gif,
        'view': view,
        'type': '',
    })
    
files_file_name = 'files.json'
    
json.dump(
    files,
    open(files_file_name, 'w'),
    sort_keys=True,
    indent=4
)

events_file_name = 'events.json'

json.dump(
    events,
    open(events_file_name, 'w'),
    sort_keys=True,
    indent=4
)

print(
    f'Results written to {files_file_name} and {events_file_name}'
)

print(
    len(files),
    'event files'
)

print(
    len(events),
    'unique events'
)
