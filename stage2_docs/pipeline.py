from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from prompts import FACT_EXTRACTION_PROMPT

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# PROMPT = PromptTemplate(
#     input_variables=["text"],
#     template="""
# Extract important factual information from the following document text.

# TEXT:
# {text}

# Return concise bullet points.
# """
# )

def load_docs(pdf_path):
    loader = PyPDFLoader(pdf_path)
    return loader.load()

def extract_fact(doc):
    prompt = PromptTemplate(
        template=FACT_EXTRACTION_PROMPT,
        input_variables=["context"]
    )

    chain = prompt | llm
    return chain.invoke({"context": doc.page_content})

def merge_facts(facts):
    return "\n".join([str(f) for f in facts])
