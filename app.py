from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

messages = []  # store typed messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form.get('message')
        if msg:
            messages.append(msg)
        return redirect(url_for('index'))
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # or any other available port
