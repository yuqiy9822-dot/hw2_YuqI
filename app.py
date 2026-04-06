import os
import argparse
from pathlib import Path
from openai import OpenAI

DEFAULT_PROMPT = """
You are an AI assistant helping a business team convert messy meeting notes into a reliable first draft.

Output format:
## Summary
2-4 sentences.

## Action Items
- Task:
  Owner:
  Deadline:

## Risks / Blockers
- ...

## Human Review Needed
- Yes or No

Rules:
- Only include owners or deadlines if they are explicitly stated.
- If a note is ambiguous, preserve that ambiguity.
- Do not invent decisions, names, deadlines, or causes.
- If the notes contain uncertainty, conflict, or missing responsibility, set "Human Review Needed" to Yes.
- Keep the tone concise and professional.
""".strip()


def call_openai(notes, prompt, model):
    client = OpenAI()  # 官方推荐写法（自动读取环境变量）

    full_input = f"{prompt}\n\nMeeting notes:\n{notes}"

    response = client.responses.create(
        model=model,
        input=full_input
    )

    return response.output[0].content[0].text


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", default="gpt-5.4-mini")
    args = parser.parse_args()

    notes = Path(args.input).read_text()
    result = call_openai(notes, DEFAULT_PROMPT, args.model)

    Path(args.output).write_text(result)
    print(result)


if __name__ == "__main__":
    main()