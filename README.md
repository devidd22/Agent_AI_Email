# 🤖 Agent AI Email

> A simple mini-agent that uses AI to send you a daily email about the news in AI.

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
---

## 4. Schedule the Daily Email

To make this agent run automatically, you need to add a new job to your `crontab`.

1.  Open your crontab editor:

    ```bash
    crontab -e
    ```

2.  Add a new line to schedule the script. This example runs the script **every day at 10:00 PM (22:00)**.

    ```cron
    # Run the AI email agent daily at 10:00 PM
    0 22 * * * /full/path/to/your/project/venv/bin/python /full/path/to/your/project/main.py >> /home/YOUR_USERNAME/cron.log 2>&1
    ```

**Important:** You **must** replace the following placeholders:

* `/full/path/to/your/project/venv/bin/python`: The **absolute path** to the Python executable *inside* your virtual environment.
* `/full/path/to/your/project/main.py`: The **absolute path** to the main Python script.
* `/home/YOUR_USERNAME/cron.log`: The path where you want to save the output logs (make sure `YOUR_USERNAME` is correct).

Save and close the crontab file. Your agent is now scheduled to run!

### 4.Configuration: Change in `main.py` 
