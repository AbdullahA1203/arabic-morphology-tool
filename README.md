# arabic-morphology-tool

A Python tool for generating word-form flashcards from Arabic nouns and verbs to support language learning.

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [License](#license)

## Background

Arabic morphology is built around manipulating root letters to form a wide range of verb and noun forms. This is powerful, however it can be challenging for learners to recognize how a given word relates to its root letters, base forms and underlying patterns, especially when encountering derived forms in real texts. Furthermore searching for the base forms given a word can become time consuming. This tool is designed to take an Arabic verb or noun and generate its core morphological forms as concise flashcards, helping learners to internalize the relation between surface forms and their base patterns. The aim of this tool is to support vocabulary building, pattern recognition and effective review for flashcard-based study workflows.

## Install

### Prerequisites

- Python 3.9+
- pip
- git

### 1. Clone the repository:

```
git clone https://github.com/AbdullahA1203/arabic-morphology-tool.git
cd arabic-morphology-tool
```

### 2. Create and activate a virtual environment (optional):

```
python -m venv venv
source venv/bin/activate
```

### 3. Install the project (editable mode):

```
pip install -e .
```
This installs:
- All required dependencies
- The CLI command
- The project in development mode

### 4. Set up environment variables:

Create a .env file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```
Do not commit this file — it should be in .gitignore.

### 5. Run the tool 

```
arabic-morphology --help
```

## Usage

Show help: 

```
arabic-morphology --help
```

Generate a verb flashcard:

```
arabic-morphology generate كتب --type verb
```

Generate a noun flashcard:

```
arabic-morphology generate كتاب --type noun
```

## License

[MIT © Abdullah Ahmad.](LICENSE)