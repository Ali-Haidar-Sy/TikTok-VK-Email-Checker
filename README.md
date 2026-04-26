<p align="center">
  <pre>
▀▀█▀▀ █ █ █▀▀ █▀▀█ █▀▀█    █  █ █  █    █▀▀ █▀▀█ █▀▀█ █  █   █▀▀ █  █ █▀▀ █▀▀█ █  █ █▀▀ █▀▀█
  █   █ █ █▀▀ █▄▄▀ █  █    █▄▄█ █▀▀█    █▀▀ █  █ █  █ ▀▀█   █▀▀ █▀▀█ █▀▀ █  █ █▄▄  █▀▀ █▄▄▀
  ▀   ▀▀▀ ▀▀▀ ▀ ▀▀ ▀▀▀▀    ▀  ▀ ▀  ▀    ▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀   ▀▀▀ ▀  ▀ ▀▀▀ ▀▀▀▀ ▄▄█ ▀▀▀ ▀ ▀▀
  </pre>
</p>

<h1 align="center">📧 TikTok · VK · Email Checker<br><sub>Multi‑platform account validator & OSINT info gatherer</sub></h1>

<p align="center">
  <strong>Automated multi‑service email verification + TikTok profile lookup, all reported via Telegram bot.</strong><br>
  <em>Educational / research tool – use responsibly.</em>
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

## 💡 What does this tool do?

- **VK (Mail.ru) account validation** – checks whether a mail.ru email is linked to a VK account and retrieves associated TikTok profile info if available.
- **TikTok email binding check** – verifies if a mail.ru email is attached to an active TikTok account (via internal API, with signature generation).
- **TikTok profile lookup** – using the `InfoTik` module, fetches username, followers, following, likes, country, and registration date.
- **Automated search & threading** – uses TikTok’s search suggestion API to generate plausible usernames → `@mail.ru` emails, then scans them in bulk across both platforms.
- **Telegram reporting** – every found account’s data is sent to a specified Telegram chat via bot API.

---

## ⚡ Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ali-Haidar-Sy/TikTok-VK-Email-Checker.git
   cd TikTok-VK-Email-Checker
Install standard dependencies

bash
pip install requests telebot pyTelegramBotAPI beautifulsoup4 user_agent
Obtain required private modules
You must place the following files in the same directory (not publicly provided):

SignerPy – TikTok’s Gorgon/Argus/Khronos signer

ms4 (or InfoTik) – TikTok profile info scraper

Run the script

bash
python checker.py
You will be prompted for:

Telegram Bot Token (from @BotFather)

Chat ID where results should be sent

The tool will then start searching and checking emails continuously.

🛠 How it works
Phase	Description
1. Search	Uses TikTok’s public search suggestion API to generate random email addresses in the form username@mail.ru.
2. VK validation	Calls api.vk.ru/method/auth.validateAccount to see if the email exists on VK.
3. TikTok check	Sends a bind‑check request to TikTok’s internal /passport/email/bind_without_verify/ endpoint (requires signature generation).
4. Profile info	If the email passes VK, the InfoTik module retrieves full TikTok profile data.
5. Telegram report	All findings are formatted and pushed to your Telegram chat.
📦 Dependencies
Package	Purpose
requests	HTTP client
telebot & pyTelegramBotAPI	Telegram bot interaction
beautifulsoup4	HTML parsing
user_agent	Random user‑agent generation
SignerPy (local)	TikTok API signature (Gorgon/Argus)
ms4 / InfoTik (local)	TikTok profile data extraction
⚠️ The proprietary modules SignerPy and ms4 are not included in this repository. You must obtain them separately.

📸 Example Telegram Output
text
===============
User » example_user
Name » Example User
Email • example@mail.ru
Followers » 12.5K
Following » 240
Like » 1.2M
Date » 2020-01-15
Country » US
By » @XEF_R
===============
⚠️ Ethical & Legal Notice
This tool interacts with third‑party services (VK, TikTok) and automates account checks.

Use it only on email addresses you own or for which you have explicit authorisation.

Unauthorised scanning, scraping, or data collection may violate TikTok’s and VK’s Terms of Service.

This project is strictly for educational and research purposes.

You are solely responsible for any misuse and legal consequences.

The author assumes no liability.

🛡️ Disclaimer
text
This tool is not affiliated with TikTok, VK, Mail.ru, or any related entities.
All trademarks belong to their respective owners.
🤝 Contributing
Found a bug? Want to add proxy support or enhance threading?
Open an Issue or submit a Pull Request.

📞 Connect With Me
Platform	Handle
GitHub	Ali-Haidar-Sy
Telegram	@P33_9
Instagram	@_ungn
<p align="center"> <strong>📡 Star the repo if you find it useful!</strong> </p> ```
