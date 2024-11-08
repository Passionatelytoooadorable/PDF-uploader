from langchain.text_splitter import SimpleTextSplitter
from langchain.qa_pipeline import QAPipeline

# Initialize a LangChain Q&A pipeline
qa_pipeline = QAPipeline()

def answer_question(text_content: str, question: str) -> str:
    splitter = SimpleTextSplitter()
    documents = splitter.split_text(text_content)
    response = qa_pipeline.run(documents=documents, query=question)
    return response
