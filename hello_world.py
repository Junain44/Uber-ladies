from flask import render_template, Flask, request
import smtplib

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/about/')
@app.route('/about/<name>')
def about(name=None):
    return render_template('about.html', name=name)


@app.route('/portfolio/')
@app.route('/portfolio/<name>')
def portfolio(name=None):
    return render_template('portfolio.html', name=name)


@app.route('/contact/')
def contact(name=None):
    return render_template('contact.html', name=name)


@app.route('/email/', methods={'post'})
def email():
    s_name = request.form['sender']
    s_password = request.form['password']
    sub = request.form['subject']
    message = request.form['message']

    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        users = s_name
        receiver = 'junaingallie44@gmail.com'
        s.starttls()

        s.login(users, s_password)
        s.sendmail(users, receiver, sub, message)

        s.quit()
    except:
        print('You have an error')

    return 'Email sent'
