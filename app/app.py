import csv

from flask import (
    Flask,
    render_template
)

zevents = []

with open('Z-challenge.csv', 'r') as zcsv:
    csv_reader = csv.reader(zcsv)
    next(csv_reader, None)

    for fn, eid in csv_reader:
        zevents.append(
            {
                'file_name': fn,
                'event_id': eid
            }
        )

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def main():
        return render_template(
            'index.html',
            events=zevents
        )

    return app
