import pandas as pd
import matplotlib.pyplot as plt
from decorators.add_table_fn import add_table_fn, table_fns
import plotly.express as px

class Graphs():
    @staticmethod
    def get_graph(view_name):
        return table_fns.get("graph", {}).get(view_name)

    @staticmethod
    @add_table_fn("graph", "pcd")
    def pcd_graph(data):
        data_sorted = data.sort_values(by="total_qtde_pcd", ascending=False)
        pink_palette = ["#FAD0C4", "#F9A8D4", "#F072A2", "#D83C7C", "#D5006D"]
        fig = px.bar(data_sorted,
                    x="grupos_pcd", 
                    y="total_qtde_pcd",
                    title="Quantidade Total de PCD por Grupo",
                    labels={"grupos_pcd": "Grupo PCD", "total_qtde_pcd": "Quantidade Total"},
                    color="total_qtde_pcd", 
                    color_continuous_scale=pink_palette, 
                    text="total_qtde_pcd" 
                    )
        fig.update_xaxes(tickangle=45)
        fig.update_layout(
            title_font=dict(size=18, color="white", family="Arial, sans-serif"),
            xaxis_title_font=dict(size=18, color="white", family="Arial, sans-serif"),
            yaxis_title_font=dict(size=18, color="white", family="Arial, sans-serif"),
            font=dict(size=14, color="white"),
            plot_bgcolor="rgba(0,0,0,0)",  
            paper_bgcolor="rgba(0,0,0,0)", 
        )
        return fig
    
    @staticmethod
    @add_table_fn("graph", "passag_per_tipo_dia")
    def mov_periodo_graph(data):
        df_grouped = data.groupby("tipo_dia")["total_validacoes"].sum().reset_index()
        df_grouped = df_grouped.sort_values(by="total_validacoes", ascending=False)
        pink_palette = ["#D5006D", "#F072A2", "#F9A8D4", "#FAD0C4"]
        fig = px.pie(
            df_grouped,
            values='total_validacoes',
            names='tipo_dia',
            color_discrete_sequence=pink_palette,
            labels={"tipo_dia": "Tipo de Dia", "total_validacoes": "Total de Validações"},
            title="Distribuição de Validações por Tipo de Dia"
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        return fig

    @staticmethod
    @add_table_fn("graph", "totalValidacoesPerDia")
    def total_validacoes_dia(data):
        pink_palette = ["#FDDDE6", "#FCE8F3",
            "#FBE4F0", "#FAD0C4", "#F9A8D4",
            "#F072A2", "#D83C7C", "#D5006D",
            "#C20055", "#B22257"]
        data['Data'] = pd.to_datetime(data['Data'], format="%a, %d %b %Y %H:%M:%S %Z")
        data['Data'] = data['Data'].dt.strftime("%a, %d %b %Y")
        data = data.groupby("Data")["total_validacoes_por_dia"].sum().reset_index()
        fig = px.bar(
            data,  
            x="Data",  
            y="total_validacoes_por_dia", 
            labels={"Data": "Data", "total_validacoes_por_dia": "Total de Validações"},
            title="Total de Validações por Dia",
            color = "total_validacoes_por_dia",
            color_continuous_scale=pink_palette 
        )
        fig.update_xaxes(title_text="Data")
        fig.update_yaxes(title_text="Total de Validações")
        return fig

    @staticmethod
    @add_table_fn("graph", "pcd_hora_linha")
    def pcd_hora_linha_graph(data):
        if not pd.api.types.is_datetime64_any_dtype(data['data']):
            try:
                data['data'] = pd.to_datetime(data['data'])
            except Exception as e:
                raise ValueError(f"Erro ao converter a coluna 'data' para datetime: {e}")
        data['data'] = data['data'].dt.strftime('%a, %d %b %Y')
        fig = px.density_heatmap(
            data, 
            x='horario', 
            y='data', 
            z='total_qtde_pcd', 
            color_continuous_scale='rdpu', 
            labels={'horario': 'Hora', 'data': 'Data', 'total_qtde_pcd': 'Quantidade PCD'}
        )
        fig.update_layout(
            xaxis=dict(title='Hora', type='category', categoryorder='array', categoryarray=list(range(24))),  
            yaxis=dict(title='Data', type='category', categoryorder='array', categoryarray=data['data'].unique()),
            title="Heatmap de Quantidade PCD por Horário e Data",
            coloraxis_colorbar=dict(title='Quantidade PCD')
        )
        fig.update_traces(
            customdata=data['semana'],
            hovertemplate='<b>%{y}</b><br>Hora: %{x} <br>Total PCDs: %{z}<extra></extra>',
        )
        return fig
    
    @staticmethod
    @add_table_fn("graph", "bilh_tipo_dia")
    def bilh_tipo_dia_graph(data):
        data_grouped = data.groupby('tipo_bilhete')['total_uso'].sum().reset_index()
        pink_palette = ["#FAD0C4", "#F9A8D4", "#F072A2", "#D83C7C", "#D5006D"]
        data_sorted = data_grouped.sort_values(by='total_uso', ascending=True) 
        fig = px.bar(
            data_sorted,
            color_continuous_scale=pink_palette, 
            y='tipo_bilhete', 
            x='total_uso', 
            labels={'tipo_bilhete': 'Tipo de Bilhete', 'total_uso': 'Total de Uso'},
            title='Tipos de Bilhete por Dia',
            color='total_uso', 
            text='total_uso',
            orientation='h' 
        )
        fig.update_layout(
            title_font=dict(size=18, color="white", family="Arial, sans-serif"),
            xaxis_title_font=dict(size=18, color="white", family="Arial, sans-serif"),
            yaxis_title_font=dict(size=18, color="white", family="Arial, sans-serif"),
            font=dict(size=14, color="white"),
            plot_bgcolor="rgba(0,0,0,0)",  
            paper_bgcolor="rgba(0,0,0,0)", 
        )
        return fig
