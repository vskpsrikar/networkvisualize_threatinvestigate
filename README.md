**Network Traffic Visualization** - This repository contains code and visualizations for a traffic visualization project focused on threat investigation.

**Project Overview** - The goal of this project is to develop a network security model that can predict future threats from the network traffic volume based on historical data. This model can be used for various purposes, such as:

Security monitoring: Identifying unusual traffic patterns can aid in detecting suspicious activity or potential denial-of-service attacks. 
Traffic optimization: Understanding traffic patterns allows for implementing strategies to optimize network performance.

**Data and Preprocessing** - The data used to build this project is the network traffic captured for 20 days.

The data preprocessing steps are as follows:-

a) Feature extraction: Selecting relevant features from the raw data, such as bytes transferred, packets sent/received, and timestamps. 
b) Data segmentation: Dividing the data into smaller time intervals (e.g., 5 minutes) to create samples for model training. 
c) Data cleaning: Any unwanted or missing values and outliers in the data are taken care.
d) Smoothing: Applied techniques like Gaussian filter to reduce noise in the data.

**Contributions** - Feel free to submit pull requests with improvements to the code, documentation, or visualizations.
