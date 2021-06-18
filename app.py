import csv
import json

from flask import (
    Flask,
    render_template
)

from flask_bootstrap import (
    Bootstrap
)

app = Flask(__name__)
bootstrap = Bootstrap(app)

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

@app.route('/acknowledgements')
def acknowledgements():
    return render_template(
        'acknowledgements.html',
        title='Acknowledgements'
    )

@app.route('/contents')
def contents():
    return render_template(
        'contents.html',
        title='Contents'
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
        ch='ch1',
        challenge='challenge1',
        nevents=len(challenge1_events)+1,
        back_id=int(id)-1,
        next_id=int(id)+1,
        options=['electron', 'muon', 'hadron'],
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
        ch='ch2',
        challenge='challenge2',
        nevents=len(challenge2_events)+1,
        back_id=int(id)-1,
        next_id=int(id)+1,
        options=['ee', 'mumu', 'tautau', 'qq'],
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
        ch='ch3',
        challenge='challenge3',
        nevents=len(challenge3_events)+1,
        back_id=int(id)-1,
        next_id=int(id)+1,
        options=['enuqq', 'munuqq', 'taunuqq', 'qqqq', 'lnulnu'],
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
        ch='ch4',
        challenge='challenge4',
        nevents=len(challenge4_events)+1,
        back_id=int(id)-1,
        next_id=int(id)+1,
        options=[
            'ee', 'mumu', 'tautau', 'qq',
            'enuqq', 'munuqq', 'taunuqq', 'qqqq', 'lnulnu'
        ],
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
        ch='ch5',
        challenge='challenge5',
        nevents=len(challenge5_events)+1,
        back_id=int(id)-1,
        next_id=int(id)+1,
        options=[
            'ee', 'mumu', 'tautau', 'qq',
            'enuqq', 'munuqq', 'taunuqq', 'qqqq', 'lnulnu',
            'ffgamma', 'qqg', 'ffff'
        ],
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
        'zdecays.html',
        title='Measuring Z decays',
        events=zevents,
    )

@app.route('/Wdecays')
def Wdecays():
    return render_template(
        'wdecays.html',
        title='Measuring W decays',
        events=wevents,
    )

@app.route('/Zdecays/<id>')
def zevent(id):
    return render_template(
        'event.html',
        title=f'Z Measurement: Event {id}',
        nevents=1000, # There are duplicates in Z dataset. Investigate.
        dataset='zevent',
        measurement='Zdecays',
        back_id=int(id)-1,
        next_id=int(id)+1,
        event=list(filter(lambda e: e["event_id"] == id, zevents))[0]
    )

@app.route('/Wdecays/<id>')
def wevent(id):    
    return render_template(
        'event.html',
        title=f'W Measurement: Event {id}',
        nevents=479, # There are duplicates in the W dataset (end and side views).
        dataset='wevent',
        measurement='Wdecays',
        back_id=int(id)-1,
        next_id=int(id)+1,
        event=list(filter(lambda e: e["event_id"] == id, wevents))[0]
    )

@app.route('/factor')
def factor():
    return render_template(
        'factor.html',
        title='Correction Factor for e+e- Events',
        header='Correction Factor for \(e^{+}e^{-}\) Events'
    )

@app.route('/stat')
def stat():
    return render_template(
        'stat.html',
        title='Some Hints on Statistical Errors'
    )

@app.route('/Z/mumu')
def mumu():
    return render_template(
        'mumu.html',
        title='Example mu+mu- Events',
        header='Example \(\mu^{+}\mu^{-}\) Events'
    )

@app.route('/Z/ee')
def ee():
    return render_template(
        'ee.html',
        title='Example e+e- Events',
        header='Example \(e^{+}e^{-}\) Events'
    )
    
@app.route('/Z/tautau')
def tautau():
    return render_template(
        'tautau.html',
        title='Example tau+tau- Events',
        header='Example \(\\tau^{+}\\tau^{-}\) Events'
    )
    
@app.route('/Z/qq')
def qq():
    return render_template(
        'qq.html',
        title='Example qq Events',
        header='Example \(q\\bar{q}\) Events'
    )

@app.route('/W/qqqq')
def qqqq():
    return render_template(
        'qqqq.html',
        title='Example qqqq Events',
        header='Example \(q\\bar{q}q\\bar{q}\) Events'
    )

@app.route('/W/lnulnu')
def lnulnu():
    return render_template(
        'lnulnu.html',
        title='Example lnulnu Events',
        header='Example \(l^{+}\\nu l^{-}\\bar{\\nu}\) Events'
    )

@app.route('/W/enuqq')
def enuqq():
    return render_template(
        'enuqq.html',
        title='Example enuqq Events',
        header='Example \(e\\bar{\\nu} q\\bar{q} \) Events'
    )

@app.route('/W/munuqq')
def munuqq():
    return render_template(
        'munuqq.html',
        title='Example munuqq Events',
        header='Example \(\mu\\bar{\\nu} q\\bar{q} \) Events'
    )

@app.route('/W/taunuqq')
def taunuqq():
    return render_template(
        'taunuqq.html',
        title='Example taunuqq Events',
        header='Example \(\\tau\\bar{\\nu} q\\bar{q} \) Events'
    )

@app.route('/others/ffgamma')
def ffgamma():
    return render_template(
        'ffgamma.html',
        title='High Energy Photons in Events Containing a Particle-Antiparticle Pair'
    )

@app.route('/others/qqg')
def qqg():
    return render_template(
        'qqg.html',
        title='High Energy Gluons in Events Containing a Quark-Antiquark Pair'
    )

@app.route('/others/ffff')
def ffff():
    return render_template(
        'ffff.html',
        title='Four Fermion Events'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

