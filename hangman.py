import random

class HangmanGame:
    def __init__(self):
        self.words = [
                      {'digital':['python', 'programming', 'computer', 'keyboard',
                      'developer', 'algorithm', 'hangman', 'variable']},
                      {'pekerjaan':["guru", "dokter", "polisi", "pemadam", "insinyur", 
                      "programmer", "chef","arsitek", "penulis", "seniman", 
                      "petani", "nelayan", "pilot", "pramugari","perawat", 
                      "akuntan", "sekretaris", "resepsionis", "tukang", 
                      "desainer","fotografer", "wartawan", "hakim", 
                      "pengacara", "musisi", "penyanyi","penari", 
                      "atlet", "pelukis", "pemahat"]},
                      {'hewan':["singa", "gajah", 
                      "harimau", "jerapah", "buaya", "ular", "kuda","kucing", 
                      "anjing", "monyet", "beruang", "serigala", "rubah", "kelinci", 
                      "kangguru", "koala", "penguin", "lumba-lumba", "paus", "hiu", 
                      "gurita", "cumi-cumi", "burung", "ayam", "bebek", "domba", 
                      "sapi", "kambing", "marmut", "tupai", "landak"]}, 
                      {'buah':["apel", 
                      "jeruk", "pisang", "mangga", "anggur", "semangka", 
                      "melon", "nanas", "pepaya", "stroberi", "kiwi", 
                      "alpukat", "rambutan", "durian", "salak", 
                      "manggis", "jambu", "belimbing", "markisa", 
                      "leci", "delima", "pir", "plum", "persik", "ceri", 
                      "kurma"]}, 
                      {'benda':["meja", "kursi", "lemari", "tempat tidur", "lampu", 
                      "buku", "pensil", "pulpen", "kertas", "komputer", "handphone", 
                      "televisi", "kipas", "ac", "kulkas", "oven", "microwave", "setrika", 
                      "mesin cuci", "tas", "sepatu", "topi", "jam tangan", "dompet", 
                      "kacamata", "payung", "botol", "gelas", "piring", "sendok", 
                      "garpu", "pisau"]}
                      ]
        self.reset_game()

    def reset_game(self):
        kategori = random.choice(self.words)  # Pilih dict seperti {'hewan': [...]}
        self.kategori, daftar_kata = list(kategori.items())[0]  # Ambil key dan value
        self.secret_word = random.choice(daftar_kata).lower()
        self.guessed_letters = []
        self.attempts_left = 6
        self.game_over = False
        self.won = False

    def display_current_state(self):
        
        display = [letter if letter in self.guessed_letters else '_' for letter in self.secret_word]
        return ' '.join(display)

    def get_hangman_art(self):
        stages = [
            f"""
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |
            """,
            f"""
               ------
               |    |
               |    O
               |   /|\\
               |   /
               |
            """,
            f"""
               ------
               |    |
               |    O
               |   /|\\
               |
               |
            """,
            f"""
               ------
               |    |
               |    O
               |   /|
               |
               |
            """,
            f"""
               ------
               |    |
               |    O
               |    |
               |
               |
            """,
            f"""
               ------
               |    |
               |    O
               |
               |
               |
            """,
            f"""
               ------
               |    |
               |
               |
               |
               |
            """
        ]
        return stages[self.attempts_left]

    def make_guess(self, letter):
        if self.game_over:
            return "Game is already over!"

        letter = letter.lower()

        if len(letter) != 1 or not letter.isalpha():
            return "Please enter a single valid letter."

        if letter in self.guessed_letters:
            return "You already guessed that letter."

        self.guessed_letters.append(letter)

        if letter not in self.secret_word:
            self.attempts_left -= 1
            message = f"Wrong! {self.attempts_left} attempts left."
        else:
            message = "Correct guess!"

        if self.attempts_left == 0:
            self.game_over = True
            self.won = False
            return f"{message}\nGame over! The word was: {self.secret_word}"

        if all(l in self.guessed_letters for l in self.secret_word):
            self.game_over = True
            self.won = True
            return f"{message}\nCongratulations! You guessed the word: {self.secret_word}"

        return message

    def play(self):
        while True:
            print("\n🎮 Welcome to Hangman!")
            print(f"Kategori: {self.kategori.capitalize()}")
            print("Guess the word. You have 6 attempts to save the hangman.")

            while not self.game_over:
                print(self.get_hangman_art())
                print("Word: " + self.display_current_state())
                print("Guessed letters: " + ", ".join(self.guessed_letters))

                guess = input("Guess a letter: ")
                result = self.make_guess(guess)
                print(result)

            print("\nYou won!" if self.won else "\nYou lost!")
            print("The word was:", self.secret_word)

            again = input("\nDo you want to play again? (y/n): ").lower()
            if again == 'y':
                self.reset_game()
            else:
                print("\nThanks for playing Hangman!")
                break

# Jalankan Game
if __name__ == "__main__":
    game = HangmanGame()
    game.play()
