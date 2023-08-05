# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:05:57 2022

@author: Tyler
"""
import numpy as np
import matplotlib as mpl
import networkx.drawing.nx_pylab as nxp
from viswaternet.network import processing
from viswaternet.utils import save_fig, normalize_parameter, unit_conversion
from viswaternet.drawing import base


default_cmap = mpl.cm.get_cmap("autumn_r")


def draw_nodes(
    self,
    ax,
    node_list,
    parameter_results=None,
    vmin=None,
    vmax=None,
    node_size=None,
    node_color="k",
    cmap="tab10",
    node_shape=".",
    edge_colors="k",
    line_widths=0,
    label=None,
):
    model=self.model
    if parameter_results is None:
        parameter_results = []
    if node_size is None:
        node_size = []
    if len(parameter_results) != 0:

        negativeValues = False
    if isinstance(node_size, list) and len(node_size) == 0:

        node_size = np.ones(len(node_list)) * 100
    if isinstance(node_size, int):
        node_size = np.ones(len(node_list)) * node_size
    if len(parameter_results) != 0:
        for value in parameter_results:

            if value < -1e-5:

                negativeValues = True

                cmap = mpl.cm.get_cmap(cmap)

                if vmin is None and vmax is None:
                    g = nxp.draw_networkx_nodes(
                        model["G"],
                        model["pos_dict"],
                        ax=ax,
                        nodelist=node_list,
                        node_size=node_size,
                        node_color=parameter_results,
                        vmax=np.max(parameter_results),
                        vmin=-np.max(parameter_results),
                        cmap=cmap,
                        node_shape=node_shape,
                        linewidths=line_widths,
                        edgecolors=edge_colors,
                        label=label,
                    )
                else:
                    g = nxp.draw_networkx_nodes(
                        model["G"],
                        model["pos_dict"],
                        ax=ax,
                        nodelist=node_list,
                        node_size=node_size,
                        node_color=parameter_results,
                        vmax=vmax,
                        vmin=vmin,
                        cmap=cmap,
                        node_shape=node_shape,
                        linewidths=line_widths,
                        edgecolors=edge_colors,
                        label=label,
                    )
                return g
        if negativeValues:
            pass
        else:
            cmap = mpl.cm.get_cmap(cmap)

            if vmin is None and vmax is None:
                g = nxp.draw_networkx_nodes(
                    model["G"],
                    model["pos_dict"],
                    ax=ax,
                    nodelist=node_list,
                    node_size=node_size,
                    node_color=parameter_results,
                    cmap=cmap,
                    node_shape=node_shape,
                    linewidths=line_widths,
                    edgecolors=edge_colors,
                )
            else:
                g = nxp.draw_networkx_nodes(
                    model["G"],
                    model["pos_dict"],
                    ax=ax,
                    nodelist=node_list,
                    node_size=node_size,
                    node_color=parameter_results,
                    cmap=cmap,
                    node_shape=node_shape,
                    linewidths=line_widths,
                    edgecolors=edge_colors,
                    vmin=vmin,
                    vmax=vmax,
                )
            return g
    else:

        nxp.draw_networkx_nodes(
            model["G"],
            model["pos_dict"],
            ax=ax,
            nodelist=node_list,
            node_size=node_size,
            node_color=node_color,
            node_shape=node_shape,
            edgecolors=edge_colors,
            linewidths=line_widths,
            label=label,
        )


def draw_links(
    self,
    ax,
    link_list,
    parameter_results=None,
    edge_color="k",
    cmap="tab10",
    widths=None,
    vmin=None,
    vmax=None,
    link_style='-',
    link_arrows=False
):
    model=self.model
    if parameter_results is None:
        parameter_results = []
    if widths is None:
        widths = []
    
    if isinstance(widths, list) and len(widths) == 0:

        widths = np.ones(len(widths)) * 100
        
    if isinstance(widths, int):
        widths = np.ones(len(link_list)) * widths
        
    edgeList = {}

    if len(widths) == 0:

        widths = np.ones(len(link_list)) * 1
    negativeValues = False

    if len(parameter_results) != 0:
        for i in link_list:
            edgeList[i] = model["G_pipe_name_list"].index(i)
        for value in parameter_results:

            if value < -1e-5:

                negativeValues = True

                cmap = mpl.cm.get_cmap(cmap)

                if vmin is None and vmax is None:
                    g = nxp.draw_networkx_edges(
                        model["G"],
                        model["pos_dict"],
                        ax=ax,
                        edgelist=([model["pipe_list"][i] for i in edgeList.values()]),
                        edge_color=parameter_results,
                        edge_vmax=np.max(parameter_results),
                        edge_vmin=-np.max(parameter_results),
                        edge_cmap=cmap,
                        style=link_style,
                        arrows=link_arrows,
                        width=widths,
                    )
                else:
                    g = nxp.draw_networkx_edges(
                        model["G"],
                        model["pos_dict"],
                        ax=ax,
                        edgelist=([model["pipe_list"][i] for i in edgeList.values()]),
                        edge_color=parameter_results,
                        edge_vmax=vmax,
                        edge_vmin=vmin,
                        edge_cmap=cmap,
                        style=link_style,
                        arrows=link_arrows,
                        width=widths,
                    )
                return g
        if negativeValues:
            pass
        else:
            cmap = mpl.cm.get_cmap(cmap)

            if vmin is None and vmax is None:
                g = nxp.draw_networkx_edges(
                    model["G"],
                    model["pos_dict"],
                    ax=ax,
                    edgelist=([model["pipe_list"][i] for i in edgeList.values()]),
                    edge_color=parameter_results,
                    edge_cmap=cmap,
                    style=link_style,
                    arrows=link_arrows,
                    width=widths,
                )
            else:
                g = nxp.draw_networkx_edges(
                    model["G"],
                    model["pos_dict"],
                    ax=ax,
                    edgelist=([model["pipe_list"][i] for i in edgeList.values()]),
                    edge_color=parameter_results,
                    edge_cmap=cmap,
                    style=link_style,
                    arrows=link_arrows,
                    width=widths,
                    edge_vmin=vmin,
                    edge_vmax=vmax
                )
            return g
    else:
        for i in link_list:
            edgeList[i] = model["G_pipe_name_list"].index(i)
        nxp.draw_networkx_edges(
            model["G"],
            model["pos_dict"],
            ax=ax,
            edgelist=([model["pipe_list"][i] for i in edgeList.values()]),
            edge_color=edge_color,
            style=link_style,
            arrows=link_arrows,
            width=widths,
        )


def plot_continuous_nodes(
    self,
    ax,
    parameter=None,
    element_list=None,
    value=None,
    unit=None,
    vmin=None,
    vmax=None,
    get_tanks=False,
    get_reservoirs=False,
    tanks=True,
    reservoirs=True,
    pumps=True,
    valves=True,
    cmap=default_cmap,
    color_bar_title=None,
    node_size=100,
    min_size=100,
    max_size=100,
    node_shape=".",
    edge_colors=None,
    line_widths=None,
    legend=True,
    legend_loc="upper right",
    legend_title=None,
    savefig=True,
    save_name=None,
    dpi='figure',
    save_format='png',
    font_size=15,
    font_color='k',
    legend_title_font_size=17,
    draw_frame=False,
    legend_sig_figs=3,
    element_size_intervals=None,
    element_size_legend_title=None,
    element_size_legend_loc=None,
    element_size_legend_labels=None,
    draw_base_legend=True,
    draw_intervals_legend=True,
    reservoir_size=150,
    reservoir_color='b',
    reservoir_shape='s',
    reservoir_border_color='k',
    reservoir_border_width=3,
    tank_size=200,
    tank_color='b',
    tank_shape='h',
    tank_border_color='k',
    tank_border_width=2,
    valve_size=200,
    valve_color='orange',
    valve_shape='P',
    valve_border_color='k',
    valve_border_width=1,
    pump_color='b',
    pump_width=3,
    pump_line_style='-',
    pump_arrows=False,
    base_node_color='k',
    base_node_size=30,
    base_link_color='k',
    base_link_width=1,
    base_link_line_style='-',
    base_link_arrows=False,
    draw_color_bar=True,
):
    """Plots continuous Nodes.
    Arguments:
    figsize: Figure size. Takes a 2-element List.
    parameter: Takes String. The name of the parameter.
    value: Takes Integer. Parameters from results must include a value
    with it. The value given is the value index, not time.
    reservoirs: Takes Boolean. Determines whether to draw reservoirs or not.
    tanks: Takes Boolean. Determines whether to draw tanks or not.
    pumps: Takes Boolean. Determines whether to draw pumps or not.
    valves: Takes Boolean. Determines whether to draw valves or not.
    legend: Takes Boolean. Determines whether to draw legend or not.
    legend_title: Takes string. Title of legend.
    legend_loc_1: Takes String. Location of legend.
    savefig: Takes Boolean. Determines if figure is saved or not.
    save_name: Takes string. SaveName acts as a prefix for the image file name,
    and is followed by the name of the network.
    specialData: Takes either Excel file or correctly formatted dictionary.
    Used to plot custom data."""

    if parameter is not None:

        parameter_results, node_list = processing.get_parameter(
            self,
            "node",
            parameter,
            value=value,
            element_list=element_list,
            tanks=get_tanks,
            reservoirs=get_reservoirs,
        )

        if unit is not None:
            parameter_results = unit_conversion(parameter_results, parameter, unit)
        if min_size is not None and max_size is not None:
            normalized_parameter = normalize_parameter(
                parameter_results, min_size, max_size
            )

            node_size = normalized_parameter
            
        g = draw_nodes(
            self,
            ax,
            node_list,
            parameter_results=parameter_results,
            vmin=vmin,
            vmax=vmax,
            node_size=node_size,
            cmap=cmap,
            node_shape=node_shape,
            edge_colors=edge_colors,
            line_widths=line_widths,
        )

        base.draw_base_elements(
            self,
            ax,
            nodes=False,
            reservoirs=reservoirs,
            tanks=tanks,
            valves=valves,
            pumps=pumps,
            reservoir_size=reservoir_size,
            reservoir_color=reservoir_color,
            reservoir_shape=reservoir_shape,
            reservoir_border_color=reservoir_border_color,
            reservoir_border_width=reservoir_border_width,
            tank_size=tank_size,
            tank_color=tank_color,
            tank_shape=tank_shape,
            tank_border_color=tank_border_color,
            tank_border_width=tank_border_width,
            valve_size=valve_size,
            valve_color=valve_color,
            valve_shape=valve_shape,
            valve_border_color=valve_border_color,
            valve_border_width=valve_border_width,
            pump_color=pump_color,
            pump_width=pump_width,
            pump_line_style=pump_line_style,
            pump_arrows=pump_arrows,
            base_node_color=base_node_color,
            base_node_size=base_node_size,
            base_link_color=base_link_color,
            base_link_width=base_link_width,
            base_link_line_style=base_link_line_style,
            base_link_arrows=base_link_arrows
        )
        if draw_color_bar == True:
            base.draw_color_bar(ax, g, cmap, color_bar_title=color_bar_title)
    if legend:

        base.draw_legend(ax, 
                         title=legend_title, 
                         pumps=pumps, 
                         loc=legend_loc,
                         font_size=font_size,
                         font_color=font_color,
                         legend_title_font_size=legend_title_font_size,
                         draw_frame=draw_frame,
                         pump_color=pump_color,
                         base_link_color=base_link_color,
                         node_sizes=node_size,
                         element_size_intervals=element_size_intervals,
                         element_size_legend_title=element_size_legend_title,
                         element_size_legend_loc=element_size_legend_loc,
                         element_size_legend_labels=element_size_legend_labels,
                         draw_base_legend= draw_base_legend,
                         draw_intervals_legend=draw_intervals_legend,
                         linewidths=line_widths,
                         edge_colors=edge_colors,
                         )
    if savefig:

        save_fig(self, save_name=save_name,dpi=dpi,save_format=save_format)


def plot_continuous_links(
    self,
    ax,
    parameter=None,
    element_list=None,
    value=None,
    unit=None,
    widths=1,
    min_width=1,
    max_width=1,
    vmin=None,
    vmax=None,
    link_style='-',
    link_arrows=False,
    tanks=True,
    reservoirs=True,
    pumps=True,
    valves=True,
    cmap=default_cmap,
    color_bar_title=None,
    legend=True,
    legend_loc="upper right",
    legend_title=None,
    savefig=True,
    save_name=None,
    dpi='figure',
    save_format='png',
    font_size=15,
    font_color='k',
    legend_title_font_size=17,
    draw_frame=False,
    legend_sig_figs=3,
    link_sizes=None,
    element_size_intervals=None,
    element_size_legend_title=None,
    element_size_legend_loc=None,
    element_size_legend_labels=None,
    draw_base_legend=True,
    draw_intervals_legend=True,
    reservoir_size=150,
    reservoir_color='b',
    reservoir_shape='s',
    reservoir_border_color='k',
    reservoir_border_width=3,
    tank_size=200,
    tank_color='b',
    tank_shape='h',
    tank_border_color='k',
    tank_border_width=2,
    valve_size=200,
    valve_color='orange',
    valve_shape='P',
    valve_border_color='k',
    valve_border_width=1,
    pump_color='b',
    pump_width=3,
    pump_line_style='-',
    pump_arrows=False,
    base_node_color='k',
    base_node_size=30,
    base_link_color='k',
    base_link_width=1,
    base_link_line_style='-',
    base_link_arrows=False,
    draw_color_bar=True,
):

    if parameter is not None:

        parameter_results, link_list = processing.get_parameter(
            self, "link", parameter, value=value,element_list=element_list
        )

        if unit is not None:
            parameter_results = unit_conversion(parameter_results, parameter, unit)
        normalized_parameter = normalize_parameter(
            parameter_results, min_width, max_width
        )

        widths = normalized_parameter

        g = draw_links(
            self,
            ax,
            link_list,
            parameter_results=parameter_results,
            cmap=cmap,
            widths=widths,
            vmin=vmin,
            vmax=vmax,
            link_style=link_style,
            link_arrows=link_arrows,
        )

        base.draw_base_elements(
            self,
            ax,
            nodes=False,
            links=False,
            reservoirs=reservoirs,
            tanks=tanks,
            valves=valves,
            pumps=pumps,
            reservoir_size=reservoir_size,
            reservoir_color=reservoir_color,
            reservoir_shape=reservoir_shape,
            reservoir_border_color=reservoir_border_color,
            reservoir_border_width=reservoir_border_width,
            tank_size=tank_size,
            tank_color=tank_color,
            tank_shape=tank_shape,
            tank_border_color=tank_border_color,
            tank_border_width=tank_border_width,
            valve_size=valve_size,
            valve_color=valve_color,
            valve_shape=valve_shape,
            valve_border_color=valve_border_color,
            valve_border_width=valve_border_width,
            pump_color=pump_color,
            pump_width=pump_width,
            pump_line_style=pump_line_style,
            pump_arrows=pump_arrows,
            base_node_color=base_node_color,
            base_node_size=base_node_size,
            base_link_color=base_link_color,
            base_link_width=base_link_width,
            base_link_line_style=base_link_line_style,
            base_link_arrows=base_link_arrows
        )
        if draw_color_bar == True:
            base.draw_color_bar(ax, g, cmap, color_bar_title=color_bar_title)
        
    if legend:

        base.draw_legend(ax, 
                         title=legend_title, 
                         pumps=pumps, 
                         loc=legend_loc,
                         font_size=font_size,
                         font_color=font_color,
                         legend_title_font_size=legend_title_font_size,
                         draw_frame=draw_frame,
                         pump_color=pump_color,
                         base_link_color=base_link_color,
                         link_sizes=widths,
                         element_size_intervals=element_size_intervals,
                         element_size_legend_title=element_size_legend_title,
                         element_size_legend_loc=element_size_legend_loc,
                         element_size_legend_labels=element_size_legend_labels,
                         draw_base_legend= draw_base_legend,
                         draw_intervals_legend=draw_intervals_legend
                         )
    if savefig:

        save_fig(self, save_name=save_name,dpi=dpi,save_format=save_format)
