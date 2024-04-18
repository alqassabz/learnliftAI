from flask import Flask, render_template, request
import nltk
from nltk.tokenize import word_tokenize
from transformers import pipeline, set_seed

# Download NLTK resources
nltk.download('punkt')

# Initialize Flask app
app = Flask(__name__)

# Use a smaller GPT-Neo model for question generation
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B', max_length=200)

# Use a question-answering model
qa_model = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad')

# Set a seed for reproducibility
set_seed(42)

# Function to answer a question based on provided text
def answer_question(text, question):
    try:
        # Adjust the context window to provide more surrounding text
        context_window = text[:1000]  # Get the first 1000 characters as context
        answer = qa_model(question=question, context=context_window)

        # Extract the segment before the answer
        segment_before = context_window[:answer['start']].strip()
        # Find the last full stop before the answer
        last_full_stop_before = segment_before.rfind('.')
        segment_before = segment_before[last_full_stop_before + 1:].strip()

        # Extract the answer
        answer_segment = answer['answer']

        # Extract the segment after the answer
        segment_after = context_window[answer['end']:].strip()
        # Find the first full stop after the answer
        first_full_stop_after = segment_after.find('.')
        segment_after = segment_after[:first_full_stop_after].strip()

        return segment_before, answer_segment, segment_after
    except Exception as e:
        print(f"Error answering question: {question}\nError: {e}")
        return None, None, None

# Function to generate questions using the first approach with filtering
def generate_questions_approach1_with_filtering(text, max_questions=10, max_length=200):
    try:
        # Tokenize the input text and tag the part-of-speech
        tokens = word_tokenize(text)
        pos_tags = nltk.pos_tag(tokens)

        # Extract nouns from the input text
        nouns = [word for word, pos in pos_tags if pos.startswith('NN')]

        # Define the prompt
        prompt = f"Generate questions for the following text:\n{text}\n\nQuestions:"

        # Generate questions
        generated_text = generator(prompt, max_length=200, num_return_sequences=max_questions, temperature=0.6)

        # Extract the generated text
        generated_text = generated_text[0]['generated_text']

        # Split the generated text into separate questions
        questions = [question.strip() for question in generated_text.split('\n') if question.strip().endswith('?')]

        # Filter questions based on relevance
        relevant_questions = []
        for question in questions:
            answer_before, answer_segment, answer_after = answer_question(text, question)
            if answer_segment:
                # Check if the noun in the question is present in the input text
                question_tokens = word_tokenize(question)
                question_nouns = [word for word, pos in nltk.pos_tag(question_tokens) if pos.startswith('NN')]
                if any(noun in nouns for noun in question_nouns):
                    relevant_questions.append((question, answer_before, answer_segment, answer_after))

        return relevant_questions
    except Exception as e:
        print(f"Error generating questions for text (Approach 1 with filtering): {text}\nError: {e}")
        return []
