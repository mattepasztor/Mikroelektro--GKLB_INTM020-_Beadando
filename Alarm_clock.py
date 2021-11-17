 #Zenelejátszás Python segítségével & Loop létrehozás & Bash környezethez kiegészítés & fizikai gomb
 
 import vlc
 player = vlc.MediaPlayer("/home/pi/Music/music.mp3")
 player.play()
 
 vlc_instance = vlc.Instance("--input-repeat=999")
 music = vlc_instance.media_new("/home/pi/Music/music.mp3")
 
 player.set_media(music)
 player.audio_set_volume(100)
 player.play()
 
  while True: pass
  
 from gpiozero import Button
 btn = Button(17)
 
 def stopMusic():
    player.stop()
 btn.when_pressed = stopMusic
 
 