from transformers import pipeline
import streamlit as st

# Optimization: Combine the get_pipeline and answer_and_score functions into one function for the number of calls.
def find_answer(question, context):
    if not context.strip() or not question.strip():
        raise ValueError("Both CONTEXT and QUESTION fields must be filled.")

    qa = pipeline('question-answering')
    result = qa(context=context, question=question)
    return result['answer'], result['score']


if __name__ == '__main__':
    try:
        st.title('ПОИСК В ТЕКСТЕ ОТВЕТА НА ВОПРОС')
        st.text('CONTEXT: текст, в котором будет осуществляться поиск ответа (англ).\n'
                'QUESTION: вопрос, на который будет осуществляться поиск ответа\n\t в тексте из поля CONTEXT (англ).')

        context = st.text_input('CONTEXT:', value='Moscow is capital of Russia.')
        question = st.text_input('QUESTION:', value='What is the capital of Russia?')

        if st.button('ИСКАТЬ ОТВЕТ'):
            answer, score = find_answer(question, context)
            st.text(f'ANSWER={answer}\nSCORE={score}')
    except ValueError as e:
        st.text(str(e))