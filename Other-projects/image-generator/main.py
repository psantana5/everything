from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form.get('prompt')
    genre = request.form.get('genre')
    mood = request.form.get('mood')
    length = request.form.get('length')

    # Modify the prompt to include the genre and mood
    modified_prompt = f"A {genre} story, with a {mood} mood: {prompt}"

    # Adjust the max tokens based on the desired length
    max_tokens = {
        'short': 500,
        'medium': 1000,
        'long': 2000
    }.get(length, 500)

    # Send a request to the OpenAI API to generate the story
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=modified_prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7
    )

    story = response.choices[0].text.strip()

    return story

if __name__ == '__main__':
    app.run(debug=True)