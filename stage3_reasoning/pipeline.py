from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

PROMPT = PromptTemplate(
    input_variables=["transcript", "facts"],
    template="""
You are a reasoning engine.

Audio Transcript:
{transcript}

Extracted Facts:
{facts}

Using ONLY the above information, provide a clear and logical conclusion.
"""
)

def reason(transcript, facts):
    chain = PROMPT | llm
    return chain.invoke({
        "transcript": transcript,
        "facts": facts
    })
