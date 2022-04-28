import time
import plotly.graph_objects as go

def plot(values):
    fig = go.Figure()
    fig.add_trace(go.Barpolar(r=values))
    fig.update_layout(
        polar=dict(
            angularaxis=dict(
                direction="clockwise",
            )
        )
    )
    # fig.show()
    fig.write_image("seer" + str(time.time()) + ".png")
