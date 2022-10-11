from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/count')
def count():
    return redirect('/')

@app.route('/count2')
def count2():
    if 'custom_number' in session:
        session['count'] += session['custom_number'] - 1
    else:
        session['count'] += 1
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/custom', methods=['GET','POST'])
def custom():
    session['custom_number'] = int(request.form.get('custom_number'))
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)