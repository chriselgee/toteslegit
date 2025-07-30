from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', '359bynpq3a9tynbqap39tyn4')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect(url_for('flag'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/flag')
def flag():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('flag.html', flag='FLAG{firewall_admin_access}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
