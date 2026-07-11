import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("used_car_price_model.pkl")

st.title("Used Car Price Prediction")

year = st.number_input("Year", 2000, 2026, 2020)
kilometer = st.number_input("Kilometers Driven", 0, 500000, 50000)

make = st.selectbox("Make", sorted(['Honda', 'Maruti Suzuki', 'Hyundai', 'Toyota', 'Mercedes-Benz',
       'BMW', 'Skoda', 'Nissan', 'Renault', 'Tata', 'Volkswagen', 'Ford',
       'Audi', 'Mahindra', 'MG', 'Jeep', 'Porsche', 'Kia', 'Land Rover',
       'Volvo', 'Maserati', 'Jaguar', 'Isuzu', 'Fiat', 'MINI', 'Ferrari',
       'Mitsubishi', 'Datsun', 'Lamborghini', 'Chevrolet', 'Ssangyong',
       'Rolls-Royce', 'Lexus'
]))

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "Electric", "CNG", "Hybrid"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

location = st.selectbox(
    "Location",
    ['Pune', 'Ludhiana', 'Lucknow', 'Mangalore', 'Mumbai', 'Coimbatore',
       'Bangalore', 'Delhi', 'Raipur', 'Kanpur', 'Patna', 'Vadodara',
       'Hyderabad', 'Yamunanagar', 'Gurgaon', 'Jaipur', 'Deoghar', 'Agra',
       'Goa', 'Warangal', 'Jalandhar', 'Noida', 'Ahmedabad', 'Mohali',
       'Navi Mumbai', 'Ghaziabad', 'Kolkata', 'Zirakpur', 'Nagpur',
       'Thane', 'Faridabad', 'Ranchi', 'Chandigarh', 'Amritsar',
       'Chennai', 'Udupi', 'Panvel', 'Jamshedpur', 'Aurangabad',
       'Rudrapur', 'Nashik', 'Varanasi', 'Salem', 'Dehradun', 'Valsad',
       'Haldwani', 'Dharwad', 'Surat', 'Indore', 'Karnal', 'Panchkula',
       'Mysore', 'Rohtak', 'Ambala Cantt', 'Samastipur', 'Unnao',
       'Purnea', 'Bhubaneswar', 'Kheda', 'Kollam', 'Meerut', 'Ernakulam',
       'Kharar', 'Mirzapur', 'Bhopal', 'Gorakhpur', 'Guwahati',
       'Allahabad', 'Muzaffurpur', 'Faizabad', 'Kota', 'Pimpri-Chinchwad',
       'Dak. Kannada', 'Ranga Reddy', 'Bulandshahar', 'Roorkee'
        # unique locations
    ]
)

color = st.selectbox(
    "Color",
    ['Grey', 'White', 'Maroon', 'Red', 'Blue', 'Orange', 'Silver',
       'Brown', 'Black', 'Bronze', 'Gold', 'Beige', 'Green', 'Yellow',
       'Purple', 'Others', 'Pink'
        # unique colors
    ]
)

owner = st.selectbox(
    "Owner",
    [
        "Unregistered",
        "First",
        "Second",
        "Third",
        "Fourth",
        "Four or More"
    ]
)

seller_type = st.selectbox(
    "Seller Type",
    ['Corporate', 'Individual', 'Commercial Registration'
        # unique seller types
    ]
)

drivetrain = st.selectbox(
    "Drivetrain",
    [
        "FWD",
        "RWD",
        "AWD"
    ]
)

engine = st.number_input("Engine (cc)", 500, 7000, 1500)
power = st.number_input("Power (bhp)", 20.0, 1000.0, 100.0)
power_rpm = st.number_input("Power RPM", 1000, 10000, 6000)

torque = st.number_input("Torque (Nm)", 20.0, 2000.0, 150.0)
torque_rpm = st.number_input("Torque RPM", 1000, 10000, 4000)

length = st.number_input("Length (mm)", 3000, 6000, 4300)
width = st.number_input("Width (mm)", 1200, 2500, 1700)
height = st.number_input("Height (mm)", 1000, 2500, 1500)

seating_capacity = st.number_input(
    "Seating Capacity",
    2,
    10,
    5
)

fuel_tank_capacity = st.number_input(
    "Fuel Tank Capacity",
    20.0,
    150.0,
    45.0
)

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        "Year": [year],
        "Kilometer": [kilometer],
        "Engine": [engine],
        "Power": [power],
        "Power rpm": [power_rpm],
        "Torque": [torque],
        "Torque rpm": [torque_rpm],
        "Length": [length],
        "Width": [width],
        "Height": [height],
        "Seating Capacity": [seating_capacity],
        "Fuel Tank Capacity": [fuel_tank_capacity],
        "Make": [make],
        "Fuel Type": [fuel_type],
        "Transmission": [transmission],
        "Location": [location],
        "Color": [color],
        "Owner": [owner],
        "Seller Type": [seller_type],
        "Drivetrain": [drivetrain]
    })

    prediction = model.predict(input_df)[0]

    st.success(
        f"Estimated Price: ₹{prediction:,.2f}"
    )