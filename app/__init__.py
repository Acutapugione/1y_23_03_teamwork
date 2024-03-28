from flask import Flask

app = Flask(__name__)




from . filters import price_format
from . import routes

for rule in app.url_map.iter_rules():
    print(rule.endpoint)