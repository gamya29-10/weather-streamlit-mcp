import asyncio
from fastmcp import Client
import streamlit as st

# Streamlit UI
st.title("🌦 Weather App using MCP")

city = st.text_input("Enter city name")

async def get_weather(city):
    async with Client("wttrserver.py") as client:
        result = await client.call_tool(
            "get_weather",
            {"city": city}
        )
        return result

# Button click
if st.button("Get Weather"):
    if city:
        result = asyncio.run(get_weather(city))
        st.success(result)
    else:
        st.warning("Please enter a city name")





        