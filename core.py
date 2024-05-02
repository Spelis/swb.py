import dbus
import datetime
import io
import requests
from PIL import Image
import os
import shutil


def get_image():
    arturl = metadata.get("mpris:artUrl")
    content = requests.get(arturl, stream=True)
    if content.status_code == 200:
        with open('album', 'wb') as f:
            content.raw.decode_content = True
            shutil.copyfileobj(content.raw, f)

    return str(os.path.abspath('album'))


try:
    bus = dbus.SessionBus()
    player = bus.get_object(
        "org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    player_iface = dbus.Interface(player, "org.mpris.MediaPlayer2.Player")
    props_iface = dbus.Interface(player, "org.freedesktop.DBus.Properties")
    status = props_iface.Get("org.mpris.MediaPlayer2.Player", "PlaybackStatus")
    metadata = props_iface.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    pos = int(
        round(
            int(props_iface.Get("org.mpris.MediaPlayer2.Player", "Position")) / 1000000
        )
    )
    l = metadata.get("mpris:length") / 1000000
    playback = "󰏤" if status == "Paused" else "󰐊"
    hexcolor = get_image()
    bar = round((l - pos) / l * 20)
    bar = f"#" * (20 - bar) + " " * bar
    bar = bar[0: len(bar) // 2] + playback + bar[len(bar) // 2:]
    length = str(datetime.timedelta(seconds=round(l)))
    length = str(length)

except Exception as e:
    if isinstance(e, dbus.exceptions.DBusException):
        print("not playing.")
    else:
        print(e)
