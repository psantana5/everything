import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTextBrowser, QComboBox
from PyQt5.QtGui import QCursor, QIcon, QFont
from PyQt5.QtCore import Qt, QTimer


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setWindowIcon(QIcon('weather_icon.png'))
        self.setGeometry(100, 100, 800, 600)

        self.api_key = '37a12bcde55e7a883f5e7c69b69d334b'

        self.city_label = QLabel('Enter City:')
        self.city_input = QLineEdit()
        self.get_weather_button = QPushButton('Get Weather')
        self.weather_label = QLabel('Weather:')
        self.forecast_label = QLabel('Forecast:')
        self.alerts_label = QLabel('Weather Alerts:')
        self.alerts_text = QTextBrowser()

        self.city_input.setPlaceholderText('Enter city name...')
        self.city_input.returnPressed.connect(self.get_weather)

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.weather_label)
        layout.addWidget(self.forecast_label)
        layout.addWidget(self.alerts_label)
        layout.addWidget(self.alerts_text)

        self.setLayout(layout)

        self.setStyleSheet('''
              QWidget {
                background-color: #212121;
            }
            QLabel {
                color: #ffffff;
                font-size: 18px;
                font-weight: bold;
            }
            QLineEdit {
                font-size: 14px;
                padding: 10px;
                border: 2px solid #424242;
                border-radius: 5px;
                color: #ffffff;
            }
            QTextBrowser {
                font-size: 14px;
                background-color: #383838;
                border: 2px solid #424242;
                border-radius: 5px;
                color: #ffffff;
            }
            QPushButton {
                font-size: 16px;
                background-color: #546e7a;
                color: #ffffff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #455a64;
            }
            ''')

        self.get_weather_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.get_weather_button.clicked.connect(self.get_weather)

        self.font_increase_button = QPushButton('+')
        self.font_decrease_button = QPushButton('-')
        self.font_increase_button.clicked.connect(self.increase_font_size)
        self.font_decrease_button.clicked.connect(self.decrease_font_size)

        self.dark_mode_button = QPushButton('Dark Mode')
        self.dark_mode_button.clicked.connect(self.toggle_dark_mode)

        font_layout = QVBoxLayout()
        font_layout.addWidget(self.font_increase_button)
        font_layout.addWidget(self.font_decrease_button)
        layout.addWidget(self.dark_mode_button)
        layout.addLayout(font_layout)

        self.city_history = []
        self.load_city_history()
        self.city_combobox = QComboBox()
        self.city_combobox.addItems(self.city_history)
        layout.addWidget(self.city_combobox)

        self.get_geolocation_button = QPushButton('Get Weather by Geolocation')
        self.get_geolocation_button.clicked.connect(
            self.get_geolocation_weather)
        layout.addWidget(self.get_geolocation_button)

        self.current_font_size = 14
        self.set_font_size()
        self.dark_mode = False

        self.auto_refresh_timer = QTimer()
        self.auto_refresh_timer.timeout.connect(self.get_weather)
        # Refresh every 10 minutes (adjust as needed)
        self.auto_refresh_timer.start(600000)

    def set_font_size(self):
        font = QFont()
        font.setPointSize(self.current_font_size)
        self.city_label.setFont(font)
        self.city_input.setFont(font)
        self.get_weather_button.setFont(font)
        self.weather_label.setFont(font)
        self.forecast_label.setFont(font)
        self.alerts_label.setFont(font)
        self.alerts_text.setFont(font)
        self.font_increase_button.setFont(font)
        self.font_decrease_button.setFont(font)
        self.dark_mode_button.setFont(font)
        self.city_combobox.setFont(font)
        self.get_geolocation_button.setFont(font)

    def increase_font_size(self):
        self.current_font_size += 1
        self.set_font_size()

    def decrease_font_size(self):
        if self.current_font_size > 8:
            self.current_font_size -= 1
            self.set_font_size()

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.setStyleSheet('''
                QWidget {
                    background-color: #212121;
                }
                QLabel {
                    color: #ffffff;
                    font-size: 18px;
                    font-weight: bold;
                }
                QLineEdit {
                    font-size: 14px;
                    padding: 10px;
                    border: 2px solid #424242;
                    border-radius: 5px;
                    color: #ffffff;
                }
                QTextBrowser {
                    font-size: 14px;
                    background-color: #383838;
                    border: 2px solid #424242;
                    border-radius: 5px;
                    color: #ffffff;
                }
                QPushButton {
                    font-size: 16px;
                    background-color: #546e7a;
                    color: #ffffff;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #455a64;
                }
                QComboBox {
                    font-size: 14px;
                    padding: 5px;
                    border: 2px solid #424242;
                    border-radius: 5px;
                    color: #ffffff;
                }
                ''')
        else:
            self.setStyleSheet('''
                QWidget {
                    background-color: #f5f5f5;
                }
                QLabel {
                    color: #333333;
                    font-size: 18px;
                    font-weight: bold;
                }
                QLineEdit {
                    font-size: 14px;
                    padding: 10px;
                    border: 2px solid #dddddd;
                    border-radius: 5px;
                    color: #333333;
                }
                QTextBrowser {
                    font-size: 14px;
                    background-color: #ffffff;
                    border: 2px solid #dddddd;
                    border-radius: 5px;
                    color: #333333;
                }
                QPushButton {
                    font-size: 16px;
                    background-color: #3498db;
                    color: #ffffff;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
                QComboBox {
                    font-size: 14px;
                    padding: 5px;
                    border: 2px solid #dddddd;
                    border-radius: 5px;
                    color: #333333;
                }
                ''')

    def get_weather(self):
        city_name = self.city_input.text()
        if city_name:
            current_url = f'http://api.weatherstack.com/current?access_key={self.api_key}&query={city_name}'
            forecast_url = f'http://api.weatherstack.com/forecast?access_key={self.api_key}&query={city_name}'
            alerts_url = f'http://api.weatherstack.com/alerts?access_key={self.api_key}&query={city_name}'

            current_response = requests.get(current_url)
            forecast_response = requests.get(forecast_url)
            alerts_response = requests.get(alerts_url)

            current_data = current_response.json()
            forecast_data = forecast_response.json()
            alerts_data = alerts_response.json()

            if 'current' in current_data:
                current_weather_description = current_data['current']['weather_descriptions'][0]
                current_temperature = current_data['current']['temperature']

                self.weather_label.setText(
                    f'Current Weather: {current_weather_description}, Temperature: {current_temperature}°C')

                map_html = f"""
                <iframe width="100%" height="300" frameborder="0" scrolling="no"
                marginheight="0" marginwidth="0"
                src="https://maps.google.com/maps?q={location['lat']},{location['lon']}&hl=es;z=14&amp;output=embed">
                </iframe>
                
            """
                self.map_browser.setHtml(map_html)
            else:
                self.weather_label.setText('Error fetching weather data.')

            if 'forecast' in forecast_data and 'daily' in forecast_data['forecast']:
                forecast_items = forecast_data['forecast']['daily']
                forecast_text = '\n'.join(
                    [f"{item['date']} - {item['weather_descriptions'][0]}, Max Temp: {item['temperature_max']}°C, Min Temp: {item['temperature_min']}°C"
                     for item in forecast_items])

                self.forecast_label.setText(f'Forecast:\n{forecast_text}')
            else:
                self.forecast_label.setText('Error fetching forecast data.')

            if 'alerts' in alerts_data:
                alerts = [
                    f"🚨 {alert['event']} - {alert['sender_name']}\n   {alert['description']}\n" for alert in alerts_data['alerts']]
                alerts_text = '\n'.join(alerts)
                self.alerts_text.setPlainText(alerts_text)
            else:
                self.alerts_text.setPlainText('No alerts for this location.')
        else:
            self.weather_label.setText('Please enter a city name.')

    def get_geolocation_weather(self):
        pass  # Implement geolocation weather fetching logic here

    def save_city_history(self):
        with open('city_history.txt', 'w') as f:
            f.write('\n'.join(self.city_history))

    def load_city_history(self):
        try:
            with open('city_history.txt', 'r') as f:
                self.city_history = f.read().splitlines()
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
