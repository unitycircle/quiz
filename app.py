from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

questions = [
    {"question": "What is the capital of France?", "choices": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "choices": ["Mars", "Earth", "Venus", "Jupiter"], "answer": "Mars"},
    {"question": "What is 2 + 2?", "choices": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Which ocean is the largest?", "choices": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"},
    {"question": "What is the chemical symbol for gold?", "choices": ["Ag", "Au", "Pb", "Fe"], "answer": "Au"},
    {"question": "How many continents are there?", "choices": ["5", "6", "7", "8"], "answer": "7"},
    {"question": "Who wrote 'Romeo and Juliet'?", "choices": ["Shakespeare", "Hemingway", "Tolstoy", "Austen"], "answer": "Shakespeare"},
    {"question": "What is the square root of 81?", "choices": ["7", "8", "9", "10"], "answer": "9"},
    {"question": "Which gas do plants absorb?", "choices": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "answer": "Carbon Dioxide"},
    {"question": "What is the largest mammal?", "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": "Blue Whale"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question')
def get_question():
    question = random.choice(questions)
    return jsonify(question)

if __name__ == '__main__':
    app.run(debug=True)
