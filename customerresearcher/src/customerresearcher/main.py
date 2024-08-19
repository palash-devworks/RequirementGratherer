#!/usr/bin/env python
import sys
import argparse
from customerresearcher.crew import CustomerresearcherCrew

def get_topic():
    """
    Get the research topic from user input.
    """
    return input("Enter the research topic: ")

def run():
    """
    Run the crew and save the final requirements.
    """
    topic = get_topic()
    inputs = {
        'topic': topic
    }
    print(f"Starting research on: {topic}")
    crew = CustomerresearcherCrew().crew()
    result = crew.kickoff(inputs=inputs)
    
    # Assuming the last task's output is the final requirements
    final_requirements = result[-1].output
    
    # Save the final requirements to a file
    with open('requirements.md', 'w') as f:
        f.write(final_requirements)
    
    print(f"Final requirements for {topic} have been saved to requirements.md")

def train():
    """
    Train the crew for a given number of iterations.
    """
    topic = get_topic()
    inputs = {
        "topic": topic
    }
    try:
        n_iterations = int(input("Enter the number of training iterations: "))
        filename = input("Enter the filename to save training results: ")
        CustomerresearcherCrew().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        task_id = input("Enter the task ID to replay from: ")
        CustomerresearcherCrew().crew().replay(task_id=task_id)
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    topic = get_topic()
    inputs = {
        "topic": topic
    }
    try:
        n_iterations = int(input("Enter the number of test iterations: "))
        openai_model_name = input("Enter the OpenAI model name to use: ")
        CustomerresearcherCrew().crew().test(n_iterations=n_iterations, openai_model_name=openai_model_name, inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def main():
    parser = argparse.ArgumentParser(description="CustomerResearcher CLI")
    parser.add_argument('action', choices=['run', 'train', 'replay', 'test'], help='Action to perform')
    args = parser.parse_args()

    actions = {
        'run': run,
        'train': train,
        'replay': replay,
        'test': test
    }

    actions[args.action]()

if __name__ == "__main__":
    main()