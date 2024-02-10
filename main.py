import streamlit as st
import pandas as pd

# Global variable to store the loaded data
data = None

# Function to get orders by customer ID
def get_orders_by_customer_id(customer_id):
    global data
    if data is None:
        load_data()
    if data is not None:
        orders = data[data['Customer ID'] == customer_id][['Customer Name', 'Order ID', 'Product Name', 'Order Date']]
        return orders
    else:
        return pd.DataFrame()

# Function to get ship date and order date by order ID
def get_dates_by_order_id(order_id):
    global data
    if data is None:
        load_data()
    if data is not None:
        order = data[data['Order ID'] == order_id]
        if not order.empty:
            return order[['Ship Date', 'Order Date']]
        else:
            return pd.DataFrame()
    else:
        return pd.DataFrame()

# Streamlit UI components
st.title("आदेश पुन: प्राप्ति प्रणाली")  # Title in Hindi

# Load the CSV data into a DataFrame
def load_data():
    global data
    try:
        data = pd.read_csv('/content/Orders.csv', encoding='latin1')   # Specify a different encoding if UTF-8 doesn't work
    except Exception as e:
        st.error(f"त्रुटि: सीएसवी फ़ाइल लोड करने में {e}")
        data = None

# Input box for user to enter customer ID or order ID
input_type = st.radio("इनपुट प्रकार का चयन करें:", ("ग्राहक आईडी", "आदेश आईडी"))  # Input type selection in Hindi
if input_type == "ग्राहक आईडी":
    input_value = st.text_input("ग्राहक आईडी दर्ज करें:")
else:
    input_value = st.text_input("आदेश आईडी दर्ज करें:")

# Button to retrieve orders or dates
if st.button("पुनः प्राप्त करें"):  # Button text in Hindi
    if input_value:
        if input_type == "ग्राहक आईडी":
            orders = get_orders_by_customer_id(int(input_value))
            if not orders.empty:
                st.write("ग्राहक आईडी के लिए आदेश:", input_value)
                st.write(orders)
            else:
                st.warning("ग्राहक आईडी के लिए कोई आदेश नहीं मिला:", input_value)
        else:
            dates = get_dates_by_order_id(int(input_value))
            if not dates.empty:
                st.write("आदेश आईडी के लिए तारीख़:", input_value)
                st.write(dates)
            else:
                st.warning("आदेश आईडी के लिए कोई आदेश नहीं मिला:", input_value)
    else:
        st.warning("कृपया पुनः प्राप्त करने से पहले कोई मान दर्ज करें।")  # Warning message in Hindi
    