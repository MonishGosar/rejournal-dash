import mysql.connector
from mysql.connector import Error
import pandas as pd

def get_tenant_sector_data():
    try:
        connection = mysql.connector.connect(
            host='193.203.184.1',
            user='u661384233_dbuser',
            password='Rejournal@123',
            database='u661384233_rejournal'
        )

        if connection.is_connected():
            query = """
            SELECT tenant_sector, SUM(area_transcatedsq_ft) as total_area 
            FROM leases 
            WHERE tenant_sector IS NOT NULL AND tenant_sector != '' 
            GROUP BY tenant_sector 
            ORDER BY total_area DESC

            """
            
            df = pd.read_sql(query, connection)
            
            # Check if the dataframe is empty
            if df.empty:
                print("No data returned from the query.")
                return []
            
            # Calculate the total area
            total_area = df['total_area'].sum()
            
            # Check if total_area is zero
            if total_area == 0:
                print("Total area is zero. Cannot calculate percentages.")
                return []
            
            # Calculate the percentage and format the data for the pie chart
            chart_data = df.apply(lambda row: {
                "id": row['tenant_sector'],
                "label": row['tenant_sector'],
                "value": round(row['total_area'] / total_area * 100, 2),
                "color": f"hsl({hash(row['tenant_sector']) % 360}, 70%, 50%)"
            }, axis=1).tolist()
            
            return chart_data

    except Error as e:
        print(f"Error: {e}")
        return []

    finally:
        if connection.is_connected():
            connection.close()