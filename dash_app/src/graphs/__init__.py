from src.graphs.bar.graph import bar_plot
from src.graphs.box.graph import box_plot
from src.graphs.corr.graph import corr_plot
from src.graphs.histogram.graph import histogram_plot
from src.graphs.line.graph import line_plot
from src.graphs.map.graph import map_plot
from src.graphs.scatter.graph import scatter_plot

from src.graphs.scatter.components import scatter_components
from src.graphs.line.components import line_components
from src.graphs.bar.components import bar_components
from src.graphs.box.components import box_components
from src.graphs.corr.components import corr_components
from src.graphs.histogram.components import histogram_components
from src.graphs.map.components import map_components

from src.graphs.scatter.callbacks import init_callbacks_scatter
from src.graphs.line.callbacks import init_callbacks_line
from src.graphs.bar.callbacks import init_callbacks_bar
from src.graphs.box.callbacks import init_callbacks_box
from src.graphs.corr.callbacks import init_callbacks_corr
from src.graphs.histogram.callbacks import init_callbacks_histogram
from src.graphs.map.callbacks import init_callbacks_map


components = dict(
    scatter=scatter_components,
    line=line_components,
    bar=bar_components,
    box=box_components,
    corr=corr_components,
    histogram=histogram_components,
    map=map_components,
)
