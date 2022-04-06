from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis")

@app.route("/")
def hello():
    visits = redis.incr('counter')
    html = "<h3>This is the {visits} </h3>" \
           "<br/>"
    return html.format(visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
