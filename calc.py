import streamlit as st

st.title("Simple Calculator 🔢")

# input numbers
num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

# operation select
operation = st.selectbox(
    "Choose Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# calculate button
if st.button("Calculate"):
    
    if operation == "Addition":
        result = num1 + num2
        
    elif operation == "Subtraction":
        result = num1 - num2
        
    elif operation == "Multiplication":
        result = num1 * num2
        
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    st.success(f"Result: {result}")