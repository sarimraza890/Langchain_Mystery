from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

PROMPT = PromptTemplate(
    input_variables=["text"],
    template="""
Extract important factual information from the following document text.

TEXT:
{text}

Return concise bullet points.
"""
)

def load_docs(pdf_path):
    loader = PyPDFLoader(pdf_path)
    return loader.load()

def extract_fact(doc):
    chain = PROMPT | llm
    return chain.invoke({"text": doc.page_content})

def merge_facts(facts):
    return "\n".join([str(f) for f in facts])
