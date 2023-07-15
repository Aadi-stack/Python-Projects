from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] ='08d9c1e388cbe976ae8e945842b94e14'



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



@app.route("/register", methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created for{form.Username.data}!','Success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'aaditshukla98710@gmail.com' and form.password.data == 'password':
            flash('you have been logined','Success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessfully logined.please check username and password','danger')

    return render_template('login.html',title='login',form=form)


if __name__ == '__main__':
    app.run(debug=True)