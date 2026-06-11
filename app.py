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
        "name": "Joel Emiliano Almeida Figueiras",
        "photo": "/static/photos/student1.jpg",
        "school": "Wilbur Cross",
        "description": "To be added.."
    },
    {
        "name": "Monserrat Arenas Martinez",
        "photo": "/static/photos/student2.jpg",
        "school": "Wilbur Cross",
        "description": "To be added..."
    },
    {
        "name": "Iliana Arocho",
        "photo": "/static/photos/student3.jpg",
        "school": "High School in the Community",
        "description": "To be added..."
    },
     {
        "name": "Ahmad Amirzai",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
    {
        "name": "Rayan Assouari",
        "photo": "/static/photos/student3.jpg",
        "school": "High School in the Community",
        "description": "To be added..."
    },
      {
        "name": "Yeimy Carisa Barreda",
        "photo": "/static/photos/student3.jpg",
        "school": "Wilbur Cross",
        "description": "To be added..."
    },
       {
        "name": "Aisake Levon Brandon",
        "photo": "/static/photos/student3.jpg",
        "school": "Career",
        "description": "To be added..."
    },
     {
        "name": "Nicholai Josiah Oponde Brown",
        "photo": "/static/photos/student3.jpg",
        "school": "COMMON GROUND",
        "description": "To be added..."
    },
     {
        "name": "Leeyanna Caple",
        "photo": "/static/photos/student3.jpg",
        "school": "Wilbur Cross",
        "description": "To be added..."
    },
]

CLASS_YEAR = "Class of 2026"


@app.route("/")
def index():
    return render_template("index.html", students=STUDENTS, class_year=CLASS_YEAR)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
