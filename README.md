<p align="center">
  <pre>
████████╗██╗██╗  ██╗    ██╗   ██╗██╗  ██╗
╚══██╔══╝██║██║ ██╔╝    ██║   ██║██║ ██╔╝
   ██║   ██║█████╔╝     ██║   ██║█████╔╝ 
   ██║   ██║██╔═██╗     ╚██╗ ██╔╝██╔═██╗ 
   ██║   ██║██║  ██╗     ╚████╔╝ ██║  ██╗
   ╚═╝   ╚═╝╚═╝  ╚═╝      ╚═══╝  ╚═╝  ╚═╝
  </pre>
</p>

<h1 align="center">🎯 TikVK Email Checker<br><sub>Bulk TikTok &amp; VK (Mail.ru) Account Validator</sub></h1>

<p align="center">
  <strong>Multi‑threaded script that checks whether emails are registered on TikTok and VK, then reports via Telegram.</strong><br>
  <em>Educational project – understand API interaction and threading concepts.</em>
</p>

<p align="center">
  <a href="https://github.com/Ali-Haidar-Sy/TikTok-VK-Email-Checker/stargazers"><img src="https://img.shields.io/github/stars/Ali-Haidar-Sy/TikTok-VK-Email-Checker?style=for-the-badge&color=yellow"></a>
  <a href="https://github.com/Ali-Haidar-Sy/TikTok-VK-Email-Checker/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Ali-Haidar-Sy/TikTok-VK-Email-Checker?style=for-the-badge&color=blue"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white"></a>
  <a href="https://t.me/P33_9"><img src="https://img.shields.io/badge/Telegram-@P33_9-2CA5E0?style=for-the-badge&logo=telegram"></a>
  <a href="https://www.instagram.com/_ungn"><img src="https://img.shields.io/badge/Instagram-@_ungn-E4405F?style=for-the-badge&logo=instagram"></a>
  <a href="https://github.com/Ali-Haidar-Sy"><img src="https://img.shields.io/badge/GitHub-Ali--Haidar--Sy-181717?style=for-the-badge&logo=github"></a>
</p>

---

## 🔍 What is TikVK Email Checker?

**TikVK** is a Python script that:

*   Generates random email addresses based on TikTok search suggestions.
*   Checks each email against **TikTok’s API** to see if it is already linked to an account.
*   Checks each email against **VK’s (Mail.ru) API** to determine if the mailbox exists.
*   Retrieves additional **TikTok user info** (followers, likes, country, etc.) for valid emails.
*   Sends all results **instantly to a Telegram bot** of your choice.

The tool is **massively multi‑threaded** – 15 parallel threads running TikTok searches simultaneously.

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Ali-Haidar-Sy/TikTok-VK-Email-Checker.git
cd TikTok-VK-Email-Checker

# 2. Install required external modules
pip install telebot user_agent requests beautifulsoup4

# 3. (IMPORTANT) You need two local modules:
#    - SignerPy.py   (TikTok signature generator)
#    - ms4.py        (contains InfoTik class)
#    Place them in the same folder.

# 4. Run the script
python tikvk.py
The script will ask for your Telegram Bot Token and Chat ID (where results will be sent).
After that it starts searching and validating automatically.

📦 Dependencies
Module	Purpose
requests	HTTP client
telebot	Telegram Bot API wrapper
user_agent	Random user‑agent generation
beautifulsoup4	HTML parsing (used indirectly)
SignerPy	TikTok API signature (must be obtained separately)
ms4	TikTok info fetcher (InfoTik) – custom module
Note: SignerPy and ms4 are not included in this repository. You must obtain them from your own sources.

🧠 How It Works (Flow)
Search Phase – The tool requests TikTok’s search suggest endpoint with random keywords to discover usernames.

Email Construction – Each username is turned into an email: username@mail.ru.

VK Validation – The email is checked against VK’s auth.validateAccount to see if a Mail.ru account exists and logs the result.

TikTok Validation – The email is sent to TikTok’s email/bind_without_verify endpoint using a valid signature. If the API responds with “Email is linked to another account”, the email is registered on TikTok.

Info Retrieval – If the email exists on VK, the InfoTik module fetches the TikTok profile details (username, followers, likes, etc.).

Telegram Report – Both hits and fails are sent live to your Telegram bot.

🖥️ Example Output (Terminal)
text
Hits • 12  
Bad ma • 47 
Good tik • 8
Bad tik • 52
def • @YAALI_515
⚠️ CRITICAL – Ethical & Legal Notice
This tool interacts with TikTok and VK/Mail.ru in unauthorised ways.

Do not use it for spam, harassment, doxxing, or any illegal activity.

Do not violate the Terms of Service of any platform.

This script is provided strictly for educational purposes – to demonstrate multi‑threading, API communication, and Telegram bot integration.

The author assumes zero liability for any misuse or damage caused by this software.

If you are unsure whether your use case is lawful, do not run this tool.

🛡️ Disclaimer
text
This project is not affiliated with TikTok, VK, Mail.ru, or Telegram.
All trademarks belong to their respective owners.
🤝 Contributing
This is a personal educational project; however, bug reports and suggestions are welcome via Issues.
Pull requests for code improvements (especially removing the dependency on external proprietary modules) are especially appreciated.

📞 Connect With Me
Platform	Handle
GitHub	Ali-Haidar-Sy
Telegram	@P33_9
Instagram	@_ungn
<p align="center"> <strong>🎯 Use knowledge responsibly. If this repo taught you something, give it a ⭐!</strong> </p> ```
