import collections
import matplotlib.pyplot as plt
from japanmap import picture
from pylab import rcParams


def plotJapan(data, output_fig_path, map_width_inches=20, map_height_inches=20):
    rcParams['figure.figsize'] = (map_width_inches, map_height_inches)
    plt.imshow(picture(data))
    plt.savefig(output_fig_path)


if __name__ == '__main__':
    """
        Count the number of prefectures and fill them in red.
    """
    output_fig_path = 'map.png'

    with open("prefecture_data.txt", "r", encoding="utf-8") as f:
        INPUT_DATA = [line.strip("\n") for line in f.readlines()]

    with open("count_data.csv", "w", encoding="utf-8") as f:
        for prefecture, number in dict(collections.Counter(INPUT_DATA)).items():
            f.write(prefecture+","+str(number)+"\n")

    color = "red"
    data = {}
    for line in INPUT_DATA:
        data[line] = color

    plotJapan(data, output_fig_path)

    print("output image >> {}".format(output_fig_path))
    print("count file: {}".format("count_data.csv"))
