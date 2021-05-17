import json
from sanic import Sanic
from sanic.response import json as sjson
app = Sanic("adviser")
PLANS_PATH = 'ready_made_plans'


@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    topic = request.args.get('topic') or 'topic_list'
    sort_func = lambda data: (sorted(data, key=lambda x: x['title']))

    try:
        with open(f'{PLANS_PATH}/{topic}.json', mode='r') as json_file:
            data = json.load(json_file)
            return sjson({'data': sort_func(data)})

    except FileNotFoundError:
        return sjson({'data': []})

#  sanic api.index.app
