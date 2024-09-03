import streamlit as st
import json

questions = [
   {
        'question': 'What is 30 + 4?',
        'options': ['33', '34', '25'],
        'answer': '34'
    },
    {
        'question': 'What is the capital of India?',
        'options': ['Tamil Nadu', 'Delhi', 'Kerla'],
        'answer': 'Delhi'
    },
    {
        'question': 'How do you pass the Hexaware CODE&RISE PROGRAM?',
        'options': [
            'Try everything',
            'Try everything',
            'Try everything',
            'All of the above'
        ],
        'answer': 'All  of the above'
    },
    {
        'question': 'What is RISE in the context of technology?',
        'options': [
            'A framework for software development',
            'A cloud computing service',
            'A training program for developers'
        ],
        'answer': 'A framework for software development'
    },
    {
        'question': 'Which of the following is a common data structure?',
        'options': ['Array', 'String', 'Integer'],
        'answer': 'Array'
    },
    {
        'question': 'What is the purpose of version control systems?',
        'options': [
            'Track changes to code',
            'Manage server configurations',
            'Monitor application performance'
        ],
        'answer': 'Track changes to code'
    },
    {
        'question': 'Which language is primarily used for web development?',
        'options': ['Python', 'JavaScript', 'C++'],
        'answer': 'JavaScript'
    },
    {
        'question': 'What does API stand for?',
        'options': ['Application Programming Interface', 'Automated Process Integration', 'Advanced Programming Instruction'],
        'answer': 'Application Programming Interface'
    },
   
]

users = {
    'student': 'password',
    'teacher': 'password'
}

def load_questions():
    """Load questions from a JSON file."""
    try:
        with open('questions.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_questions(questions):
    """Save questions to a JSON file."""
    with open('questions.json', 'w') as file:
        json.dump(questions, file)

def inject_custom_css():
    """Inject custom CSS styles into the Streamlit app."""
    st.markdown("""
       <img src="https://th.bing.com/th/id/OIP.y1VbyF9uecJ0dhB15AEMsAHaEN?rs=1&pid=ImgDetMain" alt="Paris" width="900" height="300">
        <style>
        /* Style the login form */
        .login-form {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 20px;
            background-color: white;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width: 700px;
            box-sizing: border-box; /* Ensure padding is included in the width */
        }
        .login-form input {
            border: 2px solid #4CAF50;
            border-radius: 4px;
            padding: 10px;
            width: 100%;
            margin-bottom: 10px;
            box-sizing: border-box; /* Ensure padding is included in the width */
        }
        .login-form button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 10px;
            cursor: pointer;
            width: 100%;
            box-sizing: border-box; /* Ensure padding is included in the width */
        }
        .login-form button:hover {
            background-color: #45a049;
        }
        /* Style for the forgot password link */
        .forgot-password {
            color: #4CAF50;
            cursor: pointer;
            text-decoration: underline;
            font-size: 14px;
        }
        /* Remove Streamlit default margins */
        .stApp {
            margin: 0;
            padding: 0;
        }
        /* Align remember me and forgot password link */
        .remember-forgot {
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        </style>
    """, unsafe_allow_html=True)

def login():
    """Handle user login through the center of the page."""
    st.markdown('<div class="full-height">', unsafe_allow_html=True)
    st.markdown('<div class="login-form">', unsafe_allow_html=True)
    
    st.write('<h2 style="text-align: center;">Login</h2>', unsafe_allow_html=True)
    
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    
    st.markdown('<div class="remember-forgot">', unsafe_allow_html=True)
    
    remember_me = st.checkbox('Remember Me')
    
    st.markdown('<a class="forgot-password" href="#">Forgot Password</a>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button('Login'):
        if username in users and users[username] == password:
            st.session_state['logged_in'] = True
            st.session_state['role'] = 'student' if username == 'student' else 'teacher'
            if remember_me:
                st.session_state['remember_me'] = True
        else:
            st.error('Invalid credentials')
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def take_assessment():
    """Display assessment questions and handle user answers."""
    st.subheader('Take Assessment')
    
    if 'answers' not in st.session_state:
        st.session_state['answers'] = {}

    for i, q in enumerate(questions):
        st.write(f"*Q{i + 1}: {q['question']}*")
        answer = st.radio(f"Question {i + 1}", q['options'], key=f"question_{i}")
        st.session_state['answers'][i] = answer
    
    if st.button('Submit'):
        score = 0
        feedback = []

        for i, q in enumerate(questions):
            if st.session_state['answers'][i] == q['answer']:
                score += 1
                feedback.append(f"Question {i + 1}: Correct")
            else:
                feedback.append(f"Question {i + 1}: Incorrect. The correct answer is {q['answer']}")

        st.write(f"Your score is: {score}/{len(questions)}")
        st.write("Feedback:")
        for fb in feedback:
            st.write(fb)

def create_assessment():
    """Create and save new assessment questions."""
    st.subheader('Create New Assessment')
    
    if 'new_questions' not in st.session_state:
        st.session_state['new_questions'] = []
    
    with st.form(key='create_assessment_form'):
        question_text = st.text_input('Question')
        options_text = st.text_area('Options (comma separated)')
        correct_answer = st.text_input('Correct Answer')

        if st.form_submit_button('Add Question'):
            options = [option.strip() for option in options_text.split(',')]
            st.session_state['new_questions'].append({
                'question': question_text,
                'options': options,
                'answer': correct_answer
            })
            st.success('Question added!')
    
    if st.button('Save Assessment'):
        global questions
        questions = st.session_state['new_questions']
        save_questions(questions)
        st.success('Assessment saved successfully!')
        st.session_state['new_questions'] = []

def view_assessments():
    """Display existing assessments."""
    st.subheader('View Existing Assessments')
    
    global questions
    questions = load_questions()
    
    if not questions:
        st.write('No assessments available.')
    else:
        for i, q in enumerate(questions):
            st.write(f"*Q{i + 1}: {q['question']}*")
            st.write(f"Options: {', '.join(q['options'])}")
            st.write(f"Answer: {q['answer']}")
            st.write('---')

def main():
    """Main function to handle user interface and navigation."""
    st.title('Assessment Platform')

    inject_custom_css()

    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        login()
    else:
        if st.session_state['role'] == 'student':
            st.write('Welcome, Student!')
            take_assessment()
        elif st.session_state['role'] == 'teacher':
            st.write('Welcome To Teacher Dashboard')
            option = st.sidebar.selectbox('Choose an action', ['Create New Assessment', 'View Existing Assessments'])
            if option == 'Create New Assessment':
                create_assessment()
            elif option == 'View Existing Assessments':
                view_assessments()

if _name_ == "_main_":
    main()
