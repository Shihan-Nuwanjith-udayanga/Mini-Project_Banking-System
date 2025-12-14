import matplotlib.pyplot as plt
import pandas as pd

# ===================== DATA =====================

salary_waiting = [
0,0,1.1,2.8,4.2,6,7.35,9.2,10.85,12.3,13.7,15.2,16.7,18.05,19.5,
21,22.3,23.9,25.2,26.6,28.05,29.5,31,32.5,33.95,35.5,36.9,
38.4,39.8,41.2,42.6,44,45.4,46.85,48.25,49.6,51,52.4,
53.8,55.2,56.55,58,59.4,60.75,62.15,63.55,65,66.4,67.85,69.2
]

normal_waiting = [
0,0,0,0,0.3,0,0,0.45,0,0,0,0,0,0,0.2,0,0,0,0,0,
0,0,0,0,0,0,0.3,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0
]

# ===================== CHART 1 =====================
# Waiting Time Comparison

plt.figure()
plt.plot(range(1,51), salary_waiting, label="Salary Day")
plt.plot(range(1,51), normal_waiting, label="Normal Day")
plt.xlabel("Customer Number")
plt.ylabel("Waiting Time (minutes)")
plt.title("Waiting Time Comparison: Normal Day vs Salary Day")
plt.legend()
plt.show()

# ===================== CHART 2 =====================
# Queue Growth on Salary Day

plt.figure()
plt.plot(range(1,51), salary_waiting)
plt.xlabel("Customer Number")
plt.ylabel("Waiting Time (minutes)")
plt.title("Queue Growth Pattern on Salary Day")
plt.show()

# ===================== CHART 3 =====================
# Average Time in System

avg_times = pd.DataFrame({
    "Condition": ["Normal Day", "Salary Day"],
    "Average Time in System (min)": [4.53, 40.95]
})

plt.figure()
plt.bar(avg_times["Condition"], avg_times["Average Time in System (min)"])
plt.xlabel("Operating Condition")
plt.ylabel("Average Time in System (minutes)")
plt.title("Average Time Spent in System")
plt.show()

# ===================== CHART 4 =====================
# Cashier Utilization Comparison

utilization = pd.DataFrame({
    "Condition": ["Normal Day", "Salary Day"],
    "Utilization": [0.63, 1.00]
})

plt.figure()
plt.bar(utilization["Condition"], utilization["Utilization"])
plt.xlabel("Operating Condition")
plt.ylabel("Cashier Utilization")
plt.title("Cashier Utilization Comparison")
plt.show()
