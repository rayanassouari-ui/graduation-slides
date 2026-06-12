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
        "name": "Bibi Zahra Adnan",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/719873420_1751813175814242_721287650445145070_n.png?_nc_cat=105&ccb=1-7&_nc_sid=9f807c&_nc_ohc=12eto75BHuwQ7kNvwFzAnmI&_nc_oc=Adojdp4VWJRCKkLAZvD6uSb3XONIJgaa25ygYHvqlwojMqf7hToyrPGHefYLwWtvPF4_oJB2xHZPf2fOufOGka8L&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHgpaUAI5_fl6f_Zna2HtE7CO5EmXmIEkYqt56vB8F8Gg&oe=6A53D034",
        "school": "HillHOUSE",
        "description": ""
    },
    {
        "name": "Joel Emiliano Almeida Figueiras",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/721777850_1029188303005463_906538504239668150_n.png?_nc_cat=105&ccb=1-7&_nc_sid=9f807c&_nc_ohc=r83AShUIKawQ7kNvwF7kGOI&_nc_oc=AdrLg4WBSkD-1UDx9hILLfc4hvalKnp4KjRca4Fupw7YuUfJZoC4ukBmtEVy-iI49pn4KyVoplZiu2AjAZk4dgxZ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHnCkZ62rnDwkx6PVmCNZCCKUXYEokayDiHJ5uxWTaWow&oe=6A53F099",
        "school": "Wilbur Cross",
        "description": "To be added.."
    },
    {
        "name": "Monserrat Arenas Martinez",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/717437077_2781554768875024_8612860244642542718_n.png?_nc_cat=105&ccb=1-7&_nc_sid=9f807c&_nc_ohc=olC0gQFhw3UQ7kNvwE34Soz&_nc_oc=AdojQJCvn4dVEcsU5nFlCxEod7t0X8blHQvOhVX64vm4hqm4nsP29POXeisNcwlViUz2qmIEsEANYfW5JOgHYl8n&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHqmnwQPGFiH_bTKdW8YonsXqjHe_cix5_0WCusuXEACA&oe=6A53CD63",
        "school": "Wilbur Cross",
        "description": "To be added..."
    },
    {
        "name": "Iliana Arocho",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/723130008_27490694547222673_1950729644942787669_n.png?_nc_cat=102&ccb=1-7&_nc_sid=9f807c&_nc_ohc=z2XGJJqm4EcQ7kNvwGvmVtU&_nc_oc=Adql_otsLppi5eJ_ixGXexXg3kRJtbkH0wvLQvfk-kqpxP2V1huPf0QmjHf3SAhY1-jGck4x4UPIoXIPPpw7Htgn&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHfEcfocyP4J09-45w4KUwLM3ssyfKPzN4wp5aYvf03kQ&oe=6A53F0FC",
        "school": "High School in the Community",
        "description": "To be added..."
    },
     {
        "name": "Ahmad Amirzai",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/717115052_1887602905530550_6883893978500826708_n.png?_nc_cat=104&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=eTaKXsGIyNAQ7kNvwEKimov&_nc_oc=AdpORqkQpSaVDbcbrmpq25VwZHrRJ9yl7_3y_ftl1s9GZ117WbqM91L4BZXqtwmN5BbP0WO2qrEBBxOfsTN1ztnV&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFKS0QrqWKYLQaCAXuaZPxTzd7hu3wdTHcDKjatAZxKiQ&oe=6A53BD11",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
    {
        "name": "Rayan Assouari",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/718174094_1485303206115509_8209481933846804205_n.png?_nc_cat=105&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=5l2M_QpIO_AQ7kNvwHTtnaW&_nc_oc=AdoSlKchkYb7huLjwJU1EQNrPpIlRRZgI0gYVsAJVH0A5IHEE0zlqmcDy951QISaYWbK-Oujx5U4714H_oSpeiB1&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHpuX87RL0lcgXZZmiMUWFVsHMv0kfLi7knAAxgMrZI4Q&oe=6A53D627",
        "school": "High School in the Community",
        "description": "To be added..."
    },
      {
        "name": "Yeimy Carisa Barreda",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/718611306_1219489486853853_3296595231098137329_n.png?_nc_cat=101&ccb=1-7&_nc_sid=9f807c&_nc_ohc=Ad2xQ22sdWIQ7kNvwE_tTg5&_nc_oc=AdpQTyHxfRO_GOZi84iQzOfCBwv7X3Rhr09bRLewryQDex1Rm5THCgiCV0NLRO7cVz3x5WZqWasm_XE9zQ55_1jp&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gGPZgMPOptfm9c-06Bt7Uy15MlTS0PGkVQ9hjkf-4qIbw&oe=6A53E3D2",
        "school": "Wilbur Cross",
        "description": "To be added..."
    },
       {
        "name": "Aisake Levon Brandon",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/715352880_1522818662873822_3998643176800705601_n.png?_nc_cat=110&ccb=1-7&_nc_sid=9f807c&_nc_ohc=GuMRcBYqN5QQ7kNvwGoptQe&_nc_oc=AdrpgwQUnEmOHa8W2Phl4TP-YZ9a8Ixl-AS0Z--mRMTLxlhc9NtZO0qOQmwN0dkN7uMWto1Jg5EI7DpL6OZZVfAl&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gEqLumrI9LToHpnizuEVhdhzgcjsyGXKYZf-FLDzg_rig&oe=6A53E444",
        "school": "Career",
        "description": "To be added..."
    },
     {
        "name": "Nicholai Josiah Oponde Brown",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/716449948_904421129333899_2213070239753761798_n.png?_nc_cat=101&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=oWpzUthyMscQ7kNvwGRz1Ie&_nc_oc=Adr0TqcR7xYyPxCOd1LBwSaoUZ1z8WY07lIFLe9E7LJt4oJ043genTyZJj59lvbBamKCxVS8n012d-rScaZJ9e4j&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFkeTLMIz-u9qPbJ53wgEPect3Jz6HeKI9JPYAuqp5BDg&oe=6A53C149",
        "school": "COMMON GROUND",
        "description": "To be added..."
    },
     {
        "name": "Leeyanna Caple",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/718867858_37388105664122070_2911884564444285426_n.png?_nc_cat=102&ccb=1-7&_nc_sid=9f807c&_nc_ohc=bLUgKI1D5kwQ7kNvwFvyy_l&_nc_oc=AdqruEFQP9jeV_Kc7KJtm7hak5uqfiqUWvNdxA8X7KHWj4775Up166ZLJsxdQaufffkfb15f-Wgqk3XAqfzfnama&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gGSh4olOLOJb3tC-z0OPF5jH32zXbetf829MDqRRpVe7w&oe=6A53CFAC",
        "school": "Eli Whitney",
        "description": "To be added..."
    },
      {
        "name": "Angel Jose Cruz",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/718618041_1689091345473765_6942466726756645308_n.png?_nc_cat=109&ccb=1-7&_nc_sid=9f807c&_nc_ohc=PGdsSYjmZO0Q7kNvwGLhWmx&_nc_oc=AdpqPB7OO3Za5LS_3hEWJPhgVMKTg0YSm_E9lTkDrZEj-MtTYiFjhRrrdR2FVZtPaD_AFn9tVT3GBRNfC0N1bP1A&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gGA0z2yxMWAl8FpWEZ7n3iLacgZd7FIeSarQW7-LRjp_g&oe=6A53E5ED",
        "school": "HillHOUSE",
        "description": "To be added..."
    },
    {
        "name": "Nagedlie Sofia David",
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
        "name": "Zackary Cody Franklin",
        "photo": "/static/photos/student3.jpg",
        "school": "HillHOUSE",
        "description": ""
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
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/721168429_1693502801565994_1847310654048389047_n.png?_nc_cat=110&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=qiacrXCnmnIQ7kNvwFQPPx_&_nc_oc=Adqee5mkpUrn-tDib6iE9_Qk6leEoRZ5HCjILywVDK0gT7eAGFmfjLXUzjc-cgnwBDefSBnFRXjGEdTaKlGnuphC&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gEARDG3S6jpInTP8Bh9b165mj85qGsVeBlPSEhCCBTtLA&oe=6A53D49A",
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
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/718979974_1684756596108544_3721482075968536841_n.png?_nc_cat=106&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=UB_GZLZBb5MQ7kNvwHT6iOP&_nc_oc=Ado8I0MtyV4jtjG5Nme5wxLOls5WIBkKbXMOevChk9zpBuOZVUjnuei-empvdYiP2Pq_seDTBMvw4mgdRQxZ646w&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gEM0RagCYdHgPkbIhpY4piS6gZUOSUimCxRW4nkdY9T6Q&oe=6A53CED2",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
     {
        "name": "Merlyn Anhelis Ninasunta Vegas",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/719351003_1596335762214887_874009053040774146_n.png?_nc_cat=109&ccb=1-7&_nc_sid=9f807c&_nc_ohc=jMCkZ_f-Nl0Q7kNvwGv5aFM&_nc_oc=Adq1Jgb38xQ1i8dpMty6aM-DhwydP2hLIux6Io4Vbs_gyiuX2LCbN_p1nXjFj4yOnq6y07GR9CKcEakBkJseATaw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFSFW8tVVlClQfoCAUZjhpb0Wpqu1D74-InAYBQBWBE8A&oe=6A53E893",
        "school": "WILBUR CROSS",
        "description": "To be added..."
    },
     {
        "name": "Roiy Nizami",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/720038871_1498430761181471_1001061767251977530_n.png?_nc_cat=110&ccb=1-7&_nc_sid=9f807c&_nc_ohc=dxvuVzR0QVsQ7kNvwEv1LyE&_nc_oc=AdrLUOZDIjbycajS9YWerdY4QGRdB91eh22vAwWqfVWh12lVHJ93bx-Fo-uLCFxYGgE9tv1tyAyrfxWMyxoksgBS&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHXkHSRILYUDLtndvGWHV4ZaQWa2r6H_6DgSnjRZ8Fo_A&oe=6A53E0BF",
        "school": "CAREER",
        "description": "To be added..."
    },
    {
        "name": "Luis Ismael Padilla",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/718188672_4330442600538504_6145211294751209998_n.png?_nc_cat=104&ccb=1-7&_nc_sid=9f807c&_nc_ohc=DazHZuhB-60Q7kNvwEYrtvO&_nc_oc=Adpeuzhm62bBd8VcQNGwSfkDMwyyEq8dwNq7z59RGDwXHco9gvmCjc_izGncgOmflG_cUdkhK8tyg48DuVle6EaV&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gGpTLXefE1flbgNryp_gt6V2rmLCTXsDNL-9wdjRckY9Q&oe=6A53D8E4",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
      {
        "name": "Sima Paktin",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/717264376_1469970991826914_289310158123843875_n.png?_nc_cat=110&ccb=1-7&_nc_sid=9f807c&_nc_ohc=3l789cK3s3gQ7kNvwEhVnPN&_nc_oc=AdqNZj2Qmuucj-Smj5KUIpeISIQVZUMbCudk5kpfiZmm7ijKKKFKhEKObheeP38-rmb-6wbGXOtxXPJZacilsSx7&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFhZT_egSx_hm1J4vo5bVfumAftPfmHZMuUTf9aWGq10w&oe=6A53D7C0",
        "school": "CAREER",
        "description": "To be added..."
    },
       {
        "name": "Mannix Eli Pena",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/717958560_1034716142834073_763122134756753726_n.png?_nc_cat=110&ccb=1-7&_nc_sid=9f807c&_nc_ohc=tHdOm7YZfCwQ7kNvwFLHWZX&_nc_oc=AdqZaV48DziwIxqChQvhXdGBKMNO96CL3KQtNxxjX08bsnSa7s9xDiSIBW0B7KnfZmx6pH132HALJVIr1uGTXvrH&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gH5nRL3kJNY8eMwdihBFL3TrFTMB4gZsBXLLRcJUJbknQ&oe=6A53C4AB",
        "school": "CAREER",
        "description": "To be added..."
    },
       {
        "name": "Masen Elijah Pena",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/719948624_938199269225323_8889349459118048770_n.png?_nc_cat=109&ccb=1-7&_nc_sid=9f807c&_nc_ohc=mIHXGzIO_9kQ7kNvwFPubmS&_nc_oc=Adoqv3QXOc4SKYNkBHvvHjo33dhzv_8eEweE7uWwQ8LT9EuhACiAVpef5F22nTeTA0XzyxJVJKQSf3GhgA-gGKlM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHK74ruBniRlWszGMGhrE4FtrlzKXKKv5j7Gb0BvMWIwQ&oe=6A53D680",
        "school": "CAREER",
        "description": "To be added..."
    },
      {
        "name": "Cristobal Andres Pluas Palma",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/718776631_980832648074902_6515945823802202733_n.png?_nc_cat=107&ccb=1-7&_nc_sid=9f807c&_nc_ohc=jc1s_ou1LHQQ7kNvwGg0RZy&_nc_oc=Adp0vwmVY_5N0KGktfu-X8ucIOcamnCQq3idRCjKxoRvDIse9WkTAnvrsijByH6K7x1UMGY4Uypkdec-IgaoIfVy&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHTgWU10VQ9H_kZDNVHiIZ63yn9rCfDwxUNdWXaoedH-g&oe=6A53CCBB",
        "school": "WILBUR CROSS",
        "description": "To be added..."
    },
      {
        "name": "Jeremiah Amir Ragsdale",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/721859909_2112063449356095_1724427522335985681_n.png?_nc_cat=109&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=lQlKrZsd-10Q7kNvwGZX8pi&_nc_oc=AdrmBLePbaB2e6a6ddP01lSjA-suq2b2O8I9FkIT-jZAhBT-Yw1eyiw7DyKihZKo6TDFoPJAl_-8--RALnqjbYJQ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gGb6Gc6w6At-JkQUI7k9lhpuv6V3_XklBXDmyI2cfiiGQ&oe=6A53E531",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
     {
        "name": "Angie Porter",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/721733559_1548682056958635_5597990434896591474_n.png?_nc_cat=109&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=SeqCtNPm3UUQ7kNvwGP63ND&_nc_oc=AdqMq1Jj-6xH3GqKMpS7L2I8p6-nWwGDyghg5cNA_aTIX3mEulaZbxAeFcr-YOMtP6ClYsEPwlcHCKgYlnrA1VQZ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gEpM3E7MnsiNCLy-aDOgm2JeR84Fks1ko2kOISqFGLxwQ&oe=6A53C580",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
       {
        "name": "Mirwais Rahmani",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/716985913_2026629624599929_424378790157544204_n.png?_nc_cat=109&ccb=1-7&_nc_sid=9f807c&_nc_ohc=rUtRU2BisS0Q7kNvwH2FoM0&_nc_oc=AdqmT8w_-NMhybG5LgyFatEO-MeGSRnFbyfGAJlF09EhrhgoX9FL5b1o0IudxFX2CSeuf4YWUBuw05tvmhz02rD2&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFVZRXGb0fIKoqIm2CAQZWssgCWDQqxyAs5uJfy325zFw&oe=6A53E114",
        "school": "CAREER",
        "description": "To be added..."
    },
     {
        "name": "Mai'Jor Jayvon Rangolam",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/719031717_2521504941613820_4676102658479316969_n.png?_nc_cat=109&ccb=1-7&_nc_sid=9f807c&_nc_ohc=CWVDowt3ebIQ7kNvwHhRrdF&_nc_oc=AdpZDmSO-4l_WSa1i8Nh-NbsGC8RSJpjJw32kt9G0iZQ57eOefokXppN08lQjLaxnhg7lZUCHOCB9kRG0HvMOokC&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gEdv7rbIVsDUIAkXUGBZEBrqz2Q5Hj0v3osEdbKVboqTQ&oe=6A53E64B",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
    {
        "name": "Carl Roberts",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/723674838_1810220336618385_8822610571238781138_n.png?_nc_cat=103&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=KCjHKKfyyCgQ7kNvwE-uWO6&_nc_oc=Adqq9H3PqvwGh7A9hLvKN3mGk5OrCJOBjnjCXwiLczhCXn-r75ykFxwqUYcIfP7KKvTW77pQIddNCU7mtOnHMxH9&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gGi_9PauOpAnn7iaDxYNFxNameapMEM_-JC8lnMp1t6HQ&oe=6A53D75B",
        "school": "Metropolitan Business Academy",
        "description": "To be added..."
    },
     {
        "name": "Arzo Sadiq",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/718131143_937409642661670_1620381177160620473_n.png?_nc_cat=104&ccb=1-7&_nc_sid=9f807c&_nc_ohc=87gMbT-4Vq8Q7kNvwHIkiKE&_nc_oc=AdoEbTdnWkCtjMmHCW44Glbr-3k5l5DGEeJwORb5tcyaJW1xHyYVRkw7evw1eSKBfVAd6HoVG4eDLqEEyVRIOzZR&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gEqbhaIoFtAyht_Zyl9M4v3YtAcTg49sHrIAEVB3xZzDg&oe=6A53F366",
        "school": "Metropolitan Business Academy",
        "description": "To be added..."
    },
      {
        "name": "Xavier Sampedro Rosa",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/723607544_2436962116771653_5048999379128685691_n.png?_nc_cat=111&ccb=1-7&_nc_sid=9f807c&_nc_ohc=ZRRrdG5_4mYQ7kNvwFBvteQ&_nc_oc=AdoM4Sh5vHMwOBQK-tq2pOQjv8yXJwvth8tDaZwOK_ZbvutqcY_atdyhCUFqt3FIqA2HeNw31psDNXF-bcWN0NId&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gGo6qCUHLOx1FSyYeOiIAhCH3rhx3P6i9ulybZLCwiazw&oe=6A53DF71",
        "school": "HILLHOUSE",
        "description": "To be added..."
    },
    {
        "name": "Steven Santos",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/715440753_1703987814192303_5691246700707333359_n.png?_nc_cat=101&ccb=1-7&_nc_sid=9f807c&_nc_ohc=mB9W0JuPPWAQ7kNvwEOveKa&_nc_oc=Ado3wNkvwJKNaBrqMK_sOd2n8b4XuvqB_e7NOO48xjEKFTH_zCl6SGexjUdbCQqAjNsA70VPswcxE_4od2O6Xtxn&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFpfrvYkUdaX5jXy-0819CZtDIR3XkmOpN0MkAnlq1YBA&oe=6A53CE15",
        "school": "HILLHOUSE",
        "description": ""
    },
     {
        "name": "Juan Rafael Scruggs",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/716950297_1324220715782184_801973422774066293_n.png?_nc_cat=108&ccb=1-7&_nc_sid=9f807c&_nc_ohc=60ndn6_fkToQ7kNvwEJU7um&_nc_oc=AdqSG2_8AfEM8DLIvGm8Idb4jSUTI7YCjAfHVOMklLt6qWuL36wcR6E6qSGdr3Q4cUSYGItHnqiVRcy-vUiSrTOJ&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gEAza9B3pSoNhuAIKDb2-KEDGJjQigYOapzJ_E13ZP3xQ&oe=6A53E091",
        "school": "High School in the Community",
        "description": "To be added..."
    },
     {
        "name": "Rohid Shamshad",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/716509919_1020654403808975_752389801508680566_n.png?_nc_cat=100&ccb=1-7&_nc_sid=9f807c&_nc_ohc=sYKcYpfAv3QQ7kNvwED8wsu&_nc_oc=Adr2wJ2Eb2TuoOenS3KxZ_aHJLORtnToGuRFcbjJDpPSmZucYhTXOSgQLF8hCfurAkpXqKMg3eM1svf7fUE2mWHk&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFab3tZV3p9bZMraaVoTyDXxTpCnNBVv-nMj3lCY8Cg5A&oe=6A53C6BC",
        "school": "WILBUR CROSS",
        "description": "To be added..."
    },
       {
        "name": "Maurice Lamont Smith",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/720085534_1329882025138713_4254968528441248336_n.png?_nc_cat=103&ccb=1-7&_nc_sid=9f807c&_nc_ohc=ui35EZnzR8oQ7kNvwGP1qB-&_nc_oc=Adp9DCycDOvSZo6ZThgMH5A-Hx0f31U1fVgx5Zw2IOeyfZVDoCRdryzJ10nzkNACsn3pdrm_KUm-_R30KLuUdVO3&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gGbNdsKPWj5iKvHbGBMBBul0NHRY30JxYAVfqB8lzEjfA&oe=6A53ECDC",
        "school": "SOUND",
        "description": "To be added..."
    },
     {
        "name": "Alaena Lee Soto",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/715749873_1423534989535515_323132545262997004_n.png?_nc_cat=104&ccb=1-7&_nc_sid=9f807c&_nc_ohc=nPkNAJBXEjEQ7kNvwFnh9WH&_nc_oc=AdoHn0_CqY5_k6qmX6g4vxrZwhBFlJv_wEZnhw-TSmJs0yz6vyyNNY9Q0yQJv5hkfVlHmc9o_RWWzn3t4ZZ-ZtZo&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHhj0R5IRRdyeczIMND4AwFt0KgqxxnLAw7BoJF4Fa3aQ&oe=6A53E3FE",
        "school": "CO-OP",
        "description": "To be added..."
    },
      {
        "name": "Eric Maurice Speer",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/718276287_996968516258287_895336029880586020_n.png?_nc_cat=108&ccb=1-7&_nc_sid=fc17b8&_nc_ohc=IKsKX-6ncqgQ7kNvwH_JAvT&_nc_oc=AdoIL6rOaZvrHAGpl6xm-Gx0hh9KEBxq0Niy3GlKbyZwavHSKqD_Ict4tzohXXXe8nt9w2EthdkG8IhfeptdMyqL&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFyrYwlHE4Ap0joH6TZXj5zQAaYObtp8GaNIcfVowPcIg&oe=6A53DCDF",
        "school": "CAREER",
        "description": "To be added..."
    },
      {
        "name": "Jostin Enrique Suarez Quichimbo",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/717776590_2421717721572462_893519492611999392_n.png?_nc_cat=104&ccb=1-7&_nc_sid=9f807c&_nc_ohc=grlCTg_j7ScQ7kNvwFrdsIx&_nc_oc=AdrOSAjLsw5O6VqTWsNGS_noOPkOlcjgoMJNUtMgr0wFWRWk1cJnJfZ4csoNmCf6kUZtkzSk7AyRLBHe5xrFUa_t&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gGjgGKUqRohUtXApiEuvtBQNA4WsZRhhyb-890JRB13RQ&oe=6A53C822",
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
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/721134726_2243319573075178_972262053724537543_n.png?_nc_cat=107&ccb=1-7&_nc_sid=9f807c&_nc_ohc=sOC9soYqsvoQ7kNvwHY-VfC&_nc_oc=AdpzeWJFjVqRioSsaSInbmABliCS-A6rIfhYtL42nFcYdTWni9UxvIohcNsqI17tovl_um6Gphu2DagwgF-uMoKW&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gFDMpuC7Qc3Xdv_IE0AfFfxFthP6ozl76kZeFKh29nmEg&oe=6A53E809",
        "school": "CO-OP",
        "description": "To be added..."
    },
      {
        "name": "Aiden Alexander Velazquez",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/722073923_2085001015415375_4130210383437647087_n.png?_nc_cat=100&ccb=1-7&_nc_sid=9f807c&_nc_ohc=8KAD9h6OHiMQ7kNvwHK2LJd&_nc_oc=Adr9V9V1va-QO06pA5vGUu27j7-lrhTP5gGrStTHAE8YLq58oSRzx9rTEGp4hGvaJty8beG4pfSSxlqA7Pk7fOsO&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gHSgSbc_X8RFy-1ULGKoQalsLYyzQeoIVM-60ajhMZhHA&oe=6A53D1D0",
        "school": "High School in the Community",
        "description": "To be added..."
    },
     {
        "name": "Gianna Washington",
        "photo": "https://scontent-bos5-1.xx.fbcdn.net/v/t1.15752-9/720248293_1531674865264429_3051644155272085323_n.png?_nc_cat=101&ccb=1-7&_nc_sid=9f807c&_nc_ohc=FCpsbMcGbtcQ7kNvwEDTq3g&_nc_oc=AdouvJ7iFA_KldqXXgBw564Ur_CqcQ2yMXuBsAwqMox-iq9q23J-3IJj1OhQM0xujavIvNeaVacSCAcy542vRU5M&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-bos5-1.xx&_nc_ss=7a22e&oh=03_Q7cD5gEBkTDEEHtooXTztghAljgbIdMfbf8jq1yXqkye_D83vg&oe=6A53EBC7",
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
