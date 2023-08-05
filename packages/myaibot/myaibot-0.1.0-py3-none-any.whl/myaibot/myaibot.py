"""
This module contains the implementation of a chatbot that uses the 
OpenAI GPT-3 model to generate responses to user input.
@author: Hamid Ali Syed
@email: hamidsyed37@gmail.com
"""

import os
import argparse
import logging
import openai

# Set your API key for OpenAI
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set the model to use (in this case, the GPT-3 model)

MODEL_ENGINE = "text-davinci-002"

def generate_response(input_text: str) -> str:
    """
    Generates a response to a user's input using the OpenAI GPT-3 model.

    Parameters:
    input_text (str): The input text to generate a response for.

    Returns:
    str: The generated response.
    """
    if openai.api_key is None:
        raise ValueError("OpenAI API key is not set")
    # Use the GPT-3 model to generate a response to the input text
    response = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=input_text,
        max_tokens=1024,
        n=1,
        temperature=0.5
    ).choices[0].text

    # Return the generated response
    return response

def myaibot(input_text: str) -> None:
    """
    Runs the myaibot using the user-provided input text.

    Parameters:
    input_text (str): The input text to generate a response for.
    """
    # Generate a response to the user's input
    response = generate_response(input_text)

    # Print the user's input and the generated response
    print(f"User input: {input_text}")
    print(f"myaibot response: {response}")

def main() -> None:
    """
    The main entry point for the myaibot package.
    """
    # Use argparse to parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input string to pass to the myaibot')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug output')
    args = parser.parse_args()

    # Set the logging level to DEBUG if the --debug flag is set
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    # Run the myaibot with the user-provided input
    try:
        myaibot(args.input)
    except ValueError as error:
        # Catch any exceptions that occur and print an error message
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
    