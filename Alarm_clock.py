 #Zenelejátszás Python segítségével & Loop létrehozás & Bash környezethez kiegészítés & fizikai gomb
 #szundi funkció
 
 import vlc
 from gpiozero import Button
 from time import sleep
 
vlc_instance = vlc.Instance("--input-repeat=999")
player = vlc_instance.media_player_new()
song = vlc_instance.media_new("/home/pi/Music/music.mp3")

player.set_media(song)
player.audio_set_volume(100)
player.play()
 
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
    sleep(5)
    player.play()

btn = Button(17, hold_time=3)

btn.when_held = held
btn.when_released = released

while True: pass