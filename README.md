<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agent AI Email</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            line-height: 1.6;
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        h1, h2, h3 {
            border-bottom: 1px solid #ddd;
            padding-bottom: 5px;
            margin-top: 25px;
        }
        h1 { font-size: 2.2em; }
        h2 { font-size: 1.8em; }
        h3 { font-size: 1.4em; }
        code {
            font-family: "Courier New", Courier, monospace;
            background-color: #f4f4f4;
            padding: 2px 5px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        pre code {
            background-color: transparent;
            padding: 0;
        }
        blockquote {
            color: #666;
            margin: 0;
            padding-left: 15px;
            border-left: 4px solid #ddd;
        }
        ul, ol {
            padding-left: 30px;
        }
        li {
            margin-bottom: 5px;
        }
        a {
            color: #0366d6;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <h1><span role="img" aria-label="robot">🤖</span> Agent AI Email</h1>

    <blockquote>
        <p>A simple mini-agent that uses AI to send you a daily email.</p>
    </blockquote>

    <p>This project is a small AI agent that runs on a schedule (using <code>cron</code>) to send you a daily email.</p>

    <hr>

    <h2>1. Prerequisites: Install Cron</h2>

    <p>This agent uses <code>cron</code> to run the script on a daily schedule. If you are on a Debian-based system (like Ubuntu or Debian), you may need to install it first.</p>

    <pre><code class="language-bash">sudo apt-get update
sudo apt-get install cron</code></pre>

    <p>If you're new to <code>cron</code>, this guide is helpful: <a href="https://cronitor.io/guides/cron-jobs">Cron Job Tutorial</a></p>

    <hr>

    <h2>2. Project Setup</h2>

    <p>Follow these steps to set up your Python environment and install the required packages.</p>

    <h3>A. Create a Virtual Environment</h3>

    <p>It is highly recommended to use a Python virtual environment (<code>venv</code>) to keep your project dependencies isolated.</p>

    <ol>
        <li>Navigate to your project directory.</li>
        <li>Create the virtual environment (you can name it <code>venv</code> or anything you like):
<pre><code class="language-bash"># Use python3 if your system defaults to Python 2
python3 -m venv venv</code></pre>
        </li>
        <li>Activate the environment:
<pre><code class="language-bash"># On Linux/macOS
source venv/bin/activate

# On Windows
.\venv\Scripts\activate</code></pre>
        </li>
    </ol>

    <h3>B. Install Dependencies</h3>

    <p>With your virtual environment active, install the required packages:</p>

    <pre><code class="language-bash">pip install requests beautifulsoup4 google-generativeai python-dotenv htmldate</code></pre>

    <hr>

    <h2>3. Configuration: Add Your API Key</h2>

    <p>This agent uses the Google Gemini API. You'll need to provide an API key.</p>

    <ol>
        <li><strong>Get your key:</strong> You can generate a free API key from <a href="https://ai.google.dev/gemini-api/docs/api-key">Google AI Studio</a>.</li>
        <li><strong>Create a <code>.env</code> file:</strong> In the root of your project directory, create a file named <code>.env</code>.
<pre><code class="language-bash">touch .env</code></pre>
        </li>
        <li><strong>Add your key:</strong> Open the <code>.env</code> file and add the following line, replacing <code>YOUR_API_KEY_HERE</code> with your actual key:
<pre><code class="language-ini">GEMINI_API_KEY="YOUR_API_KEY_HERE"</code></pre>
        </li>
    </ol>

    <hr>

    <h2>4. Schedule the Daily Email</h2>

    <p>To make this agent run automatically, you need to add a new job to your <code>crontab</code>.</p>

    <ol>
        <li>Open your crontab editor:
<pre><code class="language-bash">crontab -e</code></pre>
        </li>
        <li>Add a new line to schedule the script. This example runs the script <strong>every day at 10:00 PM (22:00)</strong>.
<pre><code class="language-cron"># Run the AI email agent daily at 10:00 PM
0 22 * * * /full/path/to/your/project/venv/bin/python /full/path/to/your/project/main.py >> /home/YOUR_USERNAME/cron.log 2>&1</code></pre>
        </li>
    </ol>

    <p><strong>Important:</strong> You <strong>must</strong> replace the following placeholders:</p>
    <ul>
        <li><code>/full/path/to/your/project/venv/bin/python</code>: The <strong>absolute path</strong> to the Python executable <em>inside</em> your virtual environment.</li>
        <li><code>/full/path/to/your/project/main.py</code>: The <strong>absolute path</strong> to the main Python script.</li>
        <li><code>/home/YOUR_USERNAME/cron.log</code>: The path where you want to save the output logs (make sure <code>YOUR_USERNAME</code> is correct).</li>
    </ul>

    <p>Save and close the crontab file. Your agent is now scheduled to run!</p>

</body>
</html>
