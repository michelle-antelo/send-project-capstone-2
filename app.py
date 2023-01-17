from flask import Flask, render_template
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

holds = {"jug": {"def": "handle bars"},
        "crimp": {"def": "small"},
        "sloper": {"def": "slippery"}}

class Climbing(Resource):
    def get(self, hold):
        return holds[hold]

api.add_resource(Climbing, "/climbing/<string:hold>")

if __name__ == "__app__":
    app.run(debug=True)

@app.route('/')
def homepage():
    return render_template("home.html")