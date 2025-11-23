import streamlit as st

st.set_page_config(
    page_title="Asistent Juridic AI",
    page_icon="⚖️",
    layout="centered"
)

st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
    }
    .question-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        color: #000000 !important;
    }
    .question-box * {
        color: #000000 !important;
    }
    .answer-section {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
        color: #000000 !important;
    }
    .answer-section * {
        color: #000000 !important;
    }
    .hint-section {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        color: #000000 !important;
    }
    .hint-section * {
        color: #000000 !important;
    }
    .explanation-section {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        color: #000000 !important;
    }
    .explanation-section * {
        color: #000000 !important;
    }
    .final-answer-section {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        color: #000000 !important;
    }
    .final-answer-section * {
        color: #000000 !important;
    }
    .abstention-section {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        color: #000000 !important;
    }
    .abstention-section * {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"><h1>⚖️ Asistent Juridic AI</h1></div>', unsafe_allow_html=True)
st.markdown("*Pune o întrebare și primește un răspuns concis, orientat pe regula care se aplică.*")

st.divider()

if 'history' not in st.session_state:
    st.session_state.history = []

with st.form(key='question_form', clear_on_submit=True):
    question = st.text_area(
        "Întrebarea ta:",
        placeholder="Exemplu: Ce prevede art. 969 din Codul Civil?",
        height=100,
        key="question_input"
    )
    submit_button = st.form_submit_button("Trimite întrebarea", use_container_width=True)

if submit_button and question.strip():
    with st.spinner("Procesez întrebarea..."):
        response = {
            "question": question,
            "status": "success",
            "hint": "Orientare: Caută în legislația relevantă...",
            "explanation": "Test answered successfully",
            "final_answer": "Răspunsul complet ar include referințe precise la articolele de lege aplicabile."
        }

        st.session_state.history.insert(0, response)

if st.session_state.history:
    st.markdown("### Răspunsuri")

    for idx, item in enumerate(st.session_state.history):
        with st.container():
            st.markdown(f'<div class="question-box"><strong>Întrebare:</strong> {item["question"]}</div>', unsafe_allow_html=True)

            if item["status"] == "success":
                st.markdown(f'<div class="hint-section"><strong>💡 Hint:</strong><br>{item["hint"]}</div>', unsafe_allow_html=True)

                st.markdown(f'<div class="explanation-section"><strong>📖 Explicație:</strong><br>{item["explanation"]}</div>', unsafe_allow_html=True)

                st.markdown(f'<div class="final-answer-section"><strong>✅ Răspuns final:</strong><br>{item["final_answer"]}</div>', unsafe_allow_html=True)

            elif item["status"] == "abstention":
                st.markdown(f'<div class="abstention-section"><strong>⚠️ Abținere:</strong><br>{item["message"]}</div>', unsafe_allow_html=True)

            else:
                st.error(f"Eroare: {item.get('message', 'A apărut o eroare necunoscută.')}")

            st.divider()

if st.session_state.history:
    if st.button("Șterge istoricul", type="secondary"):
        st.session_state.history = []
        st.rerun()
