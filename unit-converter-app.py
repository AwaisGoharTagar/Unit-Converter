import streamlit as st # type: ignore

# Set page title and icon
st.set_page_config(page_title="Unit Converter App", page_icon="⚖")


st.markdown("<h2 style='color: #003092; font-size: 28px'>⚖ Welcome to Unit Converter App ⚖</h2>", unsafe_allow_html=True)

# Dropdown menu for selecting an option
from_unit = st.selectbox(
    "From:",
    ["Kilometer", "Meter", "Centimeter",  "Millimeter", "Micrometer", "Nanometer", 
      "Mile", "Yard", "Foot", "Inch", "Nautical Mile"],
    key='selectbox_from'
)
# Dropdown menu for selecting an option
to_unit = st.selectbox(
    "To:",
    ["Kilometer", "Meter", "Centimeter",  "Millimeter", "Micrometer", "Nanometer", 
      "Mile", "Yard", "Foot", "Inch", "Nautical Mile"],
    key='selectbox_to'
)

user_input1 = st.number_input("Enter Number:")

# logic for cm to mm
if from_unit == "Centimeter" and to_unit == "Millimeter":
    result = float(user_input1) * 10  
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for mm to cm
elif from_unit == "Millimeter" and to_unit == "Centimeter":
    result = float(user_input1) / 10
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for cm to km
elif from_unit == "Centimeter" and to_unit == "Kilometer":
    result = float(user_input1) / 100000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to cm
elif from_unit == 'Kilometer' and to_unit == 'Centimeter':
    result = float(user_input1) * 100000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for cm to ft
elif from_unit == 'Centimeter' and to_unit == 'Foot':
    result = float(user_input1) / 30.48
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to cm
elif from_unit == 'Foot' and to_unit == 'Centimeter':
    result = float(user_input1) * 30.48
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for cm to inch
elif from_unit == 'Centimeter' and to_unit == 'Inch':
    result = float(user_input1) / 2.54
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for inch to cm
elif from_unit == 'Inch' and to_unit == 'Centimeter':
    result = float(user_input1) * 2.54
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for mm to Km
elif from_unit == 'Millimeter' and to_unit == 'Kilometer':
    result = float(user_input1) / 1e+6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to mm
elif from_unit == 'Kilometer' and to_unit == 'Millimeter':
    result = float(user_input1) * 1e+6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for mm to ft
elif from_unit == 'Millimeter' and to_unit == 'Foot':
    result = float(user_input1) / 304.8
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to mm
elif from_unit == 'Foot' and to_unit == 'Millimeter':
    result = float(user_input1) * 304.8
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for mm to inch
elif from_unit == 'Millimeter' and to_unit == 'Inch':
    result = float(user_input1) / 25.4
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for Inch to mm
elif from_unit == 'Inch' and to_unit == 'Millimeter':
    result = float(user_input1) * 25.4
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for km to ft
elif from_unit == 'Kilometer' and to_unit == 'Foot':
    result = float(user_input1) * 3280.84
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to km
elif from_unit == 'Foot' and to_unit == 'Kilometer':
    result = float(user_input1) * 0.0003048
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for ft to Inch
elif from_unit == 'Foot' and to_unit == 'Inch':
    result = float(user_input1) * 12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for Inch to Foot
elif from_unit == 'Inch' and to_unit == 'Foot':
    result = float(user_input1) / 12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for km to Inch
elif from_unit == 'Kilometer' and to_unit == 'Inch':
    result = float(user_input1) * 39370.1
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for Inch to km
elif from_unit == 'Inch' and to_unit == 'Kilometer':
    result = float(user_input1) / 39370.1
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for cm to cm
elif from_unit == 'Centimeter' and to_unit == 'Centimeter':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for mm to mm
elif from_unit =='Millimeter' and to_unit =='Millimeter':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for km to km
elif from_unit =='Kilometer' and to_unit =='Kilometer':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for ft to ft
elif from_unit =='Foot' and to_unit =='Foot':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for Inch to Inch
elif from_unit =='Inch' and to_unit =='Inch':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for nm to mm
elif from_unit == 'Nautical Mile' and to_unit == 'Millimeter':
    result = float(user_input1) * 185200
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for mm to nm
elif from_unit == 'Millimeter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 185200
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to cm
elif from_unit == 'Nautical Mile' and to_unit == 'Centimeter':
    result = float(user_input1) * 1852000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for cm to nm
elif from_unit == 'Centimeter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to mm
elif from_unit == 'Nautical Mile' and to_unit == 'Millimeter':
    result = float(user_input1) * 185200
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for mm to nm
elif from_unit == 'Millimeter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 185200
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to in
elif from_unit == 'Nautical Mile' and to_unit == 'Inch':
    result = float(user_input1) * 6076
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for in to nm
elif from_unit == 'Inch' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to yd
elif from_unit == 'Nautical Mile' and to_unit == 'Yard':
    result = float(user_input1) * 6076.22
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yd to nm
elif from_unit == 'Yard' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.22
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to mile
elif from_unit == 'Nautical Mile' and to_unit == 'Mile':
    result = float(user_input1) * 1.15078
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to nm
elif from_unit == 'Mile' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.15078
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to cm
elif from_unit == 'Nautical Mile' and to_unit == 'Centimeter':
    result = float(user_input1) * 185200
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for cm to nm
elif from_unit == 'Centimeter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 185200
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to mm
elif from_unit == 'Nautical Mile' and to_unit == 'Millimeter':
    result = float(user_input1) * 1852000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for mm to nm
elif from_unit == 'Millimeter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)
    
# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nm
elif from_unit == 'Kilometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nautical Mile' and to_unit == 'Meter':
    result = float(user_input1) * 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nm
elif from_unit == 'Meter' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 1852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to ft
elif from_unit == 'Nautical Mile' and to_unit == 'Foot':
    result = float(user_input1) * 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for ft to nm
elif from_unit == 'Foot' and to_unit == 'Nautical Mile':
    result = float(user_input1) / 6076.12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nm to km
elif from_unit == 'Nautical Mile' and to_unit == 'Kilometer':
    result = float(user_input1) * 1.852
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to m
elif from_unit == 'Kilometer' and to_unit == 'Meter':   
    result = float(user_input1) * 1000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Meter<span>', unsafe_allow_html=True)
    
# logic for m to km
elif from_unit == 'Meter' and to_unit == 'Kilometer':
    result = float(user_input1) / 1000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to micrometer
elif from_unit == 'Kilometer' and to_unit == 'Micrometer':
    result = float(user_input1) * 1e+15
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for micrometer to km
elif from_unit == 'Micrometer' and to_unit == 'Kilometer':
    result = float(user_input1) / 1e+15
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to nanometer
elif from_unit == 'Kilometer' and to_unit == 'Nanometer':
    result = float(user_input1) * 1e+9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nanometer to km
elif from_unit == 'Nanometer' and to_unit == 'Kilometer':
    result = float(user_input1) / 1e+9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to mile
elif from_unit == 'Kilometer' and to_unit == 'Mile':
    result = float(user_input1) * 0.621371
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to km
elif from_unit == 'Mile' and to_unit == 'Kilometer':
    result = float(user_input1) / 0.621371
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for km to yard
elif from_unit == 'Kilometer' and to_unit == 'Yard':
    result = float(user_input1) * 1093.6133
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Kilometer is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yard to km
elif from_unit == 'Yard' and to_unit == 'Kilometer':
    result = float(user_input1) / 1093.6133
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Kilometer<span>', unsafe_allow_html=True)

# logic for m to m
elif from_unit == 'Meter' and to_unit == 'Meter':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to m
elif from_unit == 'Meter' and to_unit == 'Meter':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Meter<span>', unsafe_allow_html=True)
    
# logic for m to c
elif from_unit == 'Meter' and to_unit == 'Centimeter':
    result = float(user_input1) * 100
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for c to m
elif from_unit == 'Centimeter' and to_unit == 'Meter':
    result = float(user_input1) / 100
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to millimeter
elif from_unit == 'Meter' and to_unit == 'Millimeter':
    result = float(user_input1) * 1000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for mm to m
elif from_unit == 'Millimeter' and to_unit == 'Meter':
    result = float(user_input1) / 1000
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to microm
elif from_unit == 'Meter' and to_unit == 'Micrometer':
    result = float(user_input1) * 1e+6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for microm to m
elif from_unit == 'Micrometer' and to_unit == 'Meter':
    result = float(user_input1) / 1e+6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to nanometer
elif from_unit == 'Meter' and to_unit == 'Nanometer':
    result = float(user_input1) * 1e+9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nm to m
elif from_unit == 'Nanometer' and to_unit == 'Meter':
    result = float(user_input1) / 1e+9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to mile
elif from_unit == 'Meter' and to_unit == 'Mile':
    result = float(user_input1) * 0.000621371
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to m
elif from_unit == 'Mile' and to_unit == 'Meter':
    result = float(user_input1) / 0.000621371
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to yard
elif from_unit == 'Meter' and to_unit == 'Yard':
    result = float(user_input1) * 1.09361
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yard to m
elif from_unit == 'Yard' and to_unit == 'Meter':
    result = float(user_input1) / 1.09361
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to foot   
elif from_unit == 'Meter' and to_unit == 'Foot':
    result = float(user_input1) * 3.28084
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for foot to m
elif from_unit == 'Foot' and to_unit == 'Meter':
    result = float(user_input1) / 3.28084
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for m to inch
elif from_unit == 'Meter' and to_unit == 'Inch':
    result = float(user_input1) * 39.3701
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Meter is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for inch to m
elif from_unit == 'Inch' and to_unit == 'Meter':
    result = float(user_input1) / 39.3701
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Meter<span>', unsafe_allow_html=True)

# logic for centimeter to micrometer
elif from_unit == 'Centimeter' and to_unit == 'Micrometer':
    result = float(user_input1) * 1e-6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for micrometer to centimeter
elif from_unit == 'Micrometer' and to_unit == 'Centimeter':
    result = float(user_input1) * 1e-6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for centimeter to nanometer
elif from_unit == 'Centimeter' and to_unit == 'Nanometer':
    result = float(user_input1) * 1e-7
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nanometer to centimeter
elif from_unit == 'Nanometer' and to_unit == 'Centimeter':
    result = float(user_input1) * 1e-7
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for centimeter to mile
elif from_unit == 'Centimeter' and to_unit == 'Mile':
    result = float(user_input1) * 6.21371e-6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to centimeter
elif from_unit == 'Mile' and to_unit == 'Centimeter':
    result = float(user_input1) / 6.21371e-6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for centimeter to yard
elif from_unit == 'Centimeter' and to_unit == 'Yard':
    result = float(user_input1) * 0.0109361
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Centimeter is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yard to centimeter
elif from_unit == 'Yard' and to_unit == 'Centimeter':
    result = float(user_input1) / 0.0109361
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Centimeter<span>', unsafe_allow_html=True)

# logic for millimeter to microm
elif from_unit == 'Millimeter' and to_unit == 'Micrometer':
    result = float(user_input1) * 1e3
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for microm to millimeter
elif from_unit == 'Micrometer' and to_unit == 'Millimeter':
    result = float(user_input1) * 1e-6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for millimeter to nanometer
elif from_unit == 'Millimeter' and to_unit == 'Nanometer':
    result = float(user_input1) * 1e9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nanometer to millimeter
elif from_unit == 'Nanometer' and to_unit == 'Millimeter':
    result = float(user_input1) * 1e-9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for millimeter to mile
elif from_unit == 'Millimeter' and to_unit == 'Mile':
    result = float(user_input1) * 6.21371e-10
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to millimeter
elif from_unit == 'Mile' and to_unit == 'Millimeter':
    result = float(user_input1) / 6.21371e-10
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for millimeter to yard
elif from_unit == 'Millimeter' and to_unit == 'Yard':
    result = float(user_input1) * 0.00109361
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Millimeter is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yard to millimeter
elif from_unit == 'Yard' and to_unit == 'Millimeter':
    result = float(user_input1) / 0.00109361
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Millimeter<span>', unsafe_allow_html=True)

# logic for microm to microm
elif from_unit == 'Micrometer' and to_unit == 'Micrometer':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for microm to nanometer
elif from_unit == 'Micrometer' and to_unit == 'Nanometer':
    result = float(user_input1) * 1e3
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nanometer to micrometer
elif from_unit == 'Nanometer' and to_unit == 'Micrometer':
    result = float(user_input1) * 1e-6
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for micrometer to mile
elif from_unit == 'Micrometer' and to_unit == 'Mile':
    result = float(user_input1) * 6.21371e-13
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to micrometer
elif from_unit == 'Mile' and to_unit == 'Micrometer':
    result = float(user_input1) / 6.21371e-13
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for micrometer to yard
elif from_unit == 'Micrometer' and to_unit == 'Yard':
    result = float(user_input1) * 0.00000000109361
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yard to micrometer
elif from_unit == 'Yard' and to_unit == 'Micrometer':
    result = float(user_input1) / 0.00000000109361
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for micrometer to foot
elif from_unit == 'Micrometer' and to_unit == 'Foot':
    result = float(user_input1) * 0.0000000508002
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for foot to micrometer
elif from_unit == 'Foot' and to_unit == 'Micrometer':
    result = float(user_input1) / 0.0000000508002
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for micrometer to inch
elif from_unit == 'Micrometer' and to_unit == 'Inch':
    result = float(user_input1) * 0.000000155001
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for inch to micrometer
elif from_unit == 'Inch' and to_unit == 'Micrometer':
    result = float(user_input1) / 0.000000155001
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for micrometer to nautical mile
elif from_unit == 'Micrometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) * 5.39957e-12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Micrometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nautical mile to micrometer
elif from_unit == 'Nautical Mile' and to_unit == 'Micrometer':
    result = float(user_input1) / 5.39957e-12
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Micrometer<span>', unsafe_allow_html=True)

# logic for nanometer to nanometer
elif from_unit == 'Nanometer' and to_unit == 'Nanometer':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nanometer to mile
elif from_unit == 'Nanometer' and to_unit == 'Mile':
    result = float(user_input1) * 6.21371e-13
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to nanometer
elif from_unit == 'Mile' and to_unit == 'Nanometer':
    result = float(user_input1) / 6.21371e-13
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nanometer to yard
elif from_unit == 'Nanometer' and to_unit == 'Yard':
    result = float(user_input1) * 1.09361e-9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yard to nanometer
elif from_unit == 'Yard' and to_unit == 'Nanometer':
    result = float(user_input1) / 1.09361e-9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nanometer to foot
elif from_unit == 'Nanometer' and to_unit == 'Foot':
    result = float(user_input1) * 3.2808e-9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for foot to nanometer
elif from_unit == 'Foot' and to_unit == 'Nanometer':
    result = float(user_input1) / 3.2808e-9
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nanometer to inch
elif from_unit == 'Nanometer' and to_unit == 'Inch':
    result = float(user_input1) * 3.93701e-8
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for inch to nanometer
elif from_unit == 'Inch' and to_unit == 'Nanometer':
    result = float(user_input1) / 3.93701e-8
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for nanometer to nautical mile
elif from_unit == 'Nanometer' and to_unit == 'Nautical Mile':
    result = float(user_input1) * 3.60886e-14
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nanometer is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

# logic for nautical mile to nanometer
elif from_unit == 'Nautical Mile' and to_unit == 'Nanometer':
    result = float(user_input1) / 3.60886e-14
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Nanometer<span>', unsafe_allow_html=True)

# logic for  mile to mile
elif from_unit == 'Mile' and to_unit == 'Mile':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to yard
elif from_unit == 'Mile' and to_unit == 'Yard':
    result = float(user_input1) * 1760
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yard  to mile
elif from_unit == 'Yard' and to_unit == 'Mile':
    result = float(user_input1) / 1760
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to foot
elif from_unit == 'Mile' and to_unit == 'Foot':
    result = float(user_input1) * 5280
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for foot to mile
elif from_unit == 'Foot' and to_unit == 'Mile':
    result = float(user_input1) / 5280
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for mile to inch
elif from_unit == 'Mile' and to_unit == 'Inch':
    result = float(user_input1) * 63360
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Mile is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for inch to mile
elif from_unit == 'Inch' and to_unit == 'Mile':
    result = float(user_input1) / 63360
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Mile<span>', unsafe_allow_html=True)

# logic for yard to yard
elif from_unit == 'Yard' and to_unit == 'Yard':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yard to foot
elif from_unit == 'Yard' and to_unit == 'Foot':
    result = float(user_input1) * 3
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Foot<span>', unsafe_allow_html=True)

# logic for foot to yard
elif from_unit == 'Foot' and to_unit == 'Yard':
    result = float(user_input1) / 3
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Foot is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for yard to inch
elif from_unit == 'Yard' and to_unit == 'Inch':
    result = float(user_input1) * 36
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Yard is equal to {result} Inch<span>', unsafe_allow_html=True)

# logic for inch to yard
elif from_unit == 'Inch' and to_unit == 'Yard':
    result = float(user_input1) / 36
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Inch is equal to {result} Yard<span>', unsafe_allow_html=True)

# logic for nautical mile to nautical mile
elif from_unit == 'Nautical Mile' and to_unit == 'Nautical Mile':
    result = float(user_input1)
    st.markdown(f'<span style="color: #003092; font-size: 22px; ; border-radius: 50px; padding: 5px ;  width: 100%">{user_input1} Nautical Mile is equal to {result} Nautical Mile<span>', unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by <strong>Awais Gohar Tagar</strong>  🚀 </div>", unsafe_allow_html=True)