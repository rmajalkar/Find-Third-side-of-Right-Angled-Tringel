import streamlit as st
import math

st.title("📐 Pythagoras Theorem Calculator")

st.write("Find the third side of a right-angled triangle.")

option = st.selectbox(
    "What do you want to calculate?",
    ["Hypotenuse", "Side A", "Side B"]
)

if option == "Hypotenuse":
    a = st.number_input("Enter Side A", min_value=0.0)
    b = st.number_input("Enter Side B", min_value=0.0)

    if st.button("Calculate"):
        c = math.sqrt(a**2 + b**2)
        st.success(f"Hypotenuse = {c:.2f}")

elif option == "Side A":
    c = st.number_input("Enter Hypotenuse", min_value=0.0)
    b = st.number_input("Enter Side B", min_value=0.0)

    if st.button("Calculate"):
        if c > b:
            a = math.sqrt(c**2 - b**2)
            st.success(f"Side A = {a:.2f}")
        else:
            st.error("Hypotenuse must be greater than Side B")

elif option == "Side B":
    c = st.number_input("Enter Hypotenuse", min_value=0.0)
    a = st.number_input("Enter Side A", min_value=0.0)

    if st.button("Calculate"):
        if c > a:
            b = math.sqrt(c**2 - a**2)
            st.success(f"Side B = {b:.2f}")
        else:
            st.error("Hypotenuse must be greater than Side A")
