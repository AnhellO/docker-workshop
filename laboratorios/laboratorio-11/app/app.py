from datetime import datetime
from flask import Flask, request, jsonify
from models import Question

app = Flask(__name__)

@app.route('/polls/questions/', methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        question_text = request.form['question_text']
        pub_date = datetime.strptime(request.form['pub_date'], '%Y-%m-%d')
        question = Question(question_text=question_text, pub_date=pub_date)
        question.save()
        return {'question_text': question.question_text, 'id': question.id, 'pub_date': question.pub_date.strftime('%Y-%m-%d')}

    questions = Question.select()
    l = []
    for question in questions:
        l.append({'question_text': question.question_text, 'id': question.id, 'pub_date': question.pub_date.strftime('%Y-%m-%d')})
    return jsonify(l)