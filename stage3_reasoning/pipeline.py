from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from prompts import (
    TIMELINE_PROMPT,
    CONTRADICTION_PROMPT,
    FINAL_REASONING_PROMPT
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

timeline_prompt = PromptTemplate(
    input_variables=["facts"],
    template=TIMELINE_PROMPT
)

contradiction_prompt = PromptTemplate(
    input_variables=["timeline"],
    template=CONTRADICTION_PROMPT
)

final_prompt = PromptTemplate(
    input_variables=["timeline", "contradictions"],
    template=FINAL_REASONING_PROMPT
)

timeline_chain = timeline_prompt | llm
contradiction_chain = contradiction_prompt | llm
final_chain = final_prompt | llm


def reason(facts: str):
    timeline = timeline_chain.invoke({"facts": facts}).content

    contradictions = contradiction_chain.invoke(
        {"timeline": timeline}
    ).content

    final_answer = final_chain.invoke({
        "timeline": timeline,
        "contradictions": contradictions
    }).content

    return {
        "timeline": timeline,
        "contradictions": contradictions,
        "final_reasoning": final_answer
    }
