from flask import Flask, render_template, request, url_for, jsonify, json

import os

app = Flask(__name__)
list_icon = "fa fa-trash-o"
notes = []


class AddNotes:
    count = 0

    def __init__(self, color=None, note=None, id=None):
        self.color = color
        self.note = note
        self.id = id
        AddNotes.count += 1

    def __str__(self):
        return self.color, self.note, self.id


@app.route('/deletenotes/<int:id>',methods=['POST','GET'])
def delete(id):
    for index, note in enumerate(notes):
        if note.id == id:
            notes.pop(index)
    return render_template('index.html', notes=notes)

@app.route('/', methods=['POST', 'GET'])
def insert_notes():
    if request.method == 'POST':
        arrayLength = notes.__len__()
        if(arrayLength == 0):
            print(arrayLength)
            note = AddNotes(request.form['color'], request.form['notes'], 0)
            notes.append(note)
        else:
            length = notes.__len__()
            print(length)
            lastnote = notes[length-1]
            lastid = lastnote.id
            print(lastid)
            note = AddNotes(request.form['color'], request.form['notes'], lastid+1)
            notes.append(note)
            print(notes)
    return render_template('index.html', notes=notes)


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


if __name__ == '__main__':
    app.debug = True
    app.run()