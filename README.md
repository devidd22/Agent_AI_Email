# 🤖 Agent AI Email

> A simple mini-agent that uses AI to send you a daily email.

This project is a small AI agent that runs on a schedule (using `cron`) to send you a daily email.

---

## 1. Prerequisites: Install Cron

This agent uses `cron` to run the script on a daily schedule. If you are on a Debian-based system (like Ubuntu or Debian), you may need to install it first.

```bash
sudo apt-get update
sudo apt-get install cron
```
---

## 2. Project Setup

Follow these steps to set up your Python environment and install the required packages.

### A. Create a Virtual Environment

It is highly recommended to use a Python virtual environment (`venv`) to keep your project dependencies isolated.

1.  Navigate to your project directory.
2.  Create the virtual environment (you can name it `venv` or anything you like):

    ```bash
    # Use python3 if your system defaults to Python 2
    python3 -m venv venv
    ```

3.  Activate the environment:

    ```bash
    # On Linux/macOS
    source venv/bin/activate
    
    # On Windows
    .\venv\Scripts\activate
    ```

### B. Install Dependencies

With your virtual environment active, install the required packages:

```bash
pip install requests beautifulsoup4 google-generativeai python-dotenv htmldate
```
### 3.Configuration:Add your API key

This agent uses a Google Gemini API.You will need to provide an API key

1. **Get your key:** You can generate a free API key from <a href="https://ai.google.dev/gemini-api/docs/api-key">Google AI Studio"</a>
2.  **Create a `.env` file:** In the root of your project directory, create a file named `.env`.

    ```bash
    touch .env
    ```

3.  **Add your key:** Open the `.env` file and add the following line, replacing `YOUR_API_KEY_HERE` with your actual key:

    ```ini
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```
