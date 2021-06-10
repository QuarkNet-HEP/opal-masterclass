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
            title='Introduction',
        )

    app.add_url_rule('/detector', 'detector', detector)

    
    @app.route('/challenge1')
    def challenge1():
        return render_template(
            'introduction.html',
            title='Challenge 1',
        )
    
    app.add_url_rule('/challenge1', 'challenge1', challenge1)

    
    @app.route('/challenge2')
    def challenge2():
        return render_template(
            'introduction.html',
            title='Challenge 2',
        )
    
    app.add_url_rule('/challenge2', 'challenge2', challenge2)

    
    @app.route('/challenge3')
    def challenge3():
        return render_template(
            'introduction.html',
            title='Challenge 3',
        )
    
    app.add_url_rule('/challenge3', 'challenge3', challenge3)

    
    @app.route('/challenge4')
    def challenge4():
        return render_template(
            'introduction.html',
            title='Challenge 4',
        )
    
    app.add_url_rule('/challenge4', 'challenge4', challenge4)

    
    @app.route('/challenge5')
    def challenge5():
        return render_template(
            'introduction.html',
            title='Challenge 5',
        )
    
    app.add_url_rule('/challenge5', 'challenge5', challenge5)

    
    @app.route('/others')
    def others():
        return render_template(
            'introduction.html',
            title='Others',
        )
    
    app.add_url_rule('/others', 'others', others)

    
    @app.route('/Z')
    def Z():
        return render_template(
            'introduction.html',
            title='Z'
        )
    
    @app.route('/W')
    def W():
        return render_template(
            'introduction.html',
            title='W'
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
