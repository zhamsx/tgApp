from flask import Flask, render_template  # render_template нужно импортировать

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Эта функция ищет файл index.html в папке templates

if __name__ == '__main__':
    app.run(debug=True)
