# Salary Prediction App

This project is a Streamlit-based web application that predicts employee salaries based on their years with the company and job rate using a pre-trained linear regression model.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)

## Overview

The **Salary Prediction App** allows users to estimate employee salaries by inputting the number of years at the company and the job rate. The app uses a pre-trained linear regression model (`linearmodel.pkl`) for predictions and provides an interactive experience.

## Installation

1. **Clone the repository:**
  ```bash
   git clone https://github.com/sianabipour/data-employees.git
   cd data-employees
```

2. **Create and activate a virtual environment (optional but recommended):**

  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

3. **Install the required packages:**
   
  ```bash
  pip install -r requirements.txt
  ```
4. **Ensure the model file (`linearmodel.pkl`) is in the same directory as `app.py`.** If it's missing, you can train a model using the analysis_modelling.ipynb notebook or provide your own serialized model.

## Usage
1. **Run the Streamlit application:**

  ```bash
  streamlit run app.py
  ```
2. **Interact with the app:**
- Enter the number of years with the company.
- Enter the job rate (e.g., a rating between 0.0 and 5.0).
- Click the "Press the button for salary prediction!" button.
- View the predicted salary displayed on the screen.

## Features
- User Input:

    - Accepts input for years with the company (integer).
    - Accepts input for job rate (float with step value).

- Prediction:
    - Uses a pre-trained linear regression model to estimate the salary.

## Project Structure
- `app.py`: The main Streamlit application script for the salary prediction app.
- `linearmodel.pkl`: The serialized linear regression model used for salary prediction.
- `requirements.txt`: List of required Python packages.
- `analysis_modelling.ipynb`: Jupyter Notebook for data analysis and training the regression model.
- `archive/`: Directory containing archived data or scripts.
