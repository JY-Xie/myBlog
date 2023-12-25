from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')


@app.route('/articles')
def articles():
    return render_template('articles.html')


@app.route('/photos')
def photos():
    photos_urls = [
        'photos/1(1).jpg',
        'photos/1(2).jpg',
    ]
    return render_template('photos.html', photos_urls=photos_urls)


if __name__ == '__main__':
    app.run(debug=True)
