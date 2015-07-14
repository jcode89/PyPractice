class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    def add_me_a_line(self):
        new_lyric = raw_input("What Lyrics shall we add? Type one! ")
        self.lyrics.append(new_lyric)
    def last_line(self):
        print self.lyrics.pop()	
happy_bday = Song(
        ["Happy birthday to you",
		 "I don't want to get sued",   
		"So i'll stop right there"]
)

bulls_on_parade = Song(
         ["They rally around the family",
		 "with pockets full of shells"]
)

taylor_swift_bad_blood = ["And it's so sad too",
        "Think about the good times",
        "You and I."]
        
# Calls the sing_me_a_song() method and prints out the lyrics one line at a time.     
happy_bday.sing_me_a_song()

# Does the same as the call above.
bulls_on_parade.sing_me_a_song()

# This calls the last_line() method which removes the last lyric from the list and displays it
bulls_on_parade.last_line()

# This prompts you to add a lyric to the song.
happy_bday.add_me_a_line()

# This will print out the lyrics including the new one you just added.
happy_bday.sing_me_a_song()

# Prompts to add a lyric
bulls_on_parade.add_me_a_line()

# Displays the new lyrics, the last line still removed and the new lyric added.
bulls_on_parade.sing_me_a_song()

# For this we instantiate the class and pass it the variable taylor_swift_bad_blood
tay_swift = Song(taylor_swift_bad_blood)

# This calls the sing_me_a_song method and displays the lyrics.
tay_swift.sing_me_a_song()