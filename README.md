
# 🤖 Alerna – A Self-Learning Python Chatbot

```
╔═══╦╗
║╔═╗║║
║║─║║║╔══╦═╦═╗╔══╗
║╚═╝║║║║═╣╔╣╔╗╣╔╗║
║╔═╗║╚╣║═╣║║║║║╔╗║
╚╝─╚╩═╩══╩╝╚╝╚╩╝╚╝
```

**Learn, Remember, Improve, Redo.**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License](https://img.shields.io/badge/License-GNU-green)

Alerna is a **terminal-based chatbot** that **learns from your conversations**.
If it doesn’t know how to answer something, you can teach it — and it will remember forever by saving to a local `training.json` file.

It comes with **100 pre-recorded Q\&A entries** to get started right away, but grows smarter the more you chat.

---

## ✨ Features

* 🧠 **Learns dynamically** – Teach Alerna new answers, and it stores them permanently.
* 📂 **Local memory** – Knowledge is saved in `training.json` and reused across all chats.
* 🎓 **100+ preloaded Q\&As** – Starts with a solid foundation of knowledge.
* 🔄 **Persistent learning** – No internet or cloud required; works fully offline.
* 🎨 **Colorful CLI** – Uses `colorama` for a retro-styled terminal experience.
* 🔍 **Fuzzy matching** – Can recognize similar phrases even with typos (via `difflib`).
* ⚡ **Lightweight & extensible** – Just Python and JSON, easy to hack and expand.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/alerna.git
cd alerna
```

### 2️⃣ Install dependencies

```bash
pip install colorama
```

### 3️⃣ Run Alerna

```bash
python alerna.py
```

---

## 🗂️ File Structure

```
alerna/
│── alerna.py        # Main chatbot program
│── training.json    # Knowledge base (preloaded with 100+ Q&As)
│── feed_bot.py      # (Optional) Extra setup/boot logic
|__ language_pack.json # predefined questions
│── README.md        # Documentation
```

---

## 📝 Example Usage

```
Alerna $> hello
Alerna: Hello there!

Alerna $> what's 2+2?
Alerna: 4

Alerna $> what's my favorite color?
im sorry i do not know that statement, whats the answer to that, or how to respond to it? >> blue
Got it, now on ill answer what's my favorite color with blue
```

*(Now later…)*

```
Alerna $> what's my favorite color?
Alerna: blue
```

---

## 🔧 Commands

* `quit` → Exit the chatbot.
* `refresh_screen` → Clears and redraws the ASCII logo + motto.

---

## 🔮 Roadmap / Ideas

* 🔗 Improve text matching with AI/NLP libraries (spaCy, Transformers, etc).
* 💾 Add export/import of knowledge to share trained bots.
* 🎤 Optional voice input/output with `speech_recognition` and `pyttsx3`.

---

## 🤝 Contributing

Contributions, ideas, and pull requests are welcome!

---

## 📜 License

This project is licensed under the **GNU General Public License** – free to use, learn from, and improve.

---

⚡ Would you like me to also design a **GitHub banner/logo image** (like a retro neon “Alerna” header) that you can put at the very top above the ASCII art? It’ll really make the repo pop.
