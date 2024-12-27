import streamlit as st
import time
from datetime import date, timedelta
from decorators.add_table_fn import add_table_fn, table_fns

class FilterGraphs():
    @staticmethod
    def get_filter(view_table):
        return table_fns.get("filter", {}).get(view_table)
    
    @staticmethod
    @add_table_fn("filter", "pcd")
    def filter_pcd(**kwargs):
        if 'metro_line' in kwargs:
            view_filter = f"WHERE UPPER(pcd.tx_descr_linha) LIKE UPPER('{kwargs['metro_line']}%')"
        else:
            view_filter = ''
        return view_filter

    @staticmethod
    @add_table_fn("filter", "totalValidacoesPerDia")
    def filter_total_validations_day(**kwargs):
        with st.container():
            col1, col2 = st.columns(2)
            initial_init_date = date(2023, 10, 1)
            initial_end_date = date(2023, 10, 15)
            with col1:
                init_date = st.date_input("Data de início", value=initial_init_date, key=f"init_date_{kwargs.get('metro_line', 'default')}_{time.time()}")
            with col2:
                end_date = st.date_input("Data de fim", value=initial_end_date, key=f"end_date_{kwargs.get('metro_line', 'default')}_{time.time()}")

            filters  = []
            if init_date:
                filters.append(f"totalValidacoesPerDia.Data >= '{init_date}'")
            if end_date:
                filters.append(f"totalValidacoesPerDia.Data <= '{end_date}'")
            view_filter = "WHERE " + " AND ".join(filters) + " ORDER BY totalValidacoesPerDia.Data DESC"
            return view_filter
        
    @staticmethod
    @add_table_fn("filter", "pcd_hora_linha")
    def filter_pcd_hora_linha(**kwargs):
        with st.container():
            col1, col2 = st.columns(2)
            initial_init_date = date(2023, 11, 1)
            initial_end_date = date(2023, 11, 6)
            with col1:
                init_date = st.date_input("Data de início", value=initial_init_date, key=f"init_date_pcd_hora_linha{kwargs.get('metro_line', 'default')}_{time.time()}")
                initial_end_date = init_date + timedelta(days=5)
            with col2:
                end_date = st.date_input("Data de fim", value=initial_end_date, key=f"end_date_pcd_hora_linha{kwargs.get('metro_line', 'default')}_{time.time()}", disabled=True)

            filters  = []
            if init_date:
                filters.append(f"pcd_hora_linha.data >= '{init_date}'")
            if end_date:
                filters.append(f"pcd_hora_linha.data <= '{end_date}'")
        if 'metro_line' in kwargs:
            filters.append(f" UPPER(pcd_hora_linha.tx_descr_linha) LIKE UPPER('{kwargs['metro_line']}%')")
        view_filter = "WHERE " + " AND ".join(filters) + " ORDER BY pcd_hora_linha.data DESC"
        return view_filter
            