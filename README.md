# Clothing Brand Name Generator

## Overview

This web application generates creative clothing brand names and related keywords/categories based on the clothing style you select. It is built using Python, Langchain, and Streamlit.

## Features

* **Clothing Brand Name Generation**: Suggests catchy and creative names for your clothing brand.
* **Keywords/Categories Generation**: Provides related keywords or product categories for the generated brand name (e.g., "T-shirts, Dresses, Jeans").
* **Clothing Style Selection**: Choose from a variety of clothing styles using a user-friendly dropdown menu in the sidebar.

## Technologies Used

* Python
* Langchain
* OpenAI API
* Streamlit

## Prerequisites

* Python 3.6 or later
* OpenAI API key

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    cd clothing-brand-name-generator
    ```
2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
3.  **Set up your API key:**

    * Create a file named `secret_key.py` in the same directory as `langchain_helper.py`.
    * Add your OpenAI API key to `secret_key.py`:

        ```python
        openapi_key = "YOUR_OPENAI_API_KEY"
        ```
    * Replace `"YOUR_OPENAI_API_KEY"` with your actual OpenAI API key.

## How to Run

1.  **Run the Streamlit app:**

    ```bash
    streamlit run main.py
    ```
2.  Open your browser to the displayed URL (usually `http://localhost:8501`).
3.  Select a clothing style from the dropdown menu, and the app will generate a brand name and related keywords/categories.


