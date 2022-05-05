"""Demonstration of Google Maps."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, jsonify, send_from_directory
from model import connect_to_db, db, Bear

app = Flask(__name__)
app.config["SECRET_KEY"] = "ursusmaritimus"
app.jinja_env.undefined = StrictUndefined

#---------------------------------------------------------------------#

@app.route("/")
def index():
    """Show homepage."""

    return render_template("index.html")

@app.route("/map/basic")
def view_basic_map():
    """Demo of basic map-related code.

    - Programmatically adding markers, info windows, and event handlers to a
      Google Map
    - Showing polylines, directions, etc.
    """

    return render_template("map-basic.html")


@app.route("/map/more")
def view_more_demos():
    """Demo of basic map-related code.

    - Programmatically adding markers, info windows, and event handlers to a
      Google Map
    - Showing polylines, directions, etc.
    """

    return render_template("map-more.html")


@app.route("/map/bears")
def view_bear_map():
    """Show map of bears."""

    return render_template("map-bears.html")


@app.route("/api/bears")
def bear_info():
    """JSON information about bears."""

    bears = [
        {
            "id": bear.marker_id,
            "bearId": bear.bear_id,
            "gender": bear.gender,
            "birthYear": bear.birth_year,
            "capYear": bear.cap_year,
            "capLat": bear.cap_lat,
            "capLong": bear.cap_long,
            "collared": bear.collared.lower()
        }
        for bear in Bear.query.limit(50)
    ]

    return jsonify(bears)


#- BORING DEMO CONFIG STUFF ------------------------------------------#
#---------------------------------------------------------------------#

@app.route("/map/static/<path:resource>")
def get_resource(resource):
    return send_from_directory("static", resource)


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)

    app.run(host="0.0.0.0")
