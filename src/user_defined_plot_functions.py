"""User defined plot functions."""

import pandas
import seaborn
from matplotlib import pyplot

   
def plot(kind: seaborn, data: pandas.DataFrame, x_arg: str = None, y_arg: str = None, title: str = "No Title",
         order: str | list = None, annot: bool = False, col: str = None, hue: str = None, x_label: str = None,
         y_label: str = None, color: seaborn.color_palette() = seaborn.color_palette()[0], bin_size: int = 50,
         marker_: str = "o") -> None:
    """
    A univariate plot function that creates defined seaborn plot.

    :param kind: seaborn plot
    :param data: The dataframe from where the feature is to be plotted.
    :param x_arg: x-axis parameter. Default value, None.
    :param y_arg: y-axis parameter. Default value, None.
    :param title: Title of the plot. Default value, "No Title".
    :param order: Arrgement of x-axis plot values. Default value, None.
    :param annot: Add anootation to plots. Specifically for seaborn barplot. Default value, False.
    :param col: Column to use for anootation basis. This must be used togerther with annot. Default value, None.
    :param hue: Additional parameter for multivatriate plots as barplot, countplot and scatterplot. Default, None.
    :param x_label: x_axis label. Default value, None.
    :param y_label: y_axis label. Default value, None.
    :param color: seaborn color palete for visualization. Default value, seaborn.color_palette()[0].
    :param bin_size: Integer value for the bin size in histogram plots. Default value, 50.
    :param marker_: Marker type to be used. Specifically for line plot. Default value, 'o'.
    """
    if kind == seaborn.lineplot:
        kind(data=data, x=x_arg, y=y_arg, hue=hue, color=color, marker=marker_)
        pyplot.title(title, size=12, weight='bold')
        pyplot.xlabel(x_label, size=10, weight='bold')
        pyplot.ylabel(y_label, size=10, weight='bold')

    elif kind == seaborn.barplot:
        ax = kind(data=data, x=x_arg, y=y_arg, hue=hue, color=color)
        pyplot.title(title, size=12, weight='bold')
        pyplot.xlabel(x_label, size=10, weight='bold')
        pyplot.ylabel(y_label, size=10, weight='bold')  
        if annot:    
            for p in ax.patches:
                ax.annotate('{:.3f}%'.format((p.get_height() / data[col].sum() * 100)),
                            (p.get_x() + 0.2, p.get_height() + 1), ha='left', va='bottom', size=12)

    elif kind == seaborn.histplot:
        seaborn.histplot(data=data, x=x_arg, bins=bin_size)
        pyplot.title(title, size = 12, weight='bold')
        pyplot.xlabel(x_label, size=10, weight='bold')
        pyplot.ylabel(y_label, size=10, weight='bold')

    elif kind == seaborn.countplot:
        if y_arg == None:
            ax = seaborn.countplot(data = data, x = x_arg, color = seaborn.color_palette()[0], order = order)
            pyplot.title(title, size = 12, weight = 'bold')
            pyplot.xlabel(x_label, size = 10, weight = 'bold')
            pyplot.ylabel(y_label, size = 10, weight = 'bold')
            for p in ax.patches:
                ax.annotate('{:.3f}%'.format((p.get_height()/data.shape[0] * 100)), (p.get_x()+0.2, p.get_height()+1),
                    ha = 'left', va = 'bottom', size = 12)  
        elif x_arg == None:
            ay = seaborn.countplot(data = data, y = y_arg, color = seaborn.color_palette()[0], order = order)
            pyplot.title(title, size = 12, weight = 'bold')
            pyplot.xlabel(x_label, size = 10, weight = 'bold')
            pyplot.ylabel(y_label, size = 10, weight = 'bold')
            for p in ay.patches:
                ay.annotate('{:.3f}%'.format((p.get_width()/data.shape[0]) * 100),
                            (p.get_x() + p.get_width() + 0.02, p.get_y() + p.get_height()/2), size = 12)
    
    else:
        kind(data=data, x=x_arg, y=y_arg, hue=hue, color=color)
        pyplot.title(title, size=12, weight='bold')
        pyplot.xlabel(x_label, size=10, weight='bold')
        pyplot.ylabel(y_label, size=10, weight='bold')
