NordLayer VPN Connection Monitor -

This script monitors your VPN connection to ensure it remains connected to a specified target IP address. If the connection is lost, it automatically restarts the NordLayer application to reestablish the connection.

Features -

Continuously checks the public IP address to verify VPN connectivity.

Automatically restarts the NordLayer application if disconnected from the target VPN.

Simple and lightweight solution for ensuring persistent VPN connectivity.

Prerequisites -

Python 3.8 or newer installed on your system.

NordLayer installed on your system.

A valid VPN connection configured with your target IP address.

Setup Instructions -

Clone this repository by running git clone https://github.com/shivaansh74/Always-On-VPN.

Navigate to the repository folder using cd Always-On-VPN.

Install the required Python package using pip install requests.

Update the following variables in the script as needed:

  TARGET_IP: Your target VPN IP address.

  NORD_APP_PATH: Path to the NordLayer executable on your system.
  
  NORD_STOP_COMMAND: Command to stop NordLayer (default provided).

Usage -

Run the script to start monitoring your VPN connection by executing python vpn_monitor.py.

The script will:

Check the current public IP address.

Restart NordLayer if not connected to the target VPN.

Notes -

Ensure that the NordLayer executable path is correctly specified.

Run the script with sufficient permissions if required to manage applications.

License -

This project is licensed under the MIT License.

Contact -
For issues or suggestions, please contact Shivaansh Dhingra at shivi@datafysystems.com.
