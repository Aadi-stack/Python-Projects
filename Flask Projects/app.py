from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Aadit',
        'title': 'Blog Post 1',
        'content': 'Deep learning in toward data science',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Shukla',
        'title': 'Blog Post 2',
        'content': 'Balanced and Imbalanced Dataset',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)