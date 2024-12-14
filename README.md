# End-to-End Text Summarization Project

This repository provides a complete, end-to-end text summarization pipeline, from data ingestion and validation to data transformation and model-based text summarization. It includes a backend pipeline orchestrated by `main.py` and a user-friendly web application built with [Streamlit](https://streamlit.io/) that allows users to interactively summarize text using a pre-trained Hugging Face model.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Running the Pipeline](#running-the-pipeline)
- [Running the Web App](#running-the-web-app)
- [Model & Summarization Logic](#model--summarization-logic)
- [Configuration Files](#configuration-files)
- [Research Notebooks](#research-notebooks)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project aims to automate the process of transforming raw text data into concise summaries. It handles every stage of the pipeline:

1. **Data Ingestion:** Download or load raw text data.  
2. **Data Validation:** Ensure data quality and format consistency.  
3. **Data Transformation:** Clean, preprocess, and prepare data for summarization.  
4. **Summarization App:** Interactively summarize text using a web interface powered by a Hugging Face transformer model.

By the end of this pipeline, you will have a working application that takes user input and provides a meaningful summary of the text.

## Features

- **Automated Pipeline:** `main.py` orchestrates the entire process (ingestion, validation, transformation).
- **Configurable Workflow:** Easily modify parameters through YAML config files (`config/` and `params.yaml`).
- **Hugging Face Integration:** Leverage state-of-the-art models (like `facebook/bart-large-cnn`) for high-quality summaries.
- **User-Friendly Web Interface:** A Streamlit-based interface allows users to input text and instantly get a summary.
- **Modular Codebase:** Clearly separated modules for components, configuration, pipeline stages, and utilities.

## Project Structure

```bash
end-to-end-text-summarization/
│
├─ .github/workflows/       # CI/CD workflows (if applicable)
├─ config/                  # Configuration files for pipeline and model settings
├─ research/                # Jupyter notebooks for exploration and experimentation
├─ src/textSummarizer/      # Source code for the summarization pipeline
│  ├─ components/           # Data ingestion, validation, transformation scripts
│  ├─ config/               # Configuration manager
│  ├─ constants/            # Constant values and paths
│  ├─ entity/               # Entity classes for structured data
│  ├─ logging/              # Custom logging setup
│  ├─ pipeline/             # Pipeline stages (data_ingestion, validation, transformation)
│  └─ utils/                # Common utility functions
│
├─ app.py                   # Streamlit web application
├─ main.py                  # Orchestration script for the entire pipeline
├─ params.yaml              # High-level parameters for the pipeline
├─ requirements.txt         # Python dependencies
├─ setup.py                 # Setup script for installing the package
├─ Dockerfile               # Docker configuration (if needed)
├─ template.py              # Template script (if any)
└─ README.md                # This README file
```

## Setup & Installation

### Prerequisites
- Python 3.7+ (Recommended: Python 3.11)
- pip (Python package installer)
- Internet connection (for downloading data/models)

### Steps

**Clone the Repository:**
```
git clone https://github.com/<your-username>/end-to-end-text-summarization.git
cd end-to-end-text-summarization
```

### Create and Activate a Virtual Environment:

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies:
```
pip install --upgrade pip
pip install -r requirements.txt
```

### (Optional) Install Editable Mode:
```
pip install -e .
```
This allows you to import textSummarizer modules easily.

## Running the Pipeline
The pipeline is orchestrated by main.py. Running it will execute:

- Data ingestion
- Data validation
- Data transformation

```
python main.py
```
You will see log messages indicating the progress of each stage. After completion, preprocessed data and artifacts (like artifacts/data_ingestion, artifacts/data_validation, artifacts/data_transformation) will be available in the artifacts directory.

## Running the Web App
Once the pipeline completes and your environment is set up, you can run the Streamlit app to summarize text interactively:

```
streamlit run app.py
```

A local URL (e.g., http://localhost:8501) will appear in your terminal. Open it in your browser and you’ll see:

A text area to enter or paste text.
A "Summarize" button.
The generated summary displayed below once the button is clicked.

## Model & Summarization Logic

Currently, the summarization logic is implemented via a Hugging Face pipeline with a pre-trained model (e.g., `facebook/bart-large-cnn`). You can customize this by:

- Changing the model name in `app.py` where the pipeline is loaded.
- Adjusting `max_length`, `min_length`, or other hyperparameters.
- Integrating a custom fine-tuned model if you have one.

---

## Configuration Files

- `params.yaml`: High-level parameters for data processing and model configuration.
- `config/config.yaml`: Specifies paths, parameters for different pipeline stages, and other runtime settings.

You can tailor these YAML files to your data sources, model paths, and preferred parameters.

---

## Research Notebooks

The `research` folder contains Jupyter notebooks that detail the experimentation and development process:

- `01_data_ingestion.ipynb`: Data loading and exploration.
- `02_data_validation.ipynb`: Data quality checks and validation logic.
- `03_data_transformation.ipynb`: Data cleaning and preprocessing steps.
- `Text_Summarizer_project.ipynb`: Overall summarization project notebook (if any).
- `trials.ipynb`: Any experimental trials or prototyping.

These notebooks help you understand how the pipeline stages were developed and tested. They’re not required to run the main pipeline but serve as valuable documentation and reference.

---

## Future Improvements

- **Model Fine-Tuning:** Integrate a custom fine-tuned summarization model for domain-specific text.
- **Scaling & Deployment:** Containerize the app with Docker and deploy to a platform like AWS, GCP, or Heroku.
- **Continuous Integration:** Integrate GitHub Actions to run tests and lint checks on every commit.
- **Advanced UI:** Enhance the Streamlit interface with additional options (e.g., parameter sliders for summary length, multiple summary methods).

---

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or improvements, please open an issue or submit a pull request.

**Steps to Contribute:**
1. Fork this repository.
2. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit and push your changes, then open a pull request.
We will review contributions and merge them after ensuring code quality and compatibility.

## License
This project is distributed under the MIT License. Feel free to use, modify, and distribute this code as allowed by the license.
