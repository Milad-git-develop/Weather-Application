
# 🌤️ Weather Application

A simple and practical Python application for getting weather information of cities worldwide.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## ✨ Features

- 📍 Get weather information for any city worldwide
- 🌡️ Display current temperature in Celsius
- 💧 Show humidity percentage
- 💨 Display wind speed
- ☁️ Show weather conditions (sunny, cloudy, rainy, etc.)
- 🔄 Interactive user interface
- 🚀 Fast performance with no delays

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Internet access

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/Milad-git-develop/weather-app.git
cd weather-app
```

2. **Install required libraries**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python weather.py
```

## 📖 Usage

After running the program, enter the name of your desired city:

```bash
Enter city name: Tehran

========================================
Weather in Tehran, IR
========================================
🌡️  Temperature: 25°C
💧 Humidity: 45%
💨 Wind Speed: 3.5 m/s
☁️  Conditions: Clear Sky
========================================
```

## 🏗️ Project Structure

```
weather-app/
├── weather.py          # Main application code
├── requirements.txt    # Required libraries list
├── README.md          # This file
├── .gitignore         # Ignored files
└── LICENSE            # Usage license
```

## 🛠️ Technologies Used

- **Python 3** - Main programming language
- **Requests** - For API communication
- **OpenWeatherMap API** - Weather data source
- **Git** - Version control
- **GitHub** - Code hosting

## 🔧 Code Example

```python
import requests

def get_weather(city):
    api_key = "your_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    return {
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description']
    }
```

## 📊 API Used

This application uses **OpenWeatherMap API**, a free service for weather data.

- 🔑 [Get Free API Key](https://openweathermap.org/api)
- 📚 [API Documentation](https://openweathermap.org/current)

## 🤝 Contributing

Contributions, ideas, and bug reports are always welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## 👨‍💻 Developer

**Milad Ganjali** - AI developer and Python programmer

- 📧 Email: milad.ganjali.01@gmail.com
- 🐙 GitHub: [Milad-git-develop](https://github.com/Milad-git-develop)

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenWeatherMap for providing free API
- Python open-source community
- Everyone who tests and improves this project

## ⭐ Support

If you find this project useful, please give it a star! ⭐
