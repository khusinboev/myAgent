import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI

load_dotenv()


def summarize_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # Barcha sahifalarni birlashtir
    text = "\n\n".join([doc.page_content for doc in docs])

    # Summarize qil
    prompt = f"Summarize the following document:\n\n{text}"
    summary = llm.invoke(prompt)

    return summary.content


if __name__ == '__main__':
    summary = summarize_pdf('mymini.pdf')
    print('Summary:')
    print(summary)