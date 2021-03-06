 #Zenelejátszás Python segítségével & Loop létrehozás & Bash környezethez kiegészítés & fizikai gomb
 #szundi funkció && ébresztés és gombnyomás közt eltelt reakcióidő kiszámítása
 #Reakcióidő fájlba írása
 #kimeneti fájl elérési útjának módosítása
 
import vlc
from gpiozero import Button
from time import sleep
from datetime import datetime
 
starttime = datetime.now()
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
    stoptime = datetime.now()
    diff = stoptime - starttime
    #print(diff.total_seconds())
    with open('/home/pi/Scripts/output.txt', 'a') as f:
        f.write (str(datetime.now()))
        f.write ('\tResponse time: ')
        f.write (str(diff.total_seconds()))
        f.write (' sec\n')
        f.close()
    
def released(btn):
    if not btn.was_held:
        pressed()
    btn.was_held = False

def pressed():
    player.pause()
    sleep(1)
    player.play()

btn = Button(17, hold_time=3)

btn.when_held = held
btn.when_released = released

while True: pass

