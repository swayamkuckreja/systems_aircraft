import matplotlib.pyplot as plt
# Data
MTOW = 23000
OEW = 13600
max_payload = 7400
max_fuel = 5000

# Configuration: Maximum Fuel
fuel_max_config = max_fuel
payload_max_config = MTOW - (OEW + fuel_max_config)

# Configuration: Maximum Payload
payload_max_payload_config = max_payload
fuel_max_payload_config = MTOW - (OEW + payload_max_payload_config)

# Labels and values for Maximum Fuel configuration
labels_fuel = ['OEW', 'Payload', 'Fuel']
values_fuel = [OEW, payload_max_config, fuel_max_config]
labels_fuel = [f'{label} ({value} kg)' for label, value in zip(labels_fuel, values_fuel)]

# Labels and values for Maximum Payload configuration
labels_payload = ['OEW', 'Payload', 'Fuel']
values_payload = [OEW, payload_max_payload_config, fuel_max_payload_config]
labels_payload = [f'{label} ({value} kg)' for label, value in zip(labels_payload, values_payload)]

# Plotting the pie chart for Maximum Fuel configuration
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.pie(values_fuel, labels=labels_fuel, autopct='%1.1f%%', startangle=90)
plt.title('Aircraft Weight Distribution (Max Fuel)')

# Plotting the pie chart for Maximum Payload configuration
plt.subplot(1, 2, 2)
plt.pie(values_payload, labels=labels_payload, autopct='%1.1f%%', startangle=90)
plt.title('Aircraft Weight Distribution (Max Payload)')

plt.tight_layout()
plt.show()