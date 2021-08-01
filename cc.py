#chromecast tests
import time
import pychromecast
import sys

tv3_url = 'https://directes-tv-int.ccma.cat/int/ngrp:tvi_web/playlist.m3u8'
eitb2_url = 'https://live-dvr.eitb-fastly.cross-media.es/live-content/etb2hd-hls/master.m3u8'

cast = pychromecast.Chromecast('192.168.1.3')
cast.wait()
time.sleep(0.1)

mc = cast.media_controller

if (sys.argv[1] == "pause"):
    mc.pause()

if (sys.argv[1] == "stop"):
    mc.stop()

if (sys.argv[1] == "play"):
    mc.play()

if (sys.argv[1] == "vol"):
    volume = float(sys.argv[2]) * 0.1 #vol is [0-1.0] so *0.1 so argv can be [0-1]
    cast.set_volume(volume)

if (sys.argv[1] == "info"):
    print(mc.status)
    print(mc.status.content_id)

if (sys.argv[1] == "tv3"):
    connection_try = 0
    while (True):
        mc.play_media(tv3_url, 'video')
        print(f"Casting TV3 to {cast.device.friendly_name}");
        connection_try += 1
        time.sleep(2.0)
        if (mc.status.content_id != None):
            print(f"Connected! {mc.status.content_id}")
            break
        if (connection_try >= 3):
            print("Too many unfulfilled connection requests")
            break
        print("Reconnecting...");

if (sys.argv[1] == "etb"):
    connection_try = 0
    while (True):
        mc.play_media(eitb2_url, 'video')
        print(f"Casting eitb to {cast.device.friendly_name}");
        connection_try += 1
        time.sleep(2.0)
        if (mc.status.content_id != None):
            print(f"Connected! {mc.status.content_id}")
            break
        if (connection_try >= 3):
            print("Too many unfulfilled connection requests")
            break
        print("Reconnecting...");
