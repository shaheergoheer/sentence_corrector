from flask import Flask, jsonify, request
from dotenv import load_dotenv
from gpt import MODEL

app = Flask(__name__)

load_dotenv()

# Create an instance of the MODEL class
model_instance = MODEL()

@app.route('/')
def home():
    return "Welcome to the sentence correction app!"

@app.route('/improve', methods=['POST'])
def improve_sentence():
    """
    Corrects and improves the given sentence.

    **Input:**
    - **Content-Type**: `application/json`
    - **Request Body**: 
      - **`sentence`** (string): The sentence to be improved.
      
      **Example:**
      ```json
      {
          "sentence": "Ths is a smple sentence with a few typoos."
      }
      ```

    **Output:**
    - **Content-Type**: `application/json`
    - **Response Body**: 
      - **`improved_sentence`** (string): The corrected and improved sentence.
      
      **Example:**
      ```json
      {
          "improved_sentence": "This is a simple sentence with a few typos."
      }
      ```
    """
    # Get the user prompt from the request body
    data = request.get_json()
    user_prompt = data.get('sentence')

    # If sentence is not provided, return an error
    if not user_prompt:
        return jsonify({'error': 'Sentence is required'}), 400

    # Get the improved response from GPT
    try:
        response_text = model_instance.get_response(user_prompt)
        return jsonify({'improved_sentence': response_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

