import os

import openai
import typer
from rich import print
from rich.console import Console
from rich.markdown import Markdown

from chams.utils import generate_temperatures, get_random_color

# Set the GPT-3 API key
try:
    # Set the GPT-3 API key
    openai.api_key = os.environ["OPENAI_API_KEY"]
except KeyError:
    print("API_KEY environment variable not set. Please set this variable and try again.")

app = typer.Typer()


def communicate_with_gpt_3(number: int, prompt: str, task: str, model="text-davinci-003"):
    """Communicate with GPT-3 using the OpenAI API"""
    temperatures = generate_temperatures(number, 0, 1)
    console = Console()
    for i in range(number):
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperatures[i % len(temperatures)],
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        markdown_template = f"# {task} - {i}"
        iteration_color = get_random_color(i)
        md = Markdown(markdown_template)
        console.print(md, style=iteration_color)
        console.print(response["choices"][0]["text"], style=iteration_color)
        console.print()
        console.print()


# Define the function that will be called when the CLI is run
@app.command()
def email(subject: str = typer.Argument(..., help="The subject of the email"),
          language: str = typer.Option("fr", help="The language to use for the prompt."),
          number: int = typer.Option(1, "-n", help="The number of emails to generate.")):
    # Use GPT-3 to generate text based on the provided prompt
    languages = {
        "fr": "créer un email en français pour dire:",
        "en": "create an email in English to say:",
    }

    prompt = f"in {languages[language]} {subject}"

    communicate_with_gpt_3(number, prompt, "email")


@app.command()
def paraphrase(text: str = typer.Argument(..., help="The text to paraphrase."),
               language: str = typer.Option("fr", help="The language to use for the prompt."),
               number: int = typer.Option(1, "-n", help="The number of text to generate.")):
    # Use GPT-3 to generate text based on the provided prompt
    languages = {
        "fr": "paraphraser ce texte en français:",
        "en": "paraphrase this text in english:"
    }

    prompt = f"{languages[language]} {text}"

    communicate_with_gpt_3(number, prompt, "paraphrase")


# Use Typer to create the CLI
if __name__ == "__main__":
    app()
