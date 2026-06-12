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
      {
        "name": "Angel Jose Cruz",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
    {
        "name": "Jareliz Dejesus Gonzalez",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
    {
        "name": "Alexis Diaz Gutierrez",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
      {
        "name": "Khalilah Marie Donnelly",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
      {
        "name": "Danna Alejandra Espin",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
     {
        "name": "Leanna Fuster",
        "photo": "https://cdn.discordapp.com/attachments/1460818048654246043/1514748266896691281/714023130_1563359182066744_1274354215665151834_n.png?ex=6a2c7ec1&is=6a2b2d41&hm=8549ecbfe68fa557e58160b211cd563e35a9810fe5df70a53e5233d037acefca&",
        "school": "Wilbur Cross",
        "description": "To be added..."
    },
     {
        "name": "Destiny Lauren Gibbs",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
      {
        "name": "Abel Yamil Gonzalez",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
      {
        "name": "Sean Haynes",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
       {
        "name": "Darianny Elizabeth Hernandez Adames",
        "photo": "/static/photos/student3.jpg",
        "school": "Wilbur Cross",
        "description": "To be added..."
    },
      {
        "name": "Dazani Hough Faulks",
        "photo": "/static/photos/student3.jpg",
        "school": "Metropolitan Business Academy",
        "description": "To be added..."
    },
      {
        "name": "Raima Kalampai",
        "photo": "/static/photos/student3.jpg",
        "school": "CAREER",
        "description": "To be added..."
    },
       {
        "name": "Wilneysha Michelle Lopez Ortiz",
        "photo": "/static/photos/student3.jpg",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
      {
        "name": "Aliana Angela Lopez",
        "photo": "/static/photos/student3.jpg",
        "school": "ELI WHITNEY",
        "description": "To be added..."
    },
    {
        "name": "Jeziel A Martinez",
        "photo": "/static/photos/student3.jpg",
        "school": "WILBUR CROSS",
        "description": "To be added..."
    },
     {
        "name": "Matthew Muniz",
        "photo": "/static/photos/student3.jpg",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
     {
        "name": "Merlyn Anhelis Ninasunta Vegas",
        "photo": "/static/photos/student3.jpg",
        "school": "WILBUR CROSS",
        "description": "To be added..."
    },
     {
        "name": "Roiy Nizami",
        "photo": "/static/photos/student3.jpg",
        "school": "CAREER",
        "description": "To be added..."
    },
    {
        "name": "Luis Ismael Padilla",
        "photo": "/static/photos/student3.jpg",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
      {
        "name": "Sima Paktin",
        "photo": "/static/photos/student3.jpg",
        "school": "CAREER",
        "description": "To be added..."
    },
       {
        "name": "Mannix Eli Pena",
        "photo": "/static/photos/student3.jpg",
        "school": "CAREER",
        "description": "To be added..."
    },
       {
        "name": "Masen Elijah Pena",
        "photo": "/static/photos/student3.jpg",
        "school": "CAREER",
        "description": "To be added..."
    },
      {
        "name": "Cristobal Andres Pluas Palma",
        "photo": "/static/photos/student3.jpg",
        "school": "WILBUR CROSS",
        "description": "To be added..."
    },
     {
        "name": "Jeremiah Amir Ragsdale",
        "photo": "/static/photos/student3.jpg",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
       {
        "name": "Mirwais Rahmani",
        "photo": "/static/photos/student3.jpg",
        "school": "CAREER",
        "description": "To be added..."
    },
    {
        "name": "Carl Roberts",
        "photo": "/static/photos/student3.jpg",
        "school": "Metropolitan Business Academy",
        "description": "To be added..."
    },
     {
        "name": "Arzo Sadiq",
        "photo": "/static/photos/student3.jpg",
        "school": "Metropolitan Business Academy",
        "description": "To be added..."
    },
      {
        "name": "Xavier Sampedro Rosa",
        "photo": "/static/photos/student3.jpg",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
     {
        "name": "Juan Rafael Scruggs",
        "photo": "/static/photos/student3.jpg",
        "school": "High School in the Community",
        "description": "To be added..."
    },
     {
        "name": "Rohid Shamshad",
        "photo": "/static/photos/student3.jpg",
        "school": "WILBUR CROSS",
        "description": "To be added..."
    },
       {
        "name": "Maurice Lamont Smith",
        "photo": "/static/photos/student3.jpg",
        "school": "SOUND",
        "description": "To be added..."
    },
     {
        "name": "Alaena Lee Soto",
        "photo": "/static/photos/student3.jpg",
        "school": "CO-OP",
        "description": "To be added..."
    },
      {
        "name": "Eric Maurice Speer",
        "photo": "/static/photos/student3.jpg",
        "school": "CAREER",
        "description": "To be added..."
    },
      {
        "name": "Jostin Enrique Suarez Quichimbo",
        "photo": "/static/photos/student3.jpg",
        "school": "WILBUR CROSS",
        "description": "To be added..."
    },
      {
        "name": "Nydeliz Dariels Torres",
        "photo": "https://cdn.discordapp.com/attachments/1460818048654246043/1514746031798091796/0461D9FE-64A7-4B35-B141-9AAFCEB52C1C.png?ex=6a2c7cac&is=6a2b2b2c&hm=df499cc9b0c2d30a585aa35e88cbb0e59d47b0a5cba56e3ab7d5308b4e31344b&",
        "school": "Eli Whitney",
        "description": "you cant be stuck on the past when your future is bright."
    },
      {
        "name": "Caeli Love Tran Hamilton",
        "photo": "/static/photos/student3.jpg",
        "school": "CO-OP",
        "description": "To be added..."
    },
      {
        "name": "Aiden Alexander Velazquez",
        "photo": "/static/photos/student3.jpg",
        "school": "High School in the Community",
        "description": "To be added..."
    },
     {
        "name": "Gianna Washington",
        "photo": "/static/photos/student3.jpg",
        "school": "CAREER",
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
