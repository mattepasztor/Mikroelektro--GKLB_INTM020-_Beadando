 #Zenelejátszás Python segítségével & Loop létrehozás
 
 import vlc
 player = vlc.MediaPlayer("/home/pi/Music/music.mp3")
 player.play()
 
 vlc_instance = vlc.Instance("--input-repeat=999")
 music = vlc_instance.media_new("/home/pi/Music/music.mp3")
 
 player.set_media(music)
 player.audio_set_volume(100)
 player.play()
 
 