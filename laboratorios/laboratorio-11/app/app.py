from datetime import datetime
from flask import Flask, request, jsonify, render_template
from models import Question

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/polls/questions/', methods=['GET', 'POST', 'DELETE'])
def questions():
    if request.method == 'POST':
        question_text = request.form['question_text']
        pub_date = datetime.strptime(request.form['pub_date'], '%Y-%m-%d')
        question = Question(question_text=question_text, pub_date=pub_date)
        question.save()
        return {'question_text': question.question_text, 'id': question.id, 'pub_date': question.pub_date.strftime('%Y-%m-%d')}, 201
    
    if request.method == 'DELETE':
        result = Question.delete().where(Question.id == request.form['id']).execute() # DELETE FROM question WHERE id == {id};
        return {"removed": result}, 204

    questions = Question.select()
    l = []
    for question in questions:
        l.append({'question_text': question.question_text, 'id': question.id, 'pub_date': question.pub_date.strftime('%Y-%m-%d')})
    return jsonify(l)