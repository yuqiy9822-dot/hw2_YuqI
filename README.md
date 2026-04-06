# Week 2: Build and Evaluate a Simple GenAI Workflow

## Project Overview
This project builds a simple GenAI workflow for converting raw meeting notes into a structured business summary. The prototype helps a project manager or team lead quickly identify key decisions, action items, owners, deadlines, and risks from messy notes.

## Chosen Workflow
The workflow I chose is summarizing meeting notes into action items and a short status update.

## Intended User
The intended user is a project manager, operations lead, or team member who needs a fast first draft after a meeting.

## Input
The system receives raw meeting notes, which may include:
- incomplete sentences
- bullet points
- informal language
- missing owners or deadlines
- side discussions

## Output
The system should produce:
- a short summary
- action items
- owners if mentioned
- deadlines if mentioned
- blockers or risks
- a human review flag when the notes are ambiguous

## Why This Task Is Valuable
This task is valuable because teams often spend time manually cleaning meeting notes and extracting next steps. A GenAI first draft can save time, improve consistency, and help teams act faster, while still keeping a human in the loop.

## Repository Files
- `app.py` - command-line Python prototype
- `prompts.md` - prompt iteration log
- `eval_set.json` - evaluation cases
- `report.md` - short report
- `sample_notes.txt` - sample input for demo

## API / Model
This project uses the OpenAI API. The Python app makes a real LLM API call using an API key stored in the `OPENAI_API_KEY` environment variable.

## How to Run
1. Install dependencies:
   ```bash
   pip install openai
