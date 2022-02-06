from src.layout.graphs.style import component_style, transparent_plot

from src.layout.graphs.scatter import scatter_components
from src.layout.graphs.line import line_components
from src.layout.graphs.bar import bar_components
from src.layout.graphs.box import box_components
from src.layout.graphs.corr import corr_components
from src.layout.graphs.histogram import histogram_components
from src.layout.graphs.map import map_components


components = dict(
    scatter = scatter_components,
    line = line_components,
    bar = bar_components,
    box = box_components,
    corr = corr_components,
    histogram = histogram_components,
    map = map_components,
)
