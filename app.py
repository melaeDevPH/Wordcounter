from flask import Flask, render_template, request
import re

app = Flask(__name__)

def count_words(text):
    """Count total words in the text."""
    return len(re.findall(r'\b\w+\b', text))

def count_sentences(text):
    """Count the number of sentences based on punctuation."""
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def count_characters(text):
    """Return character length of the input."""
    return len(text)

def estimate_reading_time(word_count):
    """Estimate reading time in minutes (200 WPM)."""
    return round(word_count / 200, 2)


@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize values
    word_count = sentence_count = char_count = reading_time = 0
    input_text = ""

    if request.method == "POST":
        action = request.form.get("action")
        
        if action == "submit":
            input_text = request.form.get("input_text", "")
            word_count = count_words(input_text)
            char_count = count_characters(input_text)
            sentence_count = count_sentences(input_text)
            reading_time = estimate_reading_time(word_count)

        elif action == "reset":
            input_text = ""

    return render_template(
        "index.html",
        input_text=input_text,
        word_count=word_count,
        sentence_count=sentence_count,
        char_count=char_count,
        reading_time=reading_time
    )

if __name__ == "__main__":
    app.run(debug=True)
