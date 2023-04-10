import json
from collections import defaultdict
from textwrap import wrap

import matplotlib.pyplot as plt


def get_playlists_data(file, top_n):
    f = open(file, encoding='utf8')
    playlists_dicts = json.load(f)['playlists']
    # names = [(i, playlist_dict['name']) for i, playlist_dict in enumerate(playlists_dicts)]
    # print(names)
    playlists_data = {}
    for playlist in playlists_dicts:
        temp = defaultdict(int)
        for item in playlist['items']:
            temp[item['track']['artistName']] += 1

        temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
        print(f'{playlist["name"]}\n\t{temp[:top_n]}')

        playlists_data[playlist['name']] = temp
    return playlists_data


def plot_top(full_data, top_n):
    fig, axes = plt.subplots(len(full_data), layout='constrained')
    fig.set_figheight(100)
    plt.subplots_adjust(hspace=1)
    i = 0
    for name, playlist in full_data.items():
        vals = [val for name, val in playlist[:top_n]]
        names = ['\n'.join(wrap(name, 10, break_long_words=False)) for name, val in playlist[:top_n]]
        axes[i].bar(names, vals)
        axes[i].set_ylabel('Num of songs')
        axes[i].set_title(name)
        i += 1
    plt.savefig('fig.png')
    plt.close(fig)


def main(file='MyData/Playlist1.json', n=5):
    data = get_playlists_data(file, n)
    plot_top(data, n)


if __name__ == '__main__':
    main()
    plt.show()
