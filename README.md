# NordLayer VPN Connection Monitor

This Python script continuously monitors your VPN connection to ensure it remains connected to a specified target IP address. If the connection is lost, the script automatically restarts the NordLayer application to reestablish the VPN connection.

## Features

- **Continuous VPN Connectivity Check:** Monitors your public IP address to ensure it's connected to the target VPN.
- **Automatic Restart of NordLayer:** If the VPN connection is lost, the script automatically restarts the NordLayer application to reconnect.
- **Lightweight Solution:** A simple and effective way to ensure persistent VPN connectivity without manual intervention.

## Prerequisites

Before running this script, ensure the following:

- **Python 3.8+** installed on your system.
- **NordLayer** VPN client installed and properly configured.
- A valid VPN connection configured with the target IP address.

## Setup Instructions

1. Clone this repository:

    ```bash
    git clone https://github.com/shivaansh74/Always-On-VPN
    ```

2. Navigate to the repository folder:

    ```bash
    cd Always-On-VPN
    ```

3. Install the required Python dependencies:

    ```bash
    pip install requests
    ```

4. Update the following variables in the script as needed:

    - **TARGET_IP:** The IP address of your target VPN server.
    - **NORD_APP_PATH:** Path to the NordLayer executable on your system.
    - **NORD_STOP_COMMAND:** The command used to stop the NordLayer application (a default command is provided).

## Usage

Run the script to start monitoring your VPN connection:

```bash
python vpn_monitor.py
```

## License 
This project is licensed under the MIT License.

## Contact
For issues or suggestions, please contact Shivaansh Dhingra at shivi@datafysystems.com.
