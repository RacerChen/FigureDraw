import plotly.graph_objects as go
import pandas as pd

# 导入数据
df = pd.read_excel('jdb_distribution.xlsx', sheet_name='Sheet1')

print(df)

fig = go.Figure(data=go.Choropleth(
    locations=df['abbr'],  # 设置位置，各州的编号（缩写）
    z=df['locations'].astype(float),  # 设置填充色数据
    text=df['state'],
    locationmode='USA-states',  # 设置国家名称
    colorscale='earth',  # 图例颜色
    colorbar_title="店数",  # 图例标题
))

fig.update_layout(
    title_text='家得宝美国门店分布',  # 地图标题
    geo_scope='usa',  # 设置地图的范围为美国
    # scope可选有"world"，"usa"，"europe"，"asia"，"africa"，"north america"，"south america"
)

# fig.show()

# 将地图导出为html文件
fig.write_html("US.html")
