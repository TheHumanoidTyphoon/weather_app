# WeatherCast
WeatherCast is a user-friendly web platform that utilizes the Flask framework and OpenWeather API to provide accurate and real-time weather information tailored to a specified location, making it a reliable and efficient tool.

## Installation
- Clone the repository:
```python
git clone https://github.com/your_username/WeatherCast.git
```

- Create a virtual environment and activate it:
```python
python -m venv venv
source venv/bin/activate
```
- Install the required packages:
```python
pip install -r requirements.txt
```
- Set the Flask app:
```python
export FLASK_APP=app.py
```
- Run the application:
```python
flask run
```
- Access the application by navigating to http://localhost:5000/ in a web browser.
## Usage
Once you access the application, you will be presented with a search box where you can enter the location for which you would like to get the weather information.

If the location entered is valid, the application will display the current weather conditions for the location. If the location entered is not valid, the application will display an error message.

## Contributing
Contributions are welcome. If you would like to contribute to this project, please follow these steps:

- Fork the repository
- Create a new branch
```python
git checkout -b my-new-branch
```
- Make changes and commit them
```python
git commit -am 'Add some feature'
```
- Push to the branch
```python
git push origin my-new-branch
```
- Create a pull request

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/TheHumanoidTyphoon/weathercast/blob/master/LICENSE) file for details.
