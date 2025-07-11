from flask import Flask, render_template, request
import random, os

app = Flask(__name__)

affirmations = {
    'happy': [
        "Your happiness is contagious!",
        "Keep shining bright like you always do.",
        "Every day is a new opportunity for joy.",
        "Your positivity inspires everyone around you."
    ],
    'sad': [
        "This feeling is temporary and you will overcome it.",
        "You are stronger than any challenge you face.",
        "Every storm runs out of rain. You will smile again.",
        "Your strength will carry you through."
    ],
    'anxious': [
        "You are capable of handling whatever comes your way.",
        "Take a deep breath; you are doing great.",
        "One step at a time, you are making progress.",
        "You have overcome challenges before and can do it again."
    ],
    'angry': [
        "It's okay to take a break and breathe.",
        "Letting go of anger gives you peace.",
        "You have control over how you react and respond.",
        "Your calm mind is your superpower."
    ],
    'stressed': [
        "You have survived every bad day so far, you can handle this too.",
        "Taking small breaks can help clear your mind.",
        "You are doing your best and that is enough.",
        "This moment of stress will pass, you will find peace."
    ],
    'general': [
        "You are worthy of love and kindness.",
        "Believe in yourself and all that you do.",
        "You have the power to create change.",
        "Every moment is a fresh beginning."
    ]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_mood = request.form.get('mood', '').lower()
        mood_category = 'general'

        if any(word in user_mood for word in ['happy', 'joy', 'good', 'great']):
            mood_category = 'happy'
        elif any(word in user_mood for word in ['sad', 'down', 'unhappy', 'depressed']):
            mood_category = 'sad'
        elif any(word in user_mood for word in ['anxious', 'nervous', 'worried', 'fear']):
            mood_category = 'anxious'
        elif any(word in user_mood for word in ['angry', 'mad', 'irate', 'furious']):
            mood_category = 'angry'
        elif any(word in user_mood for word in ['stressed', 'stress', 'overwhelmed']):
            mood_category = 'stressed'

        affirmation = random.choice(affirmations[mood_category])
        return render_template('index.html', affirmation=affirmation, mood=user_mood)

    return render_template('index.html', affirmation=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
