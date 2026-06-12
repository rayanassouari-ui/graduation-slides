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
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/714023130_1563359182066744_1274354215665151834_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=zqMO2z8k3HcQ7kNvwH-WLUQ&_nc_oc=Adr0eONZzfmb4se9xnJRgc10nlM-ZC6Fh6i5nCP9jNzUg6NrAnqwBzyrxVYbAQmAJeo2QybwE3S7vzmzqV1ahaGp&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gH8_F330itfvSq4-TCPISRnNC0PNPVy0wafA9wj_qbmcA&oe=6A52A225",
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
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/721756758_1318026190506020_3639808467011350954_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=101&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=y7YPHzoyLJsQ7kNvwF6D0JY&_nc_oc=AdrZ3VODqlU-NlspRKr6xih-wbCnl_latlhKX5Dlw0nNB7ciseatIQlN7cD9mM2qZ0k2l3SnK0T_3Hl1sJm55t2x&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7b6a8&oh=03_Q7cD5gH43JwisgCN29NdjPl5YljJIEj_LqURANaeN7GksboaZQ&oe=6A312B25&ig_cache_key=MTMxODAyNjE4NzE3MjY4Nw%3D%3D.2-ccb7-5.f",
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
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/719026669_27125397250443770_4037617840432896933_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=fZRF73io9lkQ7kNvwEh1eiY&_nc_oc=AdpCwLe340rFvO53m0A8xgS111tZxQ79_q94ngTG7ieCxaUEVJ3b2lO7awXG_02yzIqsnF32n9Bu5yRKK1BwrHdX&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gEIdgOZUKf6fOJHEO9pK6Qf_f8Gky8s8xXuMW6HIEW7kw&oe=6A52C9B7",
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
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/722446876_1588670972683669_2424562583428653438_n.png?_nc_cat=100&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=7jVWMQ_JXgkQ7kNvwFXXeYH&_nc_oc=Adq3s6RgQpbLa10fakFk9DwnjX6uB5DBK7J3GboOTA4Kv9hjhiYKibKwN1X1apMIoTGDj8NJymjPUWZLGMQTVLQH&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFXHtVLYw2HObmB8DAbE-Y4GHlgMl8no8H7NJTKX4SqVw&oe=6A52E402",
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
