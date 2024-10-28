import streamlit as st
from fpdf import FPDF
import base64
import os

# Initialize session state to store cart items and input values
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'customer_name' not in st.session_state:
    st.session_state.customer_name = ""
if 'customer_mobile' not in st.session_state:
    st.session_state.customer_mobile = ""
if 'category' not in st.session_state:
    st.session_state.category = "Select"
if 'subcategory' not in st.session_state:
    st.session_state.subcategory = "Select"
if 'quantity' not in st.session_state:
    st.session_state.quantity = 1
if 'price' not in st.session_state:
    st.session_state.price = 0

# Customer Section
st.header("Billing Software")
st.subheader("Customer Details")
st.session_state.customer_name = st.text_input("Customer Name", value=st.session_state.customer_name)
st.session_state.customer_mobile = st.text_input("Mobile Number", value=st.session_state.customer_mobile)

# Product Section
st.subheader("Product Details")

file_path = 'category.txt'
lines = []
with open(file_path, 'r') as file:
    for line in file:
        lines.append(line.strip())
mainCategoryList = ["Select"]+lines

# Product Category and Subcategory
st.session_state.category = st.selectbox("Select Category", mainCategoryList, index=mainCategoryList.index(st.session_state.category))






# Display subcategory options based on selected category
subcategory_options = []
if st.session_state.category == "All fancy":
    file_path = 'All_fancy.txt'
    lines01 = []
    with open(file_path, 'r') as file:
        for line01 in file:
            lines01.append(line01.strip())
    subcategory_options = lines01
elif st.session_state.category == "Bomb":
    file_path = 'Bomb.txt'
    lines02 = []
    with open(file_path, 'r') as file:
        for line02 in file:
            lines02.append(line02.strip())
    subcategory_options = lines02

elif st.session_state.category == "Chorsa":
    file_path = 'Chorsa.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "FP":
    file_path = 'FP.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "GC":
    file_path = 'GC.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "Kids":
    file_path = 'Kids.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "Kit Kat and Other":
    file_path = 'Kit_Kat.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "Lad":
    file_path = 'Lad.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "Matka Anar":
    file_path = 'Matka_Anar.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "Paper Bomb":
    file_path = 'Paper_Bomb.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "Rocket":
    file_path = 'Rocket.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "Sky Shot":
    file_path = 'Sky_Shot.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

elif st.session_state.category == "Sparkal":
    file_path = 'Sparkal.txt'
    lines03 = []
    with open(file_path, 'r') as file:
        for line03 in file:
            lines03.append(line03.strip())
    subcategory_options = lines03

# Determine index for subcategory selection
subcategory_index = subcategory_options.index(st.session_state.subcategory) + 1 if st.session_state.subcategory in subcategory_options else 0
st.session_state.subcategory = st.selectbox("Select Subcategory", ["Select"] + subcategory_options, index=subcategory_index)

# Quantity and Price Inputs
st.session_state.quantity = st.number_input("Quantity", min_value=1, value=st.session_state.quantity)
# st.session_state.price = st.number_input("Price", min_value=0.0, value=st.session_state.price, format="%.2f")
st.session_state.price = st.number_input("Price", min_value=0, value=st.session_state.price)

# Function to add item to cart
def add_to_cart():
    if st.session_state.category != "Select" and st.session_state.subcategory != "Select":
        item = {
            "Category": st.session_state.category,
            "Subcategory": st.session_state.subcategory,
            "Quantity": st.session_state.quantity,
            "Price": st.session_state.price,
            "Total": st.session_state.quantity * st.session_state.price
        }
        st.session_state.cart.append(item)
        st.success(f"Added {st.session_state.subcategory} to cart!")
    else:
        st.error("Please select both category and subcategory")

# Add to Cart Button
st.button("Add to Cart", on_click=add_to_cart)

# Display Cart
if st.session_state.cart:
    st.subheader("Cart")
    for item in st.session_state.cart:
        st.write(f"{item['Category']} - {item['Subcategory']}: {item['Quantity']} x {item['Price']} = {item['Total']}")

    # Total Amount Calculation
    total_amount = sum(item["Total"] for item in st.session_state.cart)
    st.write("Total Amount:", total_amount)

# PDF generation function
def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 12)

    # Customer details
    pdf.cell(200, 10, f"{'- Bill Reciept -'}", ln=True, align= 'C')
    pdf.cell(200, 10, f"Customer Name: {st.session_state.customer_name}", ln=True)
    pdf.cell(200, 10, f"Mobile Number: {st.session_state.customer_mobile}", ln=True)
    pdf.cell(200, 10, f"Total Amount: Rs. {total_amount}", ln=True)
    # Adding items
    pdf.cell(200, 10, "Items:", ln=True)
    for item in st.session_state.cart:
        pdf.cell(200, 10, f"{item['Category']} - {item['Subcategory']}: {item['Quantity']} x {item['Price']} = {item['Total']}", ln=True)

    # Save PDF
    pdf_output = f"{st.session_state.customer_name}_bill.pdf"
    pdf.output(pdf_output)
    
    # Encode PDF to base64 for download link
    with open(pdf_output, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        
    # Generate download link with print dialog trigger
    pdf_link = f'<a href="data:application/octet-stream;base64,{base64_pdf}" download="{pdf_output}" target="_blank" onclick="window.print();">Download & Print Bill</a>'
    st.markdown(pdf_link, unsafe_allow_html=True)
    
    # Cleanup: remove PDF file after generation
    # os.remove(pdf_output)

# Generate Bill Button
if st.button("Generate Bill"):
    if st.session_state.customer_name and st.session_state.customer_mobile and st.session_state.cart:
        generate_pdf()
    else:
        st.error("Please fill all customer details and add items to the cart")

# Reset Button
def reset():
    st.session_state.cart = []
    st.session_state.customer_name = ""
    st.session_state.customer_mobile = ""
    st.session_state.category = "Select"
    st.session_state.subcategory = "Select"
    st.session_state.quantity = 1
    st.session_state.price = 0
    st.success("All fields and cart reset successfully!")

st.button("Reset", on_click=reset)
