import streamlit as st
import requests
st.title(
	"SuperKart Sales Forecasting"
)
product_weight = st.number_input(
	"Product Weight",
	min_value=0.0
)
allocated_area = st.number_input(
	"Allocated Area",
	min_value=0.0
)
product_mrp = st.number_input(
	"Product MRP",
	min_value=0.0
)
if st.button("Predict Sales"):
	payload = {

    "Product_Weight":
    product_weight,

    "Product_Sugar_Content":
    "Low Sugar",

    "Product_Allocated_Area":
    allocated_area,

    "Product_Type":
    "Frozen Foods",

    "Product_MRP":
    product_mrp,

    "Store_Size":
    "Medium",

    "Store_Location_City_Type":
    "Tier 2",

    "Store_Type":
    "Supermarket Type2",

    "Product_Id_char":
    "FD",

    "Store_Age_Years":
    16,

    "Product_Type_Category":
    "Perishables"
}
	response = requests.post(
    	"http://backend:7860/v1/predict",
    	json=payload
	)
	result = response.json()
	st.success(
    	f"Predicted Sales = {result['predicted_sales']:.2f}"
	)

