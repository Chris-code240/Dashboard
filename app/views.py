from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import plotly.graph_objects as go


@api_view(['GET'])
def home(request):
    
    # colors = ['lightslategray',] * 5
    # colors[1] = 'crimson'

    # fig = go.Figure(data=[go.Bar(
    #     x=['Feature A', 'Feature B', 'Feature C',
    #     'Feature D', 'Feature E'],
    #     y=[20, 14, 23, 25, 22],
    #     marker_color=colors # marker color can be a single color value or an iterable
    # )])
    # fig.update_layout(title_text='Least Used Feature')
    # chart = fig.to_html()

    """Run Impressions against sentiment"""
    # Impressions
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=months,
        # sentiment
        y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
        name='Primary Product',
        marker_color='indianred'
    ))
    fig.add_trace(go.Bar(
        x=months,
        y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
        name='Secondary Product',
        marker_color='lightsalmon'
    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    chart = fig.to_html()
    context = {"title":"Home","side":True,"nav":True,"chart":chart}
    return render(request, template_name='home.html',context=context)
# Create your views here.
