class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    def add_me_a_line(self):
        new_lyric = raw_input("What Lyrics shall we add? Type one! ")
        self.lyrics.append(new_lyric)
        		
happy_bday = Song(
        ["Happy birthday to you",
		 "I don't want to get sued",   
		"So i'll stop right there"]
)

bulls_on_parade = Song(
         ["They rally around the family",
		 "with pockets full of shells"]
)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
happy_bday.add_me_a_line()
happy_bday.sing_me_a_song()
bulls_on_parade.add_me_a_line()
bulls_on_parade.sing_me_a_song()