# 代码生成时间: 2025-10-01 22:23:45
import streamlit as st
from streamlit.components.v1 import html, javascript
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import display, HTML

# Function to create a knowledge graph

def create_knowledge_graph(dataframe, title):
    """
    Creates a knowledge graph from a provided dataframe.
    Args:
        dataframe (pd.DataFrame): DataFrame containing the knowledge graph data.
        title (str): Title of the knowledge graph.
    """
    G = nx.Graph()
    for index, row in dataframe.iterrows():
        G.add_node(row['entity1'], label=row['entity1'])
        G.add_node(row['entity2'], label=row['entity2'])
        G.add_edge(row['entity1'], row['entity2'])

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=1500)
    nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")
    nx.draw_networkx_edges(G, pos, width=1.0)
    plt.title(title)
    plt.axis('off')
    plt.show()

# Streamlit setup
st.title('Knowledge Graph Builder')

# Input data for the knowledge graph
st.header('Input Data')
with st.form(key='data_form'):
    data = st.text_area('label', 'Paste your knowledge graph data here (CSV format)', height=300)
    submit_button = st.form_submit_button(label='Create Graph')

if submit_button and data:
    try:
        # Load the data into a pandas dataframe
        df = pd.read_csv(pd.compat.StringIO(data))

        # Validate the dataframe
        if 'entity1' not in df.columns or 'entity2' not in df.columns:
            st.error('The provided data must contain 