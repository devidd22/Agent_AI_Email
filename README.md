<h1>Agent_AI_Email</h1>
<div class="top">
   <h2 style="text-align: center;">
     An easy mini-agent for every day use
   </h2> 
   <h3>This is a mini AI-Agent which is sending an email every day.It is simpel to use, u just need to follow some steps:</h3>
   <h4> If you use a Debian based system (Debian, Ubuntu), try the following commands first:
         sudo apt-get update
         sudo apt-get install cron
         Now u have installed cron and u can set when u want to send u the email
         Follow this link to understand how cron works:
         <a href="https://cronitor.io/guides/cron-jobs">Cron Tutorial</a>
   </h4>
   <h4>
      Now I encourage you to use a ProjectVenv with this command:
      python -m venv /path/to/new/virtual/environment (you choose ur path) ~ maybe u use python3 so u can switch python with python3(depends)
      Now i will give you what u need to install for this script to work:
      pip install requests
      pip install beautifulsoup4
      pip install google-generativeai
      pip install python-dotenv
      pip install htmldate
      You will need to use this in cronjob
      exp:
      0 22 * * * cd /path/to/where/git_clone && /path/to/new/virtual/environment main.py >> /home/(your_pc_name)/cron.log 2>&1
   </h4>
   <h4>
      Now u need to create a file named ".env" in this directory
      touch ".env" <- to create the file
      Here u need to add your gemini api key
      Here is the link to make one:
         <a href="https://ai.google.dev/gemini-api/docs/api-key">Gemini API KEY"</a>
      GEMINI_API_KEY="YOUR_API_KEY"
      
   </h4>
</div>
