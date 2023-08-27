#Import streamlit
import streamlit as st

#Set the title of the app
st.title("Find the largest among 3 numbers")

# Get the input from the user
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)
num3 = st.number_input("Enter the third number", value=0)

#Define a function to find the largest number
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

#Call the function and display the result
largest = find_largest(num1, num2, num3)
st.write(f"The largest number is {largest}")
