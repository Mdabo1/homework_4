import streamlit as st
from transformers import pipeline

# Load the question-answering pipeline
distilled_student_sentiment_classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    return_all_scores=True,
)


# Streamlit app
def main():
    st.title("Про-классифицируй текст")

    # User input
    question = st.text_input("Введите текст:")

    if st.button("Получить оценку"):
        # Process the question with the static context
        answer = distilled_student_sentiment_classifier(question)

        # Display the answer
        st.subheader("Оценка")
        st.write(answer)


if __name__ == "__main__":
    main()
