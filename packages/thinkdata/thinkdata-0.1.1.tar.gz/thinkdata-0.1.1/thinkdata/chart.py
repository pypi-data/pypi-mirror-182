import networkx as nx
import matplotlib.pyplot as plt


def influence2alpha(influence):
    return min(abs(influence), 1)


def plot_influence_network(analyze_diff_result_df, min_influence=0, ax=None, fig=None):
    """
    基于MetricSystem的差异分析方法`analyze_diff`的结果，绘制指标之间的影响网络
    """

    G = nx.DiGraph()
    edge_color = []
    for _, row in analyze_diff_result_df.iterrows():
        if abs(row["influence"]) >= min_influence:
            G.add_node(row["source"], level=row["level"])
            if row["level"] == 1:
                G.add_node(row["target"], level=row["level"]-1)
            edge_label = f"{row['influence']}({row['relation']})"
            G.add_edge(row["source"], row["target"], label=edge_label)
            edge_color.append(
                (0, 0, 0, influence2alpha(abs(row["influence"]))))

    pos = nx.multipartite_layout(G, subset_key="level")

    if ax is not None:
        _ax = ax
    else:
        _, _ax = plt.subplots(figsize=(16, 5))
    nx.draw_networkx(G,
                     pos=pos,
                     with_labels=True,
                     arrows=True,
                     edge_color=edge_color,
                     width=2,
                     arrowsize=20,
                     font_family="Microsoft YaHei",
                     node_color="darkorange")
    edge_labels = {(s, t): label for s, t, label in G.edges.data("label")}
    nx.draw_networkx_edge_labels(
        G,
        pos=pos,
        edge_labels=edge_labels,
        label_pos=0.5
    )
    _ax.set_axis_off()
    return _ax
