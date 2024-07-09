import streamlit as st
from streamlit_elements import elements, dashboard, mui, nivo
from database_operations import get_tenant_sector_data

# Change page layout to wide
st.set_page_config(layout="wide")

# Create a side bar
with st.sidebar:
    st.title("REjournal")

# Define dashboard layout
layout = [
    dashboard.Item("pie_chart", 0, 0, 6, 4),
]

# Create a frame to display elements
with elements("demo"):
    # Create a new dashboard with the layout specified above
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        # Pie chart element
        with mui.Card(key="pie_chart", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Tenant Sector Share in Leasing", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                # Fetch data from the database
                tenant_sector_data = get_tenant_sector_data()
                
                if tenant_sector_data:
                    nivo.Pie(
                        data=tenant_sector_data,
                        margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
                        innerRadius=0.5,
                        padAngle=0.7,
                        cornerRadius=3,
                        activeOuterRadiusOffset=8,
                        borderWidth=1,
                        borderColor={ "from": "color", "modifiers": [ [ "darker", 0.2 ] ] },
                        arcLinkLabelsSkipAngle=10,
                        arcLinkLabelsTextColor="#333333",
                        arcLinkLabelsThickness=2,
                        arcLinkLabelsColor={ "from": "color" },
                        arcLabelsSkipAngle=10,
                        arcLabelsTextColor={ "from": "color", "modifiers": [ [ "darker", 2 ] ] },
                        legends=[
                            {
                                "anchor": "bottom",
                                "direction": "row",
                                "justify": False,
                                "translateX": 0,
                                "translateY": 56,
                                "itemsSpacing": 0,
                                "itemWidth": 100,
                                "itemHeight": 18,
                                "itemTextColor": "#999",
                                "itemDirection": "left-to-right",
                                "itemOpacity": 1,
                                "symbolSize": 18,
                                "symbolShape": "circle",
                                "effects": [
                                    {
                                        "on": "hover",
                                        "style": {
                                            "itemTextColor": "#000"
                                        }
                                    }
                                ]
                            }
                        ]
                    )
                else:
                    mui.Typography("No data available for the pie chart.")