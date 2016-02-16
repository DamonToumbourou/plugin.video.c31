from xbmcswift2 import Plugin, xbmcgui
#from resources.lib import thisweekscraper


plugin = Plugin()


@plugin.route('/')
def main_menu():

    item = [
        {
            'label': 'Watch C31 Live',
            'path': plugin.url_for('live_stream'),
        }
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


if __name__ == '__main__':
    plugin.run()
