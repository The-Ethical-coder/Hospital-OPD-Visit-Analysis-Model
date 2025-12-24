# Hospital-OPD-Visit-Analysis-Model
Hospital OPD Visit Analysis Model 🏥

An Exploratory Data Analysis (EDA) project focused on hospital Outpatient Department (OPD) visit patterns. This model simulates hospital traffic and identifies daily/weekly trends to optimize staffing and reduce patient wait times.

📌 Project Overview

As part of the Minor 1 EDA submission, this project analyzes a synthetic dataset of 1,000+ hospital records to uncover:

Peak Arrival Times: Identifying rush hours (10 AM - 1 PM).

Weekly Cycles: Analyzing high-load days (Mondays) vs. low-load days (Sundays).

Departmental Efficiency: Comparing wait times across Cardiology, Pediatrics, General Medicine, and more.

🛠️ Technical Stack

Data Generation: NumPy, Random

Data Manipulation: Pandas

Visualization: Matplotlib, Seaborn

Environment: Jupyter Notebook / Python Script

🚀 Getting Started

1. Clone the Repository

git clone [https://github.com/The-Ethical-coder/Hospital-OPD-Visit-Analysis-Model.git](https://github.com/The-Ethical-coder/Hospital-OPD-Visit-Analysis-Model.git)
cd Hospital-OPD-Visit-Analysis-Model


2. Install Dependencies

pip install pandas numpy matplotlib seaborn


3. Generate the Dataset

Run the generator script to create the hospital_opd_visits.csv file:

python opd_data_generator.py


4. Run the Analysis

Execute the analysis script to generate trend plots and summary statistics:

python hospital_analysis.py


📊 Key Features

Synthetic Data Engine: Generates realistic hospital logs including age, gender, department, and consultation fees.

Trend Analysis: Automated line plots for daily volume and bar charts for weekly distribution.

Heatmap Visualization: A density map correlating "Day of Week" and "Hour of Day" to pinpoint bottlenecks.

Summary Statistics: Automated reporting on average wait times and total revenue.

📂 Project Structure

opd_data_generator.py: Script to generate synthetic hospital data.

hospital_analysis.py: Main EDA script for processing and plotting.

hospital_opd_visits.csv: The generated dataset (ignored by .gitignore or provided as sample).

plots/: Directory containing generated PNG visualizations.

👨‍💻 Author

The-Ethical-coder
CSE AIML Student

This project is for educational purposes under the Minor 1 EDA curriculum.
