import os
import json

import requests

__here__ = os.path.dirname(os.path.abspath(__file__))

def generate_demo():
    res = requests.get('http://localhost:8000/rest_api/leaguestats/314488/')
    data = eval(res.content)
    demo_path = os.path.join(__here__, 'static', 'json', 'demo.json')
    with open(demo_path, 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    generate_demo()
