# Debate Simulator

[繁體中文](README_TW.md) | English

This project uses two language models to debate on the same topic. Each model represents either the affirmative or the negative side, and they will read each other's testimonies and make rebuttals to simulate a debate. A third model acts as the judge, reading the arguments from both sides and scoring them individually.

The core concept of this project is to simulate a generative [Adversarial Neural Network (GAN)](https://en.wikipedia.org/wiki/Generative_adversarial_network), but the models themselves are not fine-tuned based on the scores, thus it serves only as a principle simulation.

## Running Guide

This project is based on the Python programming language and uses the external library openai. It is recommended to use [Anaconda](https://www.anaconda.com) to configure the Python environment. The following setup procedures have been tested on Windows 11. Here are the commands for the console/terminal/shell.

### Environment Setup

```bash
# Create a conda environment named debate with Python version 3.11.5
conda create -n debate python=3.11.5
conda activate debate
```

```bash
# Install external libraries
cd [path to project folder]
pip install -r requirements.txt
```

### Running the Test

This project requires OpenAI API keys, which can be obtained from the [OpenAI website](https://platform.openai.com/api-keys) (paid service). Copy the generated keys into `api_keys.py`.

After setting up the environment, you can run `main.py` in the `debate/` folder.

```bash
cd debate
python main.py
```

### Viewing Debate Records

The project will automatically generate a text file in the project folder named `record.txt`. Open it to view the debate records and judge's scoring results.
