import json

from flask import Flask, request

app = Flask(__name__)

PLANS_PATH = 'ready_made_plans'

# @app.route('/')
# def home():
#     return 'Home Page Route'


# @app.route('/about')
# def about():
#     return 'About Page Route'


# @app.route('/portfolio')
# def portfolio():
#     return 'Portfolio Page Route'


# @app.route('/contact')
# def contact():
#     return 'Contact Page Route'


@app.route('/api')
def api():
    topic = request.args.get('topic')
    sort_func = lambda data: (sorted(data, key=lambda x: x['title']))

    if topic is None:
        topic = 'topic_list'
        sort_func = lambda data: (sorted(data.items(), key=lambda x: x[0]))

    try:
        with open(f'{PLANS_PATH}/{topic}.json', mode='r') as json_file:
            data = json.load(json_file)
            return {'data': sort_func(data)}

    except FileNotFoundError:
        return {'data': []}

