# COVID-19 Data Analysis with API Integration

## 📌 Project Overview
This project was originally developed as part of my **12th-grade coursework** to analyze the impact of the COVID-19 pandemic. Initially, it used **CSV datasets** to display COVID-19 statistics. Now, I have **enhanced** the project by integrating a **real-time API**, which dynamically fetches COVID-19 data instead of relying on static files.

## 🔧 Technologies Used
- **Python** - Data handling and processing
- **Requests** - API integration for real-time data
- **Matplotlib** - Data visualization using graphs and charts

## ✨ Features
✅ Fetches **real-time COVID-19 data** via an API
✅ Displays **most & least affected states/countries**
✅ Visualizes **COVID-19 cases, recoveries, deaths, and testing trends**
✅ Interactive **menu-based navigation**
✅ Implements **bar graphs and pie charts** for easy data interpretation

## 🛠 Installation & Setup
### 1️⃣ Install Required Libraries
Ensure you have Python installed and run the following command to install dependencies:
```sh
pip install requests matplotlib
```

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/SanKrishnan/covid-analysis-api.git
cd covid-analysis-api
```

### 3️⃣ Run the Program
```sh
python covid_analysis.py
```

## 🖥️ How It Works
- The program provides a **menu-based** interface for easy navigation.
- The user can select an option to view **COVID-19 statistics** for different regions.
- The program fetches **live data from an API**, eliminating the need for manual CSV updates.
- **Graphs and charts** provide a visual representation of the COVID-19 trends.

## 📊 Menu Options
```
0. About COVID-19
1. Worst affected states/countries
2. Least affected states/countries
3. Deaths by age group
4. COVID-19 updates for Maharashtra (Example)
5. COVID-19 testing stats globally
6-10. Graphical representation for the above
11. Exit
```

## 🌍 API Integration
This project fetches real-time COVID-19 data using an **open-source COVID-19 API**. The API provides up-to-date statistics for different countries, states, and age groups.

## 📝 Future Improvements
- Add more **detailed data insights** such as vaccination rates
- Implement a **GUI version** using Tkinter or Flask
- Allow users to **search for specific countries/states**

## 🤝 Contributing
Feel free to contribute by submitting **pull requests** or **feature suggestions**!

## 📜 License
This project is open-source under the **MIT License**.

---
🚀 **Stay Safe & Stay Informed!**

