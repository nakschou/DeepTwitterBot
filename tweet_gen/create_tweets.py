import openai
import numpy as np
import os
import logging
from config import get_openai_key

openai.api_key = get_openai_key()

# Change these
prompt = "Now give people back"
model = "ada:ft-personal-2023-01-03-03-07-23"
max_tokens = 50
n_generations = 25
file_path = "completions.txt"


def generate_completions(n, model, prompt, max_tokens):
    """
    Generates completions according to your parameters.
    ---
    Parameters:
        n: int
        model: str
        prompt: str
        max_tokens: int
    ---
    Returns: array of completions
    """
    arraycompletions = [
        openai.Completion.create(
            model=model, prompt=prompt, max_tokens=max_tokens, stop="END"
        )
        for i in np.arange(n)
    ]
    return arraycompletions


def write_completions(arr, file_path):
    """
    Writes the completions to a file.
    ---
    Parameters:
        arr: array of completions
        file_path: str
    ---
    Returns: None
    """
    with open(file_path, "w") as f:
        for i in arr:  # Writes to file
            f.write(str(i["choices"][0]["text"].encode("utf-8")) + "\n")
    return


completions = generate_completions(n_generations, model, prompt, max_tokens)
write_completions(completions, file_path)
