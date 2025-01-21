<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Who Wants to Be a Millionaire?</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('https://upload.wikimedia.org/wikipedia/en/8/8d/WWTBAM_Logo.png');
            background-size: cover;
            background-position: center;
            color: #fff;
            text-align: center;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: rgba(0, 0, 0, 0.8);
            border-radius: 10px;
        }
        .question {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .answers {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }
        .answer {
            padding: 10px;
            border: 2px solid #fff;
            border-radius: 5px;
            cursor: pointer;
            background-color: #444;
            color: #fff;
        }
        .answer.correct {
            background-color: green;
        }
        .answer.wrong {
            background-color: red;
        }
        .lifeline {
            margin-top: 20px;
            margin-right: 10px;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .lifeline:disabled {
            background-color: grey;
            cursor: not-allowed;
        }
        .lifeline:hover {
            background-color: #0056b3;
        }
        .result {
            display: none;
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
        }
        .next-button {
            display: none;
            margin-top: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .signature {
            margin-top: 30px;
            font-size: 14px;
            color: #ccc;
        }
        .signature a {
            color: #007bff;
            text-decoration: none;
        }
        .signature a:hover {
            text-decoration: underline;
        }
        .score {
            margin-top: 20px;
            font-size: 20px;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Who Wants to Be a Millionaire?</h1>
        <div class="question" id="question">Question will go here</div>
        <div class="answers">
            <div class="answer" id="answer1" onclick="checkAnswer(0)"></div>
            <div class="answer" id="answer2" onclick="checkAnswer(1)"></div>
            <div class="answer" id="answer3" onclick="checkAnswer(2)"></div>
            <div class="answer" id="answer4" onclick="checkAnswer(3)"></div>
        </div>
        <button class="lifeline" id="lifeline5050" onclick="useLifeline('5050')">50:50</button>
        <button class="lifeline" id="lifelineAudience" onclick="useLifeline('audience')">Ask the Audience</button>
        <button class="lifeline" id="lifelinePhone" onclick="useLifeline('phone')">Phone a Friend</button>
        <div class="result" id="result"></div>
        <button class="next-button" id="nextButton" onclick="nextQuestion()">Next Question</button>
        <div class="score" id="score"></div>
        <!-- Signature -->
        <div class="signature">
            &copy; 2025 Daniel Rojas | &#9993; <a href="mailto:unitedartistsinstitute@gmail.com">unitedartistsinstitute@gmail.com</a>
        </div>
    </div>

    <script>
        const questions = [
            { question: "What does IELTS stand for?", answers: ["International Education Language Test", "International English Language Testing System", "International English Learning Test Service", "International English Listening Test"], correct: 1 },
            { question: "How many sections are there in the IELTS Listening test?", answers: ["2", "3", "4", "5"], correct: 2 },
            { question: "Which of the following skills are tested in the IELTS exam?", answers: ["Reading, Writing, Listening, Speaking", "Grammar, Vocabulary, Reading, Listening", "Speaking, Reading, Vocabulary, Writing", "Writing, Listening, Grammar, Pronunciation"], correct: 0 },
            { question: "How long is the IELTS Speaking test?", answers: ["5–10 minutes", "11–14 minutes", "20–25 minutes", "15–20 minutes"], correct: 1 },
            { question: "What is the total duration of the IELTS Academic and General Training tests?", answers: ["2 hours 30 minutes", "3 hours", "2 hours 45 minutes", "3 hours 15 minutes"], correct: 2 },
            { question: "What is the minimum score required to pass the IELTS exam?", answers: ["5.0", "6.0", "7.0", "There is no pass/fail score"], correct: 3 },
            { question: "Which section of the IELTS exam is the same for both Academic and General Training?", answers: ["Reading", "Writing", "Listening", "Speaking"], correct: 3 },
            { question: "How many times can you take the IELTS exam?", answers: ["Once", "Twice", "Three times", "As many times as you want"], correct: 3 },
            { question: "What is the maximum score you can achieve in the IELTS exam?", answers: ["8.0", "9.0", "10.0", "There is no maximum score"], correct: 1 },
            { question: "Which of the following is NOT a type of IELTS exam?", answers: ["Academic", "General Training", "Professional", "UKVI"], correct: 2 },
            { question: "How long is the IELTS Listening test?", answers: ["30 minutes", "40 minutes", "50 minutes", "60 minutes"], correct: 0 },
            { question: "What is the format of the IELTS Writing test?", answers: ["One essay", "Two essays", "One essay and one report", "One essay and one letter"], correct: 1 },
            { question: "Which of the following is a common topic in the IELTS Speaking test?", answers: ["Politics", "Hobbies", "Religion", "Sports"], correct: 1 },
            { question: "How many parts are there in the IELTS Speaking test?", answers: ["2", "3", "4", "5"], correct: 1 },
            { question: "What is the duration of the IELTS Reading test?", answers: ["30 minutes", "40 minutes", "50 minutes", "60 minutes"], correct: 3 },
            { question: "Which of the following is a common mistake in the IELTS Writing test?", answers: ["Using informal language", "Writing too much", "Using bullet points", "All of the above"], correct: 0 },
            { question: "What is the purpose of the IELTS exam?", answers: ["To test your English proficiency", "To test your knowledge of British culture", "To test your academic skills", "To test your general knowledge"], correct: 0 },
            { question: "Which of the following is a valid IELTS score?", answers: ["4.5", "5.5", "6.5", "All of the above"], correct: 3 },
            { question: "How many times a year is the IELTS exam conducted?", answers: ["4", "12", "24", "48"], correct: 3 },
            { question: "Which of the following is a common resource for IELTS preparation?", answers: ["Cambridge IELTS books", "TOEFL practice tests", "GRE study guides", "SAT prep books"], correct: 0 }
        ];

        let currentQuestion = 0;
        let lifelinesUsed = { '5050': false, 'audience': false, 'phone': false };
        let score = 0;

        function loadQuestion() {
            const questionElement = document.getElementById('question');
            const answersElement = document.querySelectorAll('.answer');
            const resultElement = document.getElementById('result');
            const nextButton = document.getElementById('nextButton');

            questionElement.textContent = questions[currentQuestion].question;
            answersElement.forEach((answer, index) => {
                answer.textContent = questions[currentQuestion].answers[index];
                answer.classList.remove('correct', 'wrong');
                answer.style.visibility = 'visible';
            });
            resultElement.style.display = 'none';
            nextButton.style.display = 'none';
        }

        function checkAnswer(selected) {
            const correct = questions[currentQuestion].correct;
            const resultElement = document.getElementById('result');
            const answersElement = document.querySelectorAll('.answer');

            answersElement.forEach((answer, index) => {
                if (index === correct) {
                    answer.classList.add('correct');
                } else if (index === selected) {
                    answer.classList.add('wrong');
                }
            });

            if (selected === correct) {
                resultElement.textContent = "Correct!";
                resultElement.style.color = "green";
                score++;
            } else {
                resultElement.textContent = "Incorrect!";
                resultElement.style.color = "red";
            }

            resultElement.style.display = "block";
            document.getElementById('nextButton').style.display = 'block';
        }

        function useLifeline(lifeline) {
            const answersElement = document.querySelectorAll('.answer');
            const correct = questions[currentQuestion].correct;

            if (lifeline === '5050' && !lifelinesUsed['5050']) {
                lifelinesUsed['5050'] = true;
                const incorrectAnswers = [0, 1, 2, 3].filter(i => i !== correct);
                const randomIncorrect = incorrectAnswers.sort(() => 0.5 - Math.random()).slice(0, 2);
                answersElement.forEach((answer, index) => {
                    if (index !== correct && randomIncorrect.includes(index)) {
                        answer.style.visibility = 'hidden';
                    }
                });
            } else if (lifeline === 'audience' && !lifelinesUsed['audience']) {
                lifelinesUsed['audience'] = true;
                alert(`Audience suggests answer ${correct + 1}!`);
            } else if (lifeline === 'phone' && !lifelinesUsed['phone']) {
                lifelinesUsed['phone'] = true;
                alert(`Your friend suggests answer ${correct + 1}!`);
            }

            document.getElementById(`lifeline${lifeline.charAt(0).toUpperCase() + lifeline.slice(1)}`).disabled = true;
        }

        function nextQuestion() {
            currentQuestion++;
            if (currentQuestion < questions.length) {
                loadQuestion();
            } else {
                document.getElementById('question').textContent = "Congratulations! You've completed the quiz.";
                document.querySelector('.answers').innerHTML = '';
                document.getElementById('result').style.display = 'none';
                document.getElementById('nextButton').style.display = 'none';
                document.getElementById('score').textContent = `Your final score is ${score} out of ${questions.length}.`;
            }
        }

        window.onload = loadQuestion;
    </script>
</body>
</html>
