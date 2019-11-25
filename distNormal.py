import plotly.express as px
tips = px.data.tips()
fig = px.histogram(tips, x="total_bill", y="tip", color="sex", marginal="rug",
                   hover_data=tips.columns, curve_type='normal')