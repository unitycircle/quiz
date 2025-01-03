let score = 0;
let questionCount = 0;
const maxQuestions = 10;

document.addEventListener("DOMContentLoaded", () => {
    loadQuestion();
});

function loadQuestion() {
    if (questionCount >= maxQuestions) {
        document.getElementById("question-text").innerText = "Game Over! Your Score: " + score;
        document.getElementById("choices").innerHTML = "";
        document.getElementById("restart").style.display = "block";
        return;
    }

    fetch("/get_question")
        .then(response => response.json())
        .then(data => {
            document.getElementById("question-text").innerText = data.question;
            let choicesContainer = document.getElementById("choices");
            choicesContainer.innerHTML = "";

            let shuffledChoices = data.choices.sort(() => Math.random() - 0.5);

            shuffledChoices.forEach(choice => {
                let button = document.createElement("button");
                button.innerText = choice;
                button.onclick = () => checkAnswer(choice, data.answer);
                choicesContainer.appendChild(button);
            });
        });
}

function checkAnswer(selected, correct) {
    if (selected === correct) {
        score++;
        document.getElementById("score").innerText = "Score: " + score;
    }
    questionCount++;
    loadQuestion();
}

function restartGame() {
    score = 0;
    questionCount = 0;
    document.getElementById("score").innerText = "Score: 0";
    document.getElementById("restart").style.display = "none";
    loadQuestion();
}
