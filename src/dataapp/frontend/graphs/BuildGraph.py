import streamlit as st
import time
from graphs.FilterGraphs import FilterGraphs
from graphs.Graphs import Graphs
from config.RequestsToBackend import RequestsToBackend

class BuildGraph():
    @staticmethod
    def render_graph(view_table, view_name, metro_line):
        graph_fn = Graphs.get_graph(view_table)
        if graph_fn:
            view_filter = ''
            filter_fn = FilterGraphs.get_filter(view_table)
            if filter_fn:
                view_filter = filter_fn(metro_line=metro_line)
            data = RequestsToBackend.get_view_data(view_table=view_table, view_filter=view_filter)
            if not data.empty:
                graph = graph_fn(data)
                try:
                    st.pyplot(graph) 
                except:
                     st.plotly_chart(graph, key=f"_{time.time()}")
