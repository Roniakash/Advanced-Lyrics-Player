# 🎵 Python Aesthetic Lyrics Player

A highly-stylized, terminal-based music player and lyric synchronizer. It utilizes **Pygame Mixer** for audio playback, **Colorama** for vibrant CLI styling, and **Pyfiglet** for high-impact ASCII banners.

The application is engineered with **multi-threaded synchronization** using Python's `threading.Lock` to ensure a smooth, race-condition-free visualizer experience where animated lyrics and visualizer bars live together in harmony on the CLI.

---

## ✨ Features

- **🚀 Dynamic ASCII Banner:** Features a high-contrast terminal header generated on startup.
- **🎙️ Thread-Synchronized Output:** Uses locking primitives (`threading.Lock`) so the active audio visualizer gracefully yields and moves down when a new lyric types out, preventing console text overlap.
- **🎨 Premium HSL Color Palette:** Utilizes HSL-tailored colors from the Colorama palette.
- **⚡ Synchronized Typewriter Effects:** Implements custom typing speed delays matched with the exact timeline of the song.
- **📊 Real-time Terminal Visualizer:** Renders an animated terminal soundbar that dynamically updates and self-terminates when the music finishes.

---

## 🛠️ Project Structure

```
MusicProject/
│
├── advanced_lyrics_player.py  # Main executable application code
├── requirements.txt           # External Python dependencies
├── song.mpeg                  # 15-second reference audio track
└── Readme.MD                  # Documentation
```

---

## 🚀 Installation & Setup

Follow these steps to set up the project locally:

### 1. Initialize Virtual Environment

Create a clean environment for your dependencies:

```powershell
python -m venv venv
```

### 2. Activate the Virtual Environment

- **PowerShell:**

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

- **Command Prompt (CMD):**

  ```cmd
  venv\Scripts\activate.bat
  ```

- **Bash / Linux / macOS:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install all required libraries via pip:

```bash
pip install -r requirements.txt
```

---

## 🎮 Running the Player

Once the environment is active and dependencies are installed, launch the player:

```powershell
python .\advanced_lyrics_player.py
```

Enjoy your synchronized, aesthetic terminal music experience! 🎶
