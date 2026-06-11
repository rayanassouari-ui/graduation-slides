"""
Presentation of Graduates - Flask Web App
-------------------------------------------
Art-deco gold/teal graduation slideshow, deployable on Render.

Run locally:
    pip install -r requirements.txt
    python app.py

Then open http://localhost:5000
"""

from flask import Flask, render_template
import os

app = Flask(__name__)

# ----------------------------------------------------------------------
# STUDENT DATA - Edit this list with your class info!
# "photo" can be:
#   - a URL to an image, e.g. "https://example.com/photo.jpg"
#   - a path to a file in static/photos, e.g. "/static/photos/student1.jpg"
# ----------------------------------------------------------------------
STUDENTS = [
    {
        "name": "Rohid Shamshad",
        "photo": "/static/photos/student1.jpg",
        "school": "Wilbur Cross",
        "description": "Loves basketball, video games, and making everyone laugh in class."
    },
    {
        "name": "Ava Martinez",
        "photo": "/static/photos/student2.jpg",
        "school": "Lincoln High School",
        "description": "Loves art, soccer, and never misses a sunset photo."
    },
    {
        "name": "Liam Chen",
        "photo": "/static/photos/student3.jpg",
        "school": "Riverside High School",
        "description": "Future engineer, robotics club captain, coffee enthusiast (the smell, not the taste)."
    },
]

CLASS_YEAR = "Class of 2026"


@app.route("/")
def index():
    return render_template("index.html", students=STUDENTS, class_year=CLASS_YEAR)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
