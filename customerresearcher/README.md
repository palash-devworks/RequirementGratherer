# CustomerResearcher Crew

Welcome to the CustomerResearcher Crew project, powered by [crewAI](https://crewai.com). This project is designed to conduct comprehensive research on a given topic and generate detailed requirements for further market research and tool evaluation.

## Project Overview

The CustomerResearcher Crew is a multi-agent AI system that collaborates on complex research tasks. It's designed to:

1. Conduct in-depth research on a specified topic
2. Analyze trends and emerging technologies
3. Compile comprehensive research requirements
4. Generate market research criteria for tool evaluation

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management.

1. Install Poetry:
```bash
pip install poetry
```

2. Install project dependencies:
```bash
poetry lock
poetry install
```

## Configuration

## Configuration

1. Add your keys
   - `OPENAI_API_KEY` to the `.env` file in the `customerresearcher` directory.
   - `OPENAI_ORGANIZATION_ID` to the `.env` file in the `customerresearcher` directory.
   - `SERPER_API_KEY` to the `.env` file in the `customerresearcher` directory.
   - `AGENTOPS_API_KEY` to the `.env` file in the `customerresearcher` directory.

2. Customize the project:
   - Modify `src/customerresearcher/config/agents.yaml` to define your agents
   - Modify `src/customerresearcher/config/tasks.yaml` to define your tasks
   - Adjust `src/customerresearcher/crew.py` to add your own logic, tools, and specific arguments
   - Update `src/customerresearcher/main.py` to add custom inputs for your agents and tasks

## Running the Project

To start the research process:

```bash
poetry run customerresearcher
```

This command will:
1. Prompt you for a research topic
2. Initialize the CustomerResearcher Crew
3. Execute a series of research tasks
4. Generate two output files:
   - `requirements.md`: Detailed research requirements
   - `market_research_requirements.md`: Criteria for tool evaluation

## Understanding the Workflow

The CustomerResearcher Crew follows these main steps:
1. Initial consultation
2. Literature review and web research
3. Data collection and analysis
4. Expert interviews and trend analysis
5. Ethical assessment and methodology design
6. Preliminary findings compilation
7. Quality assessment
8. Final requirements compilation
9. Market research requirements generation

Each step is handled by specialized AI agents with unique roles and capabilities.

Let's revolutionize research with the power of AI collaboration!
