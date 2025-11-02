---
NOTE: .exe file location : "yt_fb_secure_blackgold\dist\YTtoFBUploader.exe"
---


````markdown
# 🎥 YT → FB Secure Uploader (Black & Gold Edition)

> 🖤 A modern, secure, and stylish way to transfer your YouTube videos directly to Facebook Pages — built for creators who value both design and functionality.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Build-Stable-success)
![UI](https://img.shields.io/badge/UI-CustomTkinter-black)
![Theme](https://img.shields.io/badge/Theme-Black%20%26%20Gold-gold)

---

## 🖥️ Overview

**YT_FB_Secure** is a desktop application that allows you to **download YouTube videos** and **upload them directly to Facebook Pages** with just one click.  
It features a **Black & Gold modern UI**, **password-protected access**, and **secure local token storage** — no data is ever shared online.

Built for content creators who want a simple yet powerful bridge between YouTube and Facebook.

---

## ✨ Key Features

- 🎨 **Sleek Black & Gold UI** – Professionally designed with CustomTkinter.  
- 🔒 **Password Protection** – App unlocks only after correct password input.  
- 📥 **YouTube Downloader** – Uses `yt_dlp` for high-quality and reliable downloads.  
- 📤 **Facebook Uploader** – Uploads videos directly to Facebook Pages.  
- ⚙️ **FFmpeg Integration** – Enables smooth, fast, and high-quality video conversion.  
- 🧠 **Error Handling** – Smart feedback if uploads or tokens fail.  
- 🪶 **Lightweight Executable** – Fully packaged `.exe` version available for Windows.

---

## 🧩 Tech Stack

| Component | Description |
|------------|-------------|
| **Language** | Python 3.13 |
| **UI Framework** | CustomTkinter |
| **Video Downloader** | yt_dlp |
| **Uploader Engine** | Facebook Graph API |
| **Video Processor** | FFmpeg |
| **Build Tool** | PyInstaller |

---

## ⚙️ Installation & Setup

### 🪄 Step 1: Clone the Repository
```bash
git clone https://github.com/Vedhanth-P/yt_fb_secure.git
cd yt_fb_secure
````

### 🧰 Step 2: Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 📦 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🎬 Step 4: Verify FFmpeg

Ensure `ffmpeg` is installed and accessible from the command line:

```bash
ffmpeg -version
```

If not installed, download from [ffmpeg.org/download.html](https://ffmpeg.org/download.html).

---

## 🔑 Facebook API Setup

1. Visit [Meta for Developers](https://developers.facebook.com/apps).
2. Create a new **App** (choose “Business” or “Creator” type).
3. Add **Facebook Graph API**.
4. Generate a **Page Access Token** with these permissions:

   * `pages_read_engagement`
   * `pages_show_list`
   * `pages_manage_posts`
5. Copy the token and enter it into the application securely.

> ⚠️ **Privacy Note:** Tokens and passwords are stored locally, never uploaded online.

---

## 💡 How to Use

1. Run the app:

   ```bash
   python app.py
   ```
2. Enter the **password** to unlock.
3. Paste your **YouTube video link**.
4. Enter your **Facebook Page ID** and **Access Token**.
5. Click **Upload** — your video is automatically posted to your page! 🎉

---

## 🧱 Folder Structure

```
yt_fb_secure/
│
├── app.py
├── requirements.txt
├── README.md
├── icon.ico
├── assets/
│   └── (UI and image files)
└── dist/
    └── YTtoFBUploader.exe
```

---

## 🖼️ Screenshots (Preview)

> *(Replace these placeholder images with your actual screenshots once available.)*

| 🖼️ Interface                                                                      | Description                               |
| ---------------------------------------------------------------------------------- | ----------------------------------------- |
| ![Login](https://via.placeholder.com/400x220?text=Password+Login+Screen)           | Secure login interface with password gate |
| ![Uploader](https://via.placeholder.com/400x220?text=YouTube+to+Facebook+Uploader) | Clean upload panel with placeholders      |
| ![Success](https://via.placeholder.com/400x220?text=Upload+Successful)             | Confirmation after successful upload      |

---

## 🧱 Future Enhancements

* 🔄 Automatic token refresh
* 🗂️ Multi-video upload queue
* 📝 Editable title & description before upload
* 🌐 Cross-platform upload support (Instagram, TikTok, etc.)

---

## ⚖️ License

This project is licensed under the **MIT License** — use, modify, and distribute freely with attribution.

---

## 💬 Credits

Developed and designed by **[Vedhanth P](https://github.com/Vedhanth-P)**
🎥 YouTube Channel: [Vedhanth113](https://www.youtube.com/@Vedhanth113)
💡 Concept & UI Design: Vedhanth P
🧠 Backend Logic: Vedhanth P
🛠️ Libraries: `yt_dlp`, `customtkinter`, `requests`, `ffmpeg`, `os`, `json`

> *“Automation meets creativity — streamline your workflow, amplify your content.”* 💫

---

## 🌟 Support the Project

If this tool helped you, please ⭐ **star the repository** on GitHub —
it motivates further updates and keeps the project alive! ❤️

[![Star on GitHub](https://img.shields.io/github/stars/Vedhanth-P/yt_fb_secure?style=social)](https://github.com/Vedhanth-P/yt_fb_secure/stargazers)

---

## COPYRIGHTS

MIT License

Copyright (c) 2025 Vedhanth P

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
---
