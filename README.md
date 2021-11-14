<div>
    <img src="./weather.jpg" alt="Weather" width="500" />
    <h1 style="border: none;">Weather App</h1>
    <h2>Writed By Semicolon World</h2>
    <h3>Frontend: <a href="https://github.com/mohammadbaratii">Mohammad Barati</a></h3>
    <h3>Backend: <a href="https://github.com/metidotpy">Mehdi Radfar</a></h3>
</div>
<div>
    <ul>
        <li>
            <h1>How to Run App</h1>
            <ol>
                <li>
                    The first step you must create a virtual environment and install requirements
                    <ul>
                        <li>if you use windows</li>
                        <pre>
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt</pre>
                        <li>if you use linux</li>
                        <pre>
sudo apt install virtualenv
virtualenv -p py3 .venv
source .venv/bin/activate
pip3 install -r requirements.txt</pre>
                        <li>if you use macOS</li>
                        <pre>
brew install virtualenv
virtualenv -p py3 .venv
source .venv/bin/activate
pip install -r requirements.txt</pre>
                    </ul>
                </li>
            <li>
                the second step you must create .env file and set SECRET_KEY variable to this file
                <ul>
                    <li>
<pre>
touch .env
#write that to .env file
SECRET_KEY = '' # your variable</pre>
                    </li>
                </ul>
            </li>
            <li>
                the last step you must run this app
                <ul>
                    <li>
<pre>
python manage.py runserver
</pre>
                    </li>
                </ul>
            </li>
            </ol>
        </li>
    </ul>
</div>
<hr>
<div>
<h1>How it works</h1>
<p>when you run the server you must go to this page <a href="https://127.0.0.1:8000/">https://127.0.0.1:8000/</a></p>
<p>enter your city name and you will recive weather information of your city</p>
<p><strong>
info => country, city name, humidity, celsius temp, description and icon
you will see "City Not Found!" Error if your city is not in the cities list
</strong>
</p>
</div>
<div>
<hr>
<h3>I hope you enjoy that <3</h3>
</div>