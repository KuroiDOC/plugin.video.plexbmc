import xbmcaddon
import re

menu_labels = {
    "All Shows": 30108,
    "Unwatched": 30109,
    "Recently Released": 30110,
    "Recently Added": 30111,
    "Recently Viewed": 30112,
    "Recently Aired": 30113,
    "Recently Viewed Episodes": 30114,
    "Recently Viewed Shows": 30115,
    "On Deck": 30116,
    "By Collection": 30117,
    "By Genre": 30118,
    "By Year": 30119,
    "By Decade": 30120,
    "By Director": 30121,
    "By Starring Actor": 30122,
    "By Country": 30123,
    "By Content Rating": 30124,
    "By Rating": 30125,
    "By First Letter": 30126,
    "By Folder": 30127,
    "By Resolution": 30128,
    "Season": 30129,
    "All episodes": 32130,
    "All": 30131,
    "Search...": 30132,
    "Search Shows...": 30133,
    "Search Episodes...": 30134
}
menu_patterns = (("Season", r"Season ?(\d+)$"), ("All", r"^All ?(\w+)$"))


def translate_menu_title(details):
    addon = xbmcaddon.Addon('plugin.video.plexbmc')
    if details["title"]:
        title = details["title"]
        label_id = menu_labels.get(title, -1)
        if label_id != -1:
            details["title"] = addon.getLocalizedString(label_id)
        else:
            for pattern in menu_patterns:
                match = re.match(pattern[1], title)
                if match:
                    label_id = menu_labels.get(pattern[0], -1)
                    print title
                    print label_id
                    details["title"] = addon.getLocalizedString(label_id) + " " + match.group(1)
                    break
