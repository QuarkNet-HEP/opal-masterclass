import csv
import json

from flask import (
    Flask,
    render_template
)

app = Flask(__name__)

zevents = []
wevents = []

with app.open_resource('data/Z-challenge.csv', mode='rt') as zcsv:
    csv_reader = csv.reader(zcsv)
    next(csv_reader, None)
    
    for fn, eid in csv_reader:
        zevents.append(
            {
                'file_name': fn,
                'event_id': eid
            }
        )

with app.open_resource('data/W-challenge.csv', mode='rt') as wcsv:
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
    app.open_resource('data/challenge1.json')
)

challenge2_events = json.load(
    app.open_resource('data/challenge2.json')
)

challenge3_events = json.load(
    app.open_resource('data/challenge3.json')
)

challenge4_events = json.load(
    app.open_resource('data/challenge4.json')
)

challenge5_events = json.load(
    app.open_resource('data/challenge5.json')
)

@app.route('/')
def index():
    return render_template(
        'index.html',
        title='OPAL Masterclass',
    )
    
@app.route('/intro')
def intro():
    return render_template(
        'introduction.html',
        title='Introduction',
    )
    
@app.route('/detector')
def detector():
    return render_template(
        'detector.html',
        title='The OPAL Detector',
    )
    
@app.route('/challenge1')
def challenge1():
    return render_template(
        'challenge1.html',
        title='Challenge 1',
        events=challenge1_events
    )

@app.route('/challenge1/<id>')
def ch1(id):
    return render_template(
        'side_end.html',
        title=f'Challenge 1: Event {id}',
        event=list(filter(lambda e: e["id"] == int(id), challenge1_events))[0]
    )

@app.route('/challenge2')
def challenge2():
    return render_template(
        'challenge2.html',
        title='Challenge 2',
        events=challenge2_events
    )

@app.route('/challenge2/<id>')
def ch2(id):
    return render_template(
        'side_end.html',
        title=f'Challenge 2: Event {id}',
        event=list(filter(lambda e: e["id"] == int(id), challenge2_events))[0]
    )

@app.route('/challenge3')
def challenge3():
    return render_template(
        'challenge3.html',
        title='Challenge 3',
        events=challenge3_events
    )

@app.route('/challenge3/<id>')
def ch3(id):
    return render_template(
        'side_end.html',
        title=f'Challenge 3: Event {id}',
        event=list(filter(lambda e: e["id"] == int(id), challenge3_events))[0]
    )

@app.route('/challenge4')
def challenge4():
    return render_template(
        'challenge4.html',
        title='Challenge 4',
        events=challenge4_events
    )

@app.route('/challenge4/<id>')
def ch4(id):
    return render_template(
        'side_end.html',
        title=f'Challenge 4: Event {id}',
        event=list(filter(lambda e: e["id"] == int(id), challenge4_events))[0]
    )

@app.route('/challenge5')
def challenge5():
    return render_template(
        'challenge5.html',
        title='Challenge 5',
        events=challenge5_events
    )

@app.route('/challenge5/<id>')
def ch5(id):
    return render_template(
        'side_end.html',
        title=f'Challenge 5: Event {id}',
        event=list(filter(lambda e: e["id"] == int(id), challenge5_events))[0]
    )

@app.route('/others')
def others():
    return render_template(
        'others.html',
        title='How to Identify Some Slightly More Complicated Types of Events',
    )
    
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

@app.route('/mumu')
def mumu():
    return render_template(
        'mumu.html',
        title='Example mu+mu- Events'
    )

@app.route('/ee')
def ee():
    return render_template(
        'ee.html',
        title='Example e+e- Events'
    )
    
@app.route('/tautau')
def tautau():
    return render_template(
        'tautau.html',
        title='Example tau+tau- Events'
    )
    
@app.route('/qq')
def qq():
    return render_template(
        'qq.html',
        title='Example qq Events'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

