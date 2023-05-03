# Real-time Process Data Dashboard

## Introduction

This project is a real-time process data dashboard that visualizes data from a bioreactor. The goal is to provide users with a web-based interface to monitor and analyze temperature, pH, distilled oxygen, and pressure data in real-time.

## Project Overview

The dashboard is built using Python, Flask, and Plotly to create interactive visualizations. The data is stored in a Postgres database, and the dashboard retrieves the data and presents it in an intuitive graphical format.

## Technical Details

- The project is implemented in Python using Flask and Plotly libraries.
- Docker is used for containerization to ensure easy deployment and testing.
- The data is stored in a Postgres database, with separate tables for temperature, pH, distilled oxygen, and pressure.
- The dashboard retrieves data from the database and visualizes it using interactive Plotly graphs.
- Users can access the dashboard by running the Docker container and navigating to http://localhost:8888 in their web browser.

## Functionality

The dashboard allows users to:

- View real-time temperature, pH, distilled oxygen, and pressure data.
- Plot the data over time using interactive graphs.
- Select a specific time window to focus on.
- Refresh the data without refreshing the page.
- Download the data as a CSV file.

## Usage

To run the project locally:

1. Make sure Docker is installed on your machine.
2. Clone the project repository to your local system.
3. Navigate to the project directory.
4. Open a terminal and run the command 
```
docker compose up
```
5. Access the dashboard in your web browser at http://localhost:8888.

## Summary

The real-time process data dashboard provides an efficient way to monitor and analyze key process variables in a bioreactor. By visualizing the data in an interactive dashboard, users can gain insights and make informed decisions. This project demonstrates proficiency in Python, web development, and data visualization techniques.
