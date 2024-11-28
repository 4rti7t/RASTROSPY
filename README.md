
---

#  RASTROSPY (Keylogger Payload Generator Tool) 🔐

Welcome to the **Keylogger Payload Generator Tool**, your one-stop solution for creating and deploying payloads on multiple platforms! 💻📱

This tool allows you to generate keylogger payloads for **Android**, **Windows**, and **Linux** systems. It also provides a Metasploit listener to interact with the generated payload.

---

## 🚀 Features

- **💥 Multiple Platform Support**:
  - Android 📱
  - Windows 💻
  - Linux 🐧

- **⚡ Fast Payload Generation**:
  - Use **Metasploit's `msfvenom`** to quickly generate reverse TCP payloads.

- **🎧 Live Listener**:
  - Automatically starts a **Metasploit listener** to handle the reverse shell connection.

- **💡 User-Friendly Interface**:
  - Simple prompts to guide you through each step.
  - Modern terminal output with progress bars and loading animations.

- **🔒 Secure and Efficient**:
  - Easy validation of IP addresses and port numbers.
  - Customizable payload options.

---

## ⚙️ Installation

### Prerequisites

Before using the tool, make sure you have the following installed:

- **Kali Linux** or any other Linux-based OS.
- **Metasploit Framework** for generating and handling payloads.
- **Python 3.x** (with the `colorama`, `tqdm`, and `os` libraries installed).

Install the required libraries:
```bash
pip install colorama tqdm
```

---

## 💻 Usage

1. **Clone the Repository**:
   Download or clone this repository to your local machine.

2. **Run the Tool**:
   After cloning the repo, navigate to the directory containing the script and run it:
   ```bash
   python3 keylogger_payload_generator.py
   ```

3. **Select Platform**:
   The tool will prompt you to select the platform you want the payload for:
   - `1. Android`
   - `2. Windows`
   - `3. Linux`

4. **Enter IP and Port**:
   - Enter your local IP address (or the IP of the machine you want to use as a listener).
   - Enter the port number for the reverse connection.

5. **Payload Generation**:
   - The script will generate the appropriate payload for the selected platform and save it in the current directory.

6. **Listener**:
   - The tool will automatically start a Metasploit listener on the provided IP and port to capture the incoming connection.

---

## 📖 Example Output

```bash
Welcome to the Keylogger Payload Generator Tool! 🚀
Please select the platform for the payload creation:
1. Android 📱
2. Windows 💻
3. Linux 🐧

Enter your choice (1/2/3): 1
Enter your IP address: 192.168.1.1
Enter the port number: 4444

Creating Android Payload... ⚡
Generating... ██████████ 100%
Android Keylogger APK has been generated. 📲

Starting Metasploit Listener... 🎧
```

---

## 🎨 Customization

You can easily customize the payload creation process or add new features like:

- **🔥 More Payload Types**: Add support for additional platforms and payload types.
- **⚙️ Advanced Options**: Customize the payload (e.g., payload type, encryption) via command-line arguments.

---

## 📢 Contributing

We welcome contributions! If you have suggestions for improving the tool, feel free to:

- Fork the repository.
- Create a new branch.
- Submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

For any questions or issues, feel free to reach out to us!

- **Email**: arti7tofficial@gmail.com
---

💥 **Enjoy using the Keylogger Payload Generator Tool!** 💥

---
