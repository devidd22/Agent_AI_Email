# 🤖 Agent AI Email

> A simple mini-agent that uses AI to send you a daily email.

This project is a small AI agent that runs on a schedule (using `cron`) to send you a daily email.

---

## 1. Prerequisites: Install Cron

This agent uses `cron` to run the script on a daily schedule. If you are on a Debian-based system (like Ubuntu or Debian), you may need to install it first.

```bash
sudo apt-get update
sudo apt-get install cron
