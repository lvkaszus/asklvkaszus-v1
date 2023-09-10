from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form['question']
        if question.strip():
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('questions.txt', 'a') as file:
                file.write(now + ', ' + question + ', TODO' + '\n')
            return render_template('success.html')
        else:
            return render_template('fail.html')
    else:
        questions = []
        with open('questions.txt', 'r') as file:
            lines = reversed(file.readlines())
            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split(', ')
                    date_str = parts[0]
                    question_str = parts[1]
                    if len(parts) == 3:
                        answer_str = parts[2]
                    else:
                        answer_str = None

                    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                    questions.append((date, question_str, answer_str))

        return render_template('index.html', questions=questions)

@app.route('/rate_limit')
def rate_limit():
	return render_template('rate_limit.html')

if __name__ == '__main__':
    app.run()
