from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from models import create_entry, get_entries, delete_entry

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET','POST'])

def index():
    if request.method == 'POST':
        name = request.form.get('name')
        cont = request.form.get('content')
        create_entry(name, cont)

    data = get_entries()

    return render_template('index.html', posts=data)

@app.route('/delete/<id>')
def delete_post(id):
    delete_entry(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)