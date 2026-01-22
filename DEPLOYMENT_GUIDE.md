# Deployment Guide

This guide will help you deploy your **Wine Cultivar Prediction** app to a cloud platform.

## Option 1: Render.com (Recommended for ease of use)

1.  **Push to GitHub**:
    - Create a new repository on GitHub (e.g., `wine-cultivar-prediction`).
    - Upload all files from `WineCultivar_Project_AyomideIbitola_23CG034077` to this repository.
    - Ensure `requirements.txt` is in the root of the repo.

2.  **Create Web Service on Render**:
    - Go to [dashboard.render.com](https://dashboard.render.com/).
    - Click **New +** -> **Web Service**.
    - Connect your GitHub account and select your new repository.

3.  **Configure Settings**:
    - **Name**: `wine-cultivar-app` (or similar).
    - **Runtime**: `Python 3`.
    - **Build Command**: `pip install -r requirements.txt`.
    - **Start Command**: `gunicorn app:app`.
        - *Note*: You may need to add `gunicorn` to your `requirements.txt` if it's not there. (I have added it for you below).

4.  **Deploy**:
    - Click **Create Web Service**.
    - Wait for the build to finish. Render will provide you with a URL (e.g., `https://wine-cultivar-app.onrender.com`).

5.  **Final Step**:
    - Copy the URL.
    - Paste it into `WineCultivar_hosted_webGUI_link.txt` in the "Live URL" field.

## Option 2: PythonAnywhere (Good alternative)

1.  **Sign Up**: Go to [pythonanywhere.com](https://www.pythonanywhere.com/) and create a beginner account.
2.  **Upload Files**:
    - Go to the **Files** tab.
    - Upload your project files (or use a Bash console to `git clone` your repo).
3.  **Virtual Env**:
    - Open a Bash console.
    - Run: `mkvirtualenv --python=/usr/bin/python3.9 myenv`.
    - Run: `pip install -r requirements.txt`.
4.  **Web App Setup**:
    - Go to the **Web** tab.
    - 'Add a new web app'.
    - Select **Flask** -> **Python 3.9**.
    - Path to flask app: `/home/yourusername/WineCultivar_Project_AyomideIbitola_23CG034077/app.py`.
5.  **Reload**:
    - Click **Reload** and visit your URL.

## Important Note regarding `gunicorn`
For deployment on Render, you need `gunicorn` in your `requirements.txt`.
Please add `gunicorn` to your `requirements.txt` if you choose Render.
