import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        info = get_user_info(username)
        return render_template('results.html', info=info, username=username)
    return render_template('index.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    username = request.form.get('username')
    info = get_user_info(username)
    return jsonify(info)

def get_user_info(username):
    platforms = {
        "facebook": f"https://www.facebook.com/{username}",
        "instagram": f"https://www.instagram.com/{username}",
        "twitter": f"https://twitter.com/{username}",
    }

    user_info = {}

    for platform, url in platforms.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        if platform == "facebook":
            # Placeholder for Facebook
            profile_picture = soup.find("img", attrs={"alt": f"{username} profile picture"})
            personal_info = None  # Facebook has strict privacy settings

        elif platform == "instagram":
            # Placeholder for Instagram
            profile_picture = soup.find("img", class_="be6sR")
            personal_info = soup.find("div", class_="-vDIg")

        elif platform == "twitter":
            # Placeholder for Twitter
            profile_picture = soup.find("img", attrs={"alt": f"{username}"})
            personal_info = soup.find("p", class_="ProfileHeaderCard-bio u-dir")

        user_info[platform] = {
            "username": username,
            "profile_picture": profile_picture["src"] if profile_picture else None,
            "personal_info": personal_info.text if personal_info else None
        }

    return user_info
# UI using tkinter
if __name__ == "__main__":
    app.run(debug=True)
