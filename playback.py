import core

title = core.metadata.get('xesam:title')
if len(title) > 15:
    title = title[:12] + '...'


print(
    f"""{title} {core.metadata.get('xesam:artist')[0]}"""
)
