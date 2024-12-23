import webbrowser

def generate_quiz():
    # Questions with answers in lowercase
    questions = [
        {"question": "What is the capital of India?", "answer": "new delhi"},
        {"question": "Who is known as the Father of the Nation in India?", "answer": "mahatma gandhi"},
        {"question": "In which year did India gain independence from British rule?", "answer": "1947"},
        {"question": "What is the national animal of India?", "answer": "bengal tiger"},
        {"question": "Which Indian city is known as the 'Pink City'?", "answer": "jaipur"},
        {"question": "Which river is considered the longest river in India?", "answer": "ganga"},
        {"question": "Who was the first Prime Minister of independent India?", "answer": "jawaharlal nehru"},
        {"question": "What is the name of the famous monument built by Shah Jahan in memory of his wife Mumtaz Mahal?", "answer": "taj mahal"},
        {"question": "What is the national flower of India?", "answer": "lotus"},
        {"question": "Which is the largest state in India by area?", "answer": "rajasthan"},
    ]

    # Generate HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>India General Knowledge Quiz</title>
    </head>
    <body>
        <h1>India General Knowledge Quiz</h1>
        <form id="quiz-form">
    """

    # Add questions to HTML
    for idx, q in enumerate(questions):
        html_content += f"""
        <div>
            <p>{idx + 1}. {q['question']}</p>
            <input type="text" name="answer{idx}" placeholder="Your answer here">
        </div>
        """

    # Add submit button and result section
    html_content += """
        <button type="button" onclick="submitQuiz()">Submit</button>
        </form>
        <div id="result"></div>

        <script>
            function submitQuiz() {
                // Correct answers in lowercase
                const correctAnswers = [""" + ", ".join([f'"{q["answer"]}"' for q in questions]) + """];
                const form = document.getElementById('quiz-form');
                const inputs = form.querySelectorAll('input');
                let score = 0;

                inputs.forEach((input, idx) => {
                    if (input.value.trim().toLowerCase() === correctAnswers[idx]) {
                        score++;
                    }
                });

                document.getElementById('result').innerHTML = `Your score is ${score} out of ${correctAnswers.length}.`;
            }
        </script>
    </body>
    </html>
    """

    # Save to an HTML file
    with open("index.html", "w") as file:
        file.write(html_content)

    # Open in the default web browser
    webbrowser.open("index.html")

# Run the function
generate_quiz()
