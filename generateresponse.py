!pip install --upgrade google-generativeai

import google.generativeai as genai

# Set up the API key
GOOGLE_API_KEY = 'AIzaSyB6vU4YmM5HJESBaB1u_8TOPsp6_YjmDr4'
genai.configure(api_key=GOOGLE_API_KEY)

# Load the generative model
model = genai.GenerativeModel('gemini-1.5-pro')  # Ensure the model is correctly set up

def suggest_response_type(question):
    """
    Suggests the most appropriate response type for a given question.
    """
    return query_model_for_response_type(question.lower().strip())

def query_model_for_response_type(question):
    """
    Queries the Gemini model to analyze the question and suggest the most appropriate response type.
    """
    prompt = (

        "Analyze the given question and suggest the most appropriate response type from the given options "
        "options: Text Box, Integer, File Input (doc, image etc.), "
        "Rating/Scale Questions, Date, Binary type (like yes/no), Dropdown (multiple choices).\n\n"
        f"Question: {question}\n\n"
        "Response Type:"
        "provide only the response type , not explaination"
    )
    try:
        # Call the Gemini model and get a response
        response = model.generate_content(prompt)
        if response and hasattr(response, 'text'):  # Ensure the response contains text
            return response.text.strip()
        else:
            return "Error: Unexpected response format or empty response."
    except Exception as e:
        return f"Error querying the Gemini model: {e}"

def integrate_question_suggestion():
    """
    Interactive loop to input questions and get response type suggestions.
    """
    print("\nWelcome to the Gemini Response Type Suggestion Tool!")
    print("Type your question and get the suggested response type. Type 'exit' to quit.\n")
    while True:
        question = input("Type your question: ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        # Get the response type suggestion dynamically
        response_type = suggest_response_type(question)
        print("Suggested Response Type:", response_type)

# Run the interactive tool
integrate_question_suggestion()
