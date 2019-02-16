import pandas as pd
from matplotlib import pyplot

if __name__ == '__main__':
    file_loc = 'dataset/turnstile.txt'

    station_filter = 'STATION', '59 ST'
    graph_x, graph_y = ['DATE', 'TIME'], 'ENTRIES'
    bar_graph_x, bar_graph_y = ['DATE'], ['ENTRIES', 'EXITS']

    turnstile_data = pd.read_csv(file_loc)

    col, filter_value = station_filter
    st59_data = turnstile_data[turnstile_data[col] == filter_value]
    entry_exit_data = st59_data.groupby(by=graph_x).sum()

    ax = entry_exit_data[graph_y].plot()
    ax.set_xticklabels([])
    ax.set_ylabel(graph_y)

    entry_exit_data = st59_data.groupby(by=bar_graph_x).sum()
    entry_exit_data.plot.bar(y=bar_graph_y)

    pyplot.show()
