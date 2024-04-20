from altair import Chart, Tooltip


def chart(df, x, y, target) -> Chart:
    '''
    Takes in a pandas DataFrame with a selected 'x', 'y',
    and 'target' varibles and create a altair graph for visualization.

    Parameters:
    df: A Pandas DataFrame object
    x (string): Column for X-axis
    y (string): Column in Y-axis
    target (string): Column for the legend

    Returns:
    graph: An interactive altair graph
    '''

    # save the Chart() class to a variable name 'graph'
    graph = Chart(
        data=df,
        title=f"{y} by {x} for {target}"
        ).mark_circle(size=100).encode(
            x=x,
            y=y,
            color=target,
            tooltip=Tooltip(df.columns.to_list())
            ).properties(
                width=400,
                height=440,
                background="#252525",
                padding=40
            ).configure_axis(
                gridColor="#333333",
                labelColor="#AAAAAA",
                labelPadding=5,
                tickColor="#333333",
                tickSize=10,
                titleColor="#AAAAAA",
                titlePadding=20
            ).configure_legend(
                labelColor="#AAAAAA",
                padding=10,
                titleColor="#AAAAAA"
            ).configure_title(
                color="#AAAAAA",
                fontSize=26,
                offset=30
            ).configure_view(
                continuousHeight=300,
                continuousWidth=400,
                stroke="#333333"
            )

    # return altair graph
    return graph
