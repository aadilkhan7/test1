from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

from datetime import datetime, timezone, timedelta

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)


@app.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)


@app.route('/add', methods=['POST'])
def add_note():
    content = request.form['content']
    new_note = Note(content=content)
    db.session.add(new_note)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = Note.query.get_or_404(note_id)
    if request.method == 'POST':
        note.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', note=note)


@app.route('/delete/<int:note_id>', methods=['GET', 'POST'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=7777)
