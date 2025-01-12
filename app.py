from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

questions_pool = [
    {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "choices": ["Mars", "Earth", "Venus", "Jupiter"], "answer": "Mars"},
    {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Which ocean is the largest?", "choices": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "Who discovered gravity?", "choices": ["Einstein", "Newton", "Galileo", "Tesla"], "answer": "Newton"},
    {"question": "Which is the longest river in the world?", "choices": ["Amazon", "Nile", "Yangtze", "Mississippi"], "answer": "Nile"},
    {"question": "What is the freezing point of water?", "choices": ["0°C", "100°C", "50°C", "-10°C"], "answer": "0°C"},
    {"question": "Who painted the Mona Lisa?", "choices": ["Michelangelo", "Van Gogh", "Picasso", "Da Vinci"], "answer": "Da Vinci"},
    {"question": "What is the national bird of the USA?", "choices": ["Eagle", "Peacock", "Sparrow", "Ostrich"], "answer": "Eagle"},
    {"question": "Which language has the most speakers?", "choices": ["English", "Spanish", "Mandarin", "Hindi"], "answer": "Mandarin"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_questions')
def get_questions():
    selected_questions = random.sample(questions_pool, 10)  # Pick 10 unique questions
    return jsonify(selected_questions)

if __name__ == '__main__':
    app.run(debug=True)
