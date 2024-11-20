import requests
import subprocess
import time
import os

# Constants
TARGET_IP = "YOUR NORDLAYER IP"
NORD_APP_PATH = r"C:\Program Files (x86)\NordLayer\NordLayer.exe"  # Path to NordLayer executable
NORD_STOP_COMMAND = r"taskkill /IM NordLayer.exe /F"  # Command to stop NordLayer

def get_public_ip():
    """Fetches the current public IP address."""
    try:
        response = requests.get("https://api.ipify.org?format=text", timeout=5)
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        print(f"Error fetching public IP: {e}")
        return None

def stop_nordlayer():
    """Stops the NordLayer application."""
    try:
        subprocess.run(NORD_STOP_COMMAND, shell=True, check=True)
        print("NordLayer app stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping NordLayer: {e}")

def start_nordlayer():
    """Starts the NordLayer application."""
    try:
        # Launch NordLayer app in the background
        subprocess.Popen([NORD_APP_PATH], shell=True)
        print("NordLayer app started successfully.")
    except Exception as e:
        print(f"Error starting NordLayer: {e}")

def main():
    while True:
        print("Checking VPN connection...")
        current_ip = get_public_ip()

        if current_ip == TARGET_IP:
            print(f"Connected to NordLayer VPN (IP: {current_ip}). No action needed.")
        else:
            print(f"Not connected to target VPN IP (Current IP: {current_ip}). Restarting NordLayer...")
            stop_nordlayer()
            time.sleep(3)  # Wait before restarting
            start_nordlayer()
            time.sleep(10)  # Wait for connection to establish

        # Check every 10 seconds
        time.sleep(10)

if __name__ == "__main__":
    main()
