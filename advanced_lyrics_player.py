import pygame
import time
import os
import threading
from colorama import init, Fore, Style
from pyfiglet import Figlet


class AestheticLyricsPlayer:

    def __init__(self, song_file):

        init(autoreset=True)

        self.song_file = song_file
        self.print_lock = threading.Lock()

        self.colors = [
            Fore.LIGHTMAGENTA_EX,
            Fore.CYAN,
            Fore.LIGHTYELLOW_EX,
            Fore.LIGHTRED_EX,
            Fore.GREEN,
            Fore.LIGHTBLUE_EX
        ]

        self.lyrics = [

            (0, Fore.CYAN,
             "🍷 Nashe mein hum nahi hai..."),

            (2, Fore.LIGHTRED_EX,
             "✨ Yeh sama nasheela hai..."),

            (4.5, Fore.YELLOW,
             "🥃 Paani bhi peete hai..."),

            (6.5, Fore.MAGENTA,
             "🔥 Toh lagta hai tequila hai..."),

            (9, Fore.LIGHTMAGENTA_EX,
             "❤️ Mood aashikana hai..."),

            (11, Fore.YELLOW,
             "🌅 Subah ghar jaana hai..."),

            (13, Fore.CYAN,
             "✨ Tune kaisa jaadu hai kiya...")
        ]

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def banner(self):
        fig = Figlet(font="slant")

        print(
            Fore.LIGHTMAGENTA_EX +
            fig.renderText("MUSIC PLAYER")
        )

        print(
            Fore.CYAN +
            "=" * 70
        )

        print(
            Fore.YELLOW +
            "🎵 Python Aesthetic Lyrics Terminal 🎵\n"
        )

    def typewriter(self, text, color, delay=0.05):

        with self.print_lock:
            # Clear the visualizer line first
            print("\r" + " " * 80 + "\r", end="", flush=True)
            for char in text:
                print(color + char, end="", flush=True)
                time.sleep(delay)
            print()

    def loading_animation(self):

        print(Fore.GREEN + "Loading song", end="")

        for _ in range(6):
            time.sleep(0.4)
            print(".", end="", flush=True)

        print("\n")

    def play_song(self):

        pygame.mixer.init()
        pygame.mixer.music.load(self.song_file)
        pygame.mixer.music.play()

    def show_lyrics(self):

        start_time = time.time()

        for lyric_time, color, text in self.lyrics:

            while time.time() - start_time < lyric_time:
                time.sleep(0.1)

            self.typewriter(text, color)

    def music_visualizer(self):

        bars = [
            "▁▂▃▄▅▆▇█▇▆▅▄▃▂",
            "▂▃▄▅▆▇█▇▆▅▄▃▂▁",
            "▄▅▆▇█▇▆▅▄▃▂▁▂▃",
            "▇█▇▆▅▄▃▂▁▂▃▄▅▆"
        ]

        index = 0

        while pygame.mixer.music.get_busy():

            with self.print_lock:
                print(
                    "\r" + self.colors[index % len(self.colors)] +
                    bars[index % len(bars)] + " " * 10,
                    end="",
                    flush=True
                )

            index += 1
            time.sleep(0.15)

        # Clear the visualizer line when music stops
        with self.print_lock:
            print("\r" + " " * 80 + "\r", end="", flush=True)

    def run(self):

        self.clear()
        self.banner()
        self.loading_animation()

        self.play_song()

        import threading

        visualizer_thread = threading.Thread(
            target=self.music_visualizer,
            daemon=True
        )

        visualizer_thread.start()

        self.show_lyrics()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

        print(
            Fore.GREEN +
            "\n\n🎶 Song Finished Successfully 🎶"
        )


if __name__ == "__main__":

    player = AestheticLyricsPlayer("song.mpeg")
    player.run()