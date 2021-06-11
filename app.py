import csv
import os
import json

from flask import (
    Flask,
    render_template
)

data_dir = os.path.join(
    os.path.abspath('./'),
    'data'
)

zevents = []
wevents = []

with open(os.path.join(data_dir, 'Z-challenge.csv'), 'r') as zcsv:
    csv_reader = csv.reader(zcsv)
    next(csv_reader, None)

    for fn, eid in csv_reader:
        zevents.append(
            {
                'file_name': fn,
                'event_id': eid
            }
        )

with open(os.path.join(data_dir, 'W-challenge.csv'), 'r') as wcsv:
    csv_reader = csv.reader(wcsv)
    next(csv_reader, None)

    for fn, eid in csv_reader:
        wevents.append(
            {
                'file_name': fn,
                'event_id': eid
            }
        )

challenge1_events = json.load(
    open(os.path.join(data_dir, 'challenge1.json'), 'r')
)

challenge2_events = json.load(
    open(os.path.join(data_dir, 'challenge2.json'), 'r')
)

challenge3_events = json.load(
    open(os.path.join(data_dir, 'challenge3.json'), 'r')
)

challenge4_events = json.load(
    open(os.path.join(data_dir, 'challenge4.json'), 'r')
)

challenge5_events = json.load(
    open(os.path.join(data_dir, 'challenge5.json'), 'r')
)

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template(
            'index.html',
            title='OPAL Masterclass',
        )
        
    app.add_url_rule('/', 'index', index)

    
    @app.route('/intro')
    def intro():
        return render_template(
            'introduction.html',
            title='Introduction',
        )
        
    app.add_url_rule('/intro', 'intro', intro)

    
    @app.route('/detector')
    def detector():
        return render_template(
            'detector.html',
            title='The OPAL Detector',
        )

    app.add_url_rule('/detector', 'detector', detector)

    
    @app.route('/challenge1')
    def challenge1():
        return render_template(
            'challenge1.html',
            title='Challenge 1',
            events=challenge1_events
        )
    
    app.add_url_rule('/challenge1', 'challenge1', challenge1)

    
    @app.route('/challenge2')
    def challenge2():
        return render_template(
            'challenge2.html',
            title='Challenge 2',
            events=challenge2_events
        )
    
    app.add_url_rule('/challenge2', 'challenge2', challenge2)

    
    @app.route('/challenge3')
    def challenge3():
        return render_template(
            'challenge3.html',
            title='Challenge 3',
            events=challenge3_events
        )
    
    app.add_url_rule('/challenge3', 'challenge3', challenge3)

    
    @app.route('/challenge4')
    def challenge4():
        return render_template(
            'challenge4.html',
            title='Challenge 4',
            events=challenge4_events
        )
    
    app.add_url_rule('/challenge4', 'challenge4', challenge4)

    
    @app.route('/challenge5')
    def challenge5():
        return render_template(
            'challenge5.html',
            title='Challenge 5',
            events=challenge5_events
        )
    
    app.add_url_rule('/challenge5', 'challenge5', challenge5)

    
    @app.route('/others')
    def others():
        return render_template(
            'others.html',
            title='How to Identify Some Slightly More Complicated Types of Events',
        )
    
    app.add_url_rule('/others', 'others', others)

    
    @app.route('/Z')
    def Z():
        return render_template(
            'Z.html',
            title='How to Identify Events Containing a Particle-Antiparticle Pair'
        )
    
    @app.route('/W')
    def W():
        return render_template(
            'W.html',
            title='How to Identify Events Containing a Pair of W Particles'
        )
    
    @app.route('/Zdecays')
    def Zdecays():
        return render_template(
            'events.html',
            title='Z challenge',
            events=zevents,
        )

    @app.route('/Wdecays')
    def Wdecays():
        return render_template(
            'events.html',
            title='W challenge',
            events=wevents,
        )


    app.add_url_rule('/Z', 'Z', Z)
    app.add_url_rule('/W', 'W', W)
    
    app.add_url_rule('/Zdecays', 'Zdecays', Zdecays)
    app.add_url_rule('/Wdecays', 'Wdecays', Wdecays)
    
    return app
