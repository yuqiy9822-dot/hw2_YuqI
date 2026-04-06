# Report

## Business Use Case
This prototype converts raw meeting notes into structured summaries and action items.

## Model Choice
I used the OpenAI API with the Python SDK to make real LLM calls.

## Prompt Iteration
The initial prompt was simple and caused overconfident outputs. Later versions added rules to avoid hallucination and introduced structured output.

## Limitations
The model struggles when notes are ambiguous or incomplete.

## Recommendation
This workflow should be used as a first draft tool with human review.
