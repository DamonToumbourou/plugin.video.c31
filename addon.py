from xbmcswift2 import Plugin, xbmcgui
from resources.lib import c31scraper

PLUGIN_URL = 'plugin://plugin.video.youtube/play/?video_id'

plugin = Plugin()


@plugin.route('/')
def main_menu():

    item = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('live_stream'),
        },
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('get_shows'),
        },
        {
            'label': plugin.get_string(30002),
        },
        {
            'label': plugin.get_string(30003),
        },
        {
            'label': plugin.get_string(30004),
        },
        { 
            'label': plugin.get_string(30005),
        },
        {
            'label': plugin.get_string(30006),
        },
        {
            'label': plugin.get_string(30007),
        },
    ]

    return item


@plugin.route('/live_stream/')
def live_stream():

    item = []
    
    item.append(
        plugin.play_video({
            'label': 'C31 Live',
            'path': 'http://c31.mediafoundry.com.au/sites/default/files/manifest/manifest_live_27.m3u8',
        })
    )

    
    return item


@plugin.route('/get_shows/')
def get_shows():
    KEYWORD= 'Uploads'
    item = [
        {
            'label': '4WD TV',
            'path': plugin.url_for('play_show', url='https://www.youtube.com/user/4wdTVtube', keyword=KEYWORD),
            'thumbnail': 'http://www.c31.org.au/library/program/preview_lg//4wd-440x326.jpg',
        },
        {
            'label': """Vasili's Garden to Kitchen""",
            'path': plugin.url_for('play_show', url='https://www.youtube.com/channel/UCUNfGu0l8O6FvCsuvJFgHOA/featured', keyword=KEYWORD),
            'thumbnail': 'http://www.c31.org.au/library/program/preview_lg//vasili_hag_main_2.jpg',
        },
        {
            'label': 'On the List... Melbourne',
            'path': plugin.url_for('play_show', url='https://www.youtube.com/channel/UCbcvUNnJEsQLzciJr9RFvRg', keyword=KEYWORD),
            'thumbnail': 'http://www.c31.org.au/library/program/preview_lg/onthelist_largenew.jpg',
        },
        {
            'label': 'New Game Plus',
            'path': plugin.url_for('play_show', url='https://www.youtube.com/user/NewGamePlusTV', keyword=KEYWORD),
            'thumbnail': 'http://www.c31.org.au/library/program/preview_lg//newgameplus_main.jpg',
        },
        {
            'label': 'Mr Sink Show',
            'path': plugin.url_for('play_show', url='https://www.youtube.com/channel/UCpCZWhMIPrMpAL9x1oG264w', keyword=KEYWORD),
            'thumbnail': 'http://www.c31.org.au/library/program/preview_lg//mrsink_largenew.jpg',
        }
    ]

    return item


@plugin.route('/get_shows/<url>/<keyword>')
def play_show(url, keyword):

    item = []

    content = c31scraper.get_content(url, keyword)

    for i in content:
        item.append({
            'label': i['label'],
            'path': PLUGIN_URL + i['path'],
            'thumbnail': i['thumbnail'],
            'is_playable': True,
        })

    return item


if __name__ == '__main__':
    plugin.run()
