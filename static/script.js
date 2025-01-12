let score = 0;
let questionIndex = 0;
let questions = [];
const maxQuestions = 10;

document.addEventListener("DOMContentLoaded", () => {
    fetch("/get_questions")
        .then(response => response.json())
        .then(data => {
            questions = data;
            loadQuestion();
        });
});

function loadQuestion() {
    if (questionIndex >= maxQuestions) {
        document.getElementById("question-text").innerText = "Game Over! Your Score: " + score + "/10";
        document.getElementById("choices").innerHTML = "";
        document.getElementById("restart").style.display = "block";
        return;
    }

    let currentQuestion = questions[questionIndex];
    document.getElementById("question-text").innerText = currentQuestion.question;
    
    let choicesContainer = document.getElementById("choices");
    choicesContainer.innerHTML = "";

    let shuffledChoices = currentQuestion.choices.sort(() => Math.random() - 0.5);

    shuffledChoices.forEach(choice => {
        let button = document.createElement("button");
        button.innerText = choice;
        button.onclick = () => checkAnswer(button, choice, currentQuestion.answer);
        choicesContainer.appendChild(button);
    });
}

function checkAnswer(selectedButton, selected, correct) {
    let buttons = document.querySelectorAll("#choices button");

    buttons.forEach(button => {
        button.disabled = true;  // Disable buttons after selection
        if (button.innerText === correct) {
            button.style.backgroundColor = "green";  // Highlight correct answer in green
            button.style.color = "white";
        }
        if (button.innerText === selected && selected !== correct) {
            button.style.backgroundColor = "red";  // Highlight wrong choice in red
            button.style.color = "white";
        }
    });

    if (selected === correct) {
        score++;
    }

    document.getElementById("score").innerText = `Score: ${score}/10`;

    setTimeout(() => {
        questionIndex++;
        loadQuestion();
    }, 1500); // Delay before next question
}

function restartGame() {
    score = 0;
    questionIndex = 0;
    document.getElementById("score").innerText = "Score: 0/10";
    document.getElementById("restart").style.display = "none";

    fetch("/get_questions")
        .then(response => response.json())
        .then(data => {
            questions = data;
            loadQuestion();
        });
}
