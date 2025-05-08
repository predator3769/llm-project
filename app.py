import os
from dotenv import load_dotenv

from flask import Flask, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from forms import FileForm, TextForm
from llm import output, create_cache

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

global cache

if __name__=='main':
    app.run(debug=True, port=8050, host='0.0.0.0')


@app.route('/', methods=['GET', 'POST'])
def display_form():
    global cache
    form = FileForm()
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)
        filepath = f'instance/uploads/{filename}'
        f.save(os.path.join(app.instance_path, 'uploads', filename))
        cache = create_cache(filepath)
        text = "DummyText"
        return redirect(url_for('queries', text=text))
    return render_template('index.html', title='Home Page', form=form)

@app.route('/query/<text>', methods=['GET', 'POST'])
def queries(text):
    global cache
    form = TextForm()
    if form.validate_on_submit():
        text = output(cache, form.text.data)
        return redirect(url_for('queries', text=text))
    return render_template('question.html', title='Questions', text=text, form=form)