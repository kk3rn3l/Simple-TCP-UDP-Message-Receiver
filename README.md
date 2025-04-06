# Simple TCP/UDP Message Receiver

A lightweight tool to create TCP or UDP servers for receiving messages. Built for Kali Linux but compatible with any Linux system. Ideal for testing, debugging, or learning network communication basics.

---

## Features
- **TCP Server**: Reliable, connection-oriented message reception.
- **UDP Server**: Fast, connectionless message reception.
- **Python Scripts**: Flexible and customizable.
- **Netcat Commands**: Quick one-liners for testing.
- **Cross-Platform**: Works on Linux, macOS, and Windows (Python scripts only).

---

## Installation

### Prerequisites
- **Kali Linux** (or any Linux distribution).
- Python 3.x (pre-installed on Kali).
- Netcat (`nc`) for quick testing (pre-installed on Kali).

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/kk3rn3l/tcp-udp-server.git
   cd tcp-udp-server
   ```
2. Make the Python scripts executable (optional):
   ```bash
   chmod +x tcp_server.py udp_server.py
   ```

---

## Usage

### 1. Python Scripts
#### **TCP Server**
```bash
python3 tcp_server.py
# To customize IP/port, edit HOST and PORT in the script.
```

#### **UDP Server**
```bash
python3 udp_server.py
# To customize IP/port, edit HOST and PORT in the script.
```

### 2. Netcat (Quick Testing)
#### **TCP Server**
```bash
nc -l -p 4444 -v  # Listen on port 4444
```

#### **UDP Server**
```bash
nc -u -l -p 4444 -v  # Listen on UDP port 4444
```

---

## Sending Messages
Use `netcat`, `telnet`, or any socket client to send messages to the server.

### Example Commands
#### **TCP Client**
```bash
echo "Hello TCP" | nc localhost 4444
# Or use telnet:
telnet localhost 4444
```

#### **UDP Client**
```bash
echo "Hello UDP" | nc -u localhost 4444
```

---

## Configuration
- **Change Port**: Modify the `PORT` variable in the Python scripts or replace `4444` in the commands.
- **Bind to Specific IP**: Replace `0.0.0.0` (all interfaces) with a specific IP in the Python scripts.

---

## Troubleshooting
- **Port Conflicts**: Ensure no other service is using the same port.
- **Firewall Issues**: Allow traffic on the chosen port:
  ```bash
  sudo ufw allow 4444
  ```
- **Permissions**: Use `sudo` for ports below 1024 (e.g., `sudo nc -l -p 80`).

---

## Contributing
Contributions are welcome!  
1. Fork the repository.  
2. Create a feature branch: `git checkout -b new-feature`.  
3. Commit changes: `git commit -am 'Add feature'`.  
4. Push to the branch: `git push origin new-feature`.  
5. Submit a pull request.

---

## Disclaimer
Use this tool responsibly and only on networks you own/have permission to test. The authors are not responsible for misuse.

---
