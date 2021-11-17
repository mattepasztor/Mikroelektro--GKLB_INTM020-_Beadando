 #Zenelejátszás Python segítségével & Loop létrehozás & Bash környezethez kiegészítés & fizikai gomb
 #szundi funkció
 
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
  btn = Button(17, hold_time=2)
 
  Button.was_held = False
  def held(btn):
      btn.was_held = True  
      player.stop()
  def released(btn):
    if not btn.was_held:
       pressed()
    btn.was_held = False
  def pressed():
    player.pause()
    sleep(3)
    player.play()
  btn.when_held = held
  btn.when_released = released
 
 
 