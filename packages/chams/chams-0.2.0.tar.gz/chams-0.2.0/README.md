# chams - NLP Tasks with OpenAI GPT-3

Welcome to chams, a Python package for natural language processing (NLP) tasks such as paraphrasing and email generation using OpenAI's GPT-3 model.

## Installation

you can install chams by running the following command:

```bash
pip install chams
```

## Usage
To use chams, you will need to set the OPENAI_API_KEY environment variable to your OpenAI API key.

You can then use the following command to generate emails with chams:

```bash
chams email "send login for the database to infrastructure team" --language "en" -n 3
```

This will generate 3 emails with the subject "send login for the database to infrastructure team" in English.

You can also use the paraphrase command to generate paraphrased text. For example:
    
```bash
chams paraphrase --text "Hello, how are you doing?" --language "en" --number 2
```
This will generate 2 paraphrased versions of the text "Hello, how are you doing?" in English.

## Author
chams was created by Zakaria Fellah. You can reach him at [fellah.zakaria@yahoo.com](mailto:fellah.zakaria@yahoo.com)

## License
chams is released under the MIT license.