FACT_EXTRACTION_PROMPT = """
You are an expert investigator.

Read the following story text carefully and extract ONLY verifiable facts.

Rules:
- Do not guess or infer
- Do not solve the mystery
- Keep facts short and precise
- Use bullet points

Text:
{context}
"""


TIMELINE_PROMPT = """
Task: Construct a STRICT chronological timeline.

Rules:
- Output ONLY ordered events
- Each event must be a single observable action or state
- NO explanations
- NO cause-and-effect language
- NO speculation
- NO inferred intent
- NO adjectives

Format:
1. Event
2. Event
3. Event

Facts:
{facts}

"""


CONTRADICTION_PROMPT = """
You are a forensic logic auditor.

Given the timeline below, identify:
- Logical impossibilities
- Conflicting statements
- Missing causal links
- Events that cannot all be true at once

Rules:
- Each bullet must reference specific timeline events
- Do NOT restate the timeline
- Do NOT speculate beyond the timeline

Timeline:
{timeline}

Return only bullet points.

"""


FINAL_REASONING_PROMPT = """
You are a forensic reasoning engine.

Inputs:
Timeline:
{timeline}

Contradictions:
{contradictions}

Rules:
- State conclusions decisively
- No modal verbs (may, might, possibly)
- No investigative theory
- No generic explanations
- Reference specific timeline items as evidence

Output format:

WHO:
HOW:
WHY:

If motive is indirect, state the inference explicitly.

"""
