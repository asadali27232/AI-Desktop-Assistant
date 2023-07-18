from playsound import playsound

class MusicPlayer:
    def listen_music(self, file_path):
        playsound(file_path)

# Create an instance of the MusicPlayer class
player = MusicPlayer()

# Specify the path to your MP3 file
mp3_file = "path/to/your/file.mp3"

# Call the listen_music() method to play the MP3 file
player.listen_music(mp3_file)
