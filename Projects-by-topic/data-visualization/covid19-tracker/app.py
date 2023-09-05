from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    world_data = {}
    country_data = {}
    world_vaccine_data = {}
    country_vaccine_data = {}
    countries = []

    if request.method == 'POST':
        country = request.form.get('country')
        url = f"https://corona.lmao.ninja/v2/countries/{country}"
        response = requests.get(url)
        if response.status_code == 200:
            country_data = response.json()

    url = "https://corona.lmao.ninja/v2/all"
    response = requests.get(url)
    if response.status_code == 200:
        world_data = response.json()

    url = "https://corona.lmao.ninja/v2/countries/"
    response = requests.get(url)
    if response.status_code == 200:
        countries = [country['country'] for country in response.json()]

    return render_template('index.html', world_data=world_data, country_data=country_data, countries=countries, world_vaccine_data=world_vaccine_data,  country_vaccine_data=country_vaccine_data)

@app.route('/historical/<country>', methods=['GET'])
def historical(country):
    url = f"https://corona.lmao.ninja/v2/historical/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
