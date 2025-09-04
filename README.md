🦠 COVID-Data Analysis - Real-Time API with GUI
📌 Project Overview
Originally created as a 12th-grade academic project, this COVID-19 dashboard began with static CSV datasets. It has since evolved into a powerful tool that integrates a real-time API and now features a Tkinter-based GUI, enabling users to interactively explore COVID-19 data across the globe.

🔧 Technologies Used
Python – Core logic and GUI

Requests – API integration for real-time data

Matplotlib – Visual representation through graphs and charts

Tkinter – Graphical User Interface for enhanced usability

✨ Features
✅ Fetches real-time COVID-19 data from a public API
✅ Displays most & least affected countries dynamically
✅ Visualizes cases, deaths, and testing trends using bar and pie charts
✅ Fully functional Tkinter-based GUI – no need for terminal interaction
✅ Enables country-specific data search
✅ User-friendly interface with pop-up graphs and messages

🛠 Installation & Setup
1️⃣ Install Required Libraries
Ensure Python is installed, then run:

sh
Copy
Edit
pip install requests matplotlib
2️⃣ Clone the Repository
sh
Copy
Edit
git clone https://github.com/SanKrishnan/mini-projects.git
cd covid-analysis-api
3️⃣ Run the Program
sh
Copy
Edit
python covid_analysis.py
🖥️ How It Works
Launches a Tkinter GUI with easy-to-navigate buttons.

Click on menu options to view live stats, graphs, or search for a country.

Real-time data is retrieved from an open-source COVID-19 API.

Graphs are generated dynamically inside the GUI using Matplotlib.

📊 GUI Menu Options
About COVID-19

Top 5 Worst Affected Countries

Top 5 Least Affected Countries

Deaths in Last 24 Hours

Graph - Most/Least Affected

Graph - Deaths over Last 30 Days

Testing Stats and Pie Graph

Country Stats Search

Exit

🌍 API Integration
Utilizes the disease.sh open-source API to fetch:

Country-wise cases, deaths, tests

Historical trends for the last 30 days

🚀 Future Enhancements
Include vaccination data and trends

Add dark mode for GUI

Introduce voice commands for accessibility

Option to export graphs as PNG/PDF

🤝 Contributing
Pull requests and ideas for new features are welcome!

📜 License
Licensed under the MIT License.
