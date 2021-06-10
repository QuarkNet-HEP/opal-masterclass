import csv
import os

from flask import (
    Flask,
    render_template
)

csv_dir = os.path.join('./', 'data')

zevents = []
wevents = []


with open(os.path.join(csv_dir, 'Z-challenge.csv'), 'r') as zcsv:
    csv_reader = csv.reader(zcsv)
    next(csv_reader, None)

    for fn, eid in csv_reader:
        zevents.append(
            {
                'file_name': fn,
                'event_id': eid
            }
        )

with open(os.path.join(csv_dir, 'W-challenge.csv'), 'r') as wcsv:
    csv_reader = csv.reader(wcsv)
    next(csv_reader, None)

    for fn, eid in csv_reader:
        wevents.append(
            {
                'file_name': fn,
                'event_id': eid
            }
        )
        
def create_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template(
            'index.html',
            title='OPAL Masterclass',
        )

    @app.route('/Z')
    def z():
        return render_template(
            'events.html',
            title='Z challenge',
            events=zevents,
        )

    @app.route('/W')
    def w():
        return render_template(
            'events.html',
            title='W challenge',
            events=wevents,
        )
    
    app.add_url_rule('/', 'index', index)
    
    app.add_url_rule('/Z', 'Z', z)
    app.add_url_rule('/W', 'W', w)
    
    return app
