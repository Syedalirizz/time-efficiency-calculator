import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Title of the app
st.title("AI-Powered Time Efficiency Calculator")

# Introduction and instructions
st.markdown("""
This tool helps you input daily tasks and calculates how efficiently you are spending your time. 
It provides suggestions for improvement based on your input.
""")

# Input Fields
st.header("Input Your Daily Tasks and Time Spent (in minutes):")
tasks = []
times = []

# Remove task limit to make it more flexible
num_tasks = st.number_input("How many tasks do you want to input?", min_value=1, max_value=50, step=1)

for i in range(num_tasks):
    task = st.text_input(f"Task {i+1} Name", key=f"task_{i}")
    time = st.number_input(f"Time spent on {task} (minutes)", min_value=1, max_value=1440, step=1, key=f"time_{i}")
    
    if task and time:
        tasks.append(task)
        times.append(time)

# Calculate total time spent
total_time = sum(times)
total_hours = total_time // 60
total_minutes = total_time % 60

# Display total time spent
st.subheader(f"Total Time Spent: {total_hours} hours and {total_minutes} minutes")

# Time Efficiency Suggestions
st.header("Time Efficiency Suggestions")
suggestions = []

# Dummy suggestions for now (you can improve or customize this later)
if total_time > 480:  # 8 hours of work
    suggestions.append("Consider taking more breaks to avoid burnout.")
if total_time < 180:  # Less than 3 hours
    suggestions.append("You might be under-committing. Try allocating more tasks or work sessions.")
if total_time >= 600:  # Over 10 hours
    suggestions.append("You are working a lot! Maybe delegate some tasks or optimize your workflow.")

# Display suggestions
if suggestions:
    for suggestion in suggestions:
        st.markdown(f"- {suggestion}")
else:
    st.markdown("Your time allocation looks balanced. Keep up the good work!")

# Create a time distribution chart
st.header("Time Distribution by Task")
time_data = pd.DataFrame({'Task': tasks, 'Time (minutes)': times})
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the chart
ax.pie(time_data['Time (minutes)'], labels=time_data['Task'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
st.pyplot(fig)

# Flowchart of time distribution (percentage)
st.header("Time Efficiency Flowchart")

# Create a DataFrame for flowchart
time_df = pd.DataFrame({'Task': tasks, 'Time Spent (minutes)': times})
time_df['Percentage'] = (time_df['Time Spent (minutes)'] / total_time) * 100

# Display the flowchart
st.write("Here is the time spent on each task in percentage:")
st.dataframe(time_df)

# Make sure we close the streamlit session properly
if st.button("Clear Data"):
    st.experimental_rerun()
