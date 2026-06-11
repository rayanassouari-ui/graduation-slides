# Presentation of Graduates - Web App (Render-ready)

Art-deco gold/teal graduation slideshow as a Flask website. Title slide
+ one slide per student (photo, name, gold underline, school,
description). Smooth fade transitions on click / spacebar / arrow keys.
Fully responsive (works on phones too).

## Project structure
```
grad_web/
├── app.py              # Flask app + STUDENTS data
├── requirements.txt    # Python dependencies
├── render.yaml         # Render deployment config
├── templates/
│   └── index.html      # Page template (HTML/CSS/JS)
└── static/
    └── photos/         # Put local student photos here
```

## Edit your students

Open `app.py` and edit the `STUDENTS` list:

```python
STUDENTS = [
    {
        "name": "Rohid Shamshad",
        "photo": "/static/photos/student1.jpg",   # local file...
        "school": "Wilbur Cross",
        "description": "Loves basketball, video games, and making everyone laugh in class."
    },
    {
        "name": "Ava Martinez",
        "photo": "https://example.com/path/to/photo.jpg",  # ...or a direct image URL
        "school": "Lincoln High School",
        "description": "Loves art, soccer, and never misses a sunset photo."
    },
]
```

For local photos, drop the image files into `static/photos/` and
reference them as `/static/photos/yourfile.jpg`.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Deploy to Render

1. Push this folder to a GitHub repo.
2. Go to https://dashboard.render.com → **New** → **Web Service**.
3. Connect your repo. Render will detect `render.yaml` automatically
   (or set these manually):
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment:** Python 3
4. Click **Create Web Service**. Render gives you a live URL
   (e.g. `https://your-app.onrender.com`).

That's it — every time you push to the repo, Render redeploys.

## Controls
- Click anywhere → next slide
- Right Arrow / Space → next slide
- Left Arrow → previous slide
