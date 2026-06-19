import pandas as pd

def calculate_kpis(df):

    total_revenue = df["TotalPrice"].sum()

    total_orders = df["InvoiceNo"].nunique()

    total_customers = df["CustomerID"].nunique()

    avg_order_value = total_revenue / total_orders

    return {
        "Revenue": total_revenue,
        "Orders": total_orders,
        "Customers": total_customers,
        "AOV": avg_order_value
    }