import re
import nltk
import smtplib
from email.mime.text import MIMEText
import joblib
import urllib

# Definir URL del modelo ML
model_url = 'https://github.com/RamyaSree-git/ML-model-for-Phishing-Websites-Detection/blob/main/phishing_classifier.pkl'

try:
    urllib.request.urlretrieve(model_url, 'phishing_classifier.pkl')
except urllib.error.HTTPError as e:
    print(f'Error downloading the ML model: {e}')
    exit()

# Cargar Modelo ML
model = joblib.load('phishing_model.pkl')

# Define a function to preprocess the email text
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove email headers
    text = re.sub(r'^.*\n', '', text)
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    # Remove non-alphanumeric characters
    text = re.sub(r'[^a-z0-9 ]', '', text)
    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    # Remove stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [token for token in tokens if token not in stopwords]
    # Join the tokens back into a string
    text = ' '.join(tokens)
    return text

# Define the sender, recipient, and email text
sender = 'sender@example.com'
recipient = 'recipient@example.com'
subject = 'Important information'
body = 'Dear customer, please verify your account information by clicking on the following link: http://example.com/verify'

# Preprocess the email text
preprocessed_body = preprocess_text(body)

# Predict whether the email is a phishing attempt using the ML model
prediction = model.predict([preprocessed_body])

# If the email is predicted to be a phishing attempt, print a message and send an email notification
if prediction == 1:
    print('Possible phishing email detected.')
    
    # Send an email notification
    sender = 'sender@example.com'
    recipient = 'recipient@example.com'
    subject = 'Possible phishing email detected'
    body = 'A possible phishing email was detected at {datetime.now()}. Please investigate.'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    s = smtplib.SMTP('localhost')
    s.sendmail(sender, [recipient], msg.as_string())
    s.quit()
else:
    print('Email is not a phishing attempt.')