import streamlit as st
import gemini as gem

# Function to call Gemini API
def get_career_suggestions(answers):

    response = gem.question(answers)
    if response:
        return response
    else:
        return None

# Streamlit app
st.title('Career Guidance Portal')

# Preliminary career choice input
specific_career = st.text_input("If you have a specific career in mind, please enter it here:")

# Define the questions
questions = [
    "(Enter your name & answer): What activities or hobbies do you find yourself most engaged in during your free time?",
    "When faced with a challenging problem, how do you typically approach finding a solution?",
    "What subjects did you enjoy the most during your education? Why?",
    "If you could shadow any professional for a day, who would it be and why?",
    "What are your long-term career goals, or what impact do you hope to make in your future career?",
    "How do you prioritize between stability and innovation in your career choices?",
    "Describe a project or task you completed that you felt particularly proud of. What about it was fulfilling?",
    "If you had to choose between a career that pays well but you're less passionate about versus a lower-paying career that aligns with your interests, which would you choose and why?",
    "What skills or knowledge would you like to develop further?",
    "If you could change one thing about your current job or academic path, what would it be?"
]

# Initialize session state
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0
if 'answers' not in st.session_state:
    st.session_state.answers = []

# Function to reset the session state
def restart_chat():
    st.session_state.current_question_index = 0
    st.session_state.answers = []
    st.experimental_rerun()

# Show questions one by one
if specific_career:
    st.write(f"Based on your input, you are interested in a career in {specific_career}.")
    # st.write(f"Here's a quick roadmap to help you explore more about {specific_career} :")
    st.session_state.answers.append(f'specific career:{specific_career}')
    suggestion = get_career_suggestions(f'{st.session_state.answers}')
    st.write(suggestion)


else:
    if st.session_state.current_question_index < len(questions):
        current_question = questions[st.session_state.current_question_index]
        answer = st.text_input(current_question, key=current_question)
        if st.button('Next'):
            if answer:
                st.session_state.answers.append(answer)
                st.session_state.current_question_index += 1
                st.experimental_rerun()
            else:
                st.write('Please provide an answer to proceed.')
    else:
        # Once all questions are answered, get career suggestions
        suggestions = get_career_suggestions(st.session_state.answers)
        if suggestions:
            st.write('Based on your answers, here are some possible career paths for you:')
            st.write(suggestions)
        else:
            st.write('Sorry, there was an error fetching career suggestions. Please try again.')

        # Add a button to restart the chat for a new user
        if st.button('Restart'):
            restart_chat()

