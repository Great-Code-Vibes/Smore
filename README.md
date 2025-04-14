name: "Smore"
tagline: "A Research-Grade Bitcoin Wallet Keyspace Explorer (GPU-Accelerated)"

about: >
  Smore is a tool built for **educational use**, cryptographic research,
  and keyspace analysis related to Bitcoin. It demonstrates how private keys
  relate to public addresses using real ECDSA math and allows users to explore
  address generation and collision probabilities at scale.

  GPU acceleration and live balance checking make it ideal for studying Bitcoin’s keyspace
  in a controlled, testable environment — with full transparency.

features:
  - "Real ECDSA key and Bitcoin address generation"
  - "Supports P2PKH (legacy) and P2WPKH (SegWit) address formats"
  - "Live balance checking via public blockchain APIs"
  - "OpenCL-based GPU acceleration (NVIDIA / AMD)"
  - "Custom USD threshold filter for hit results"
  - "Simple GUI with logging and live statistics"
  - "Supports both random generation and bulk keyspace exploration"

install:
  clone:
    - "git clone https://github.com/Great-Code-Vibes/Smore.git"
    - "cd Smore"
  dependencies:
    - "pip install -r requirements.txt"
  gpu_note: >
    Make sure your system has OpenCL drivers installed and your GPU is compatible.
    This allows you to take full advantage of Smore’s acceleration.

run:
  command: "python smore.py"
  gui_instructions: >
    Use the interface to configure scanning options, load addresses or ranges,
    and begin exploring the Bitcoin keyspace responsibly.

license:
  type: "MIT"
  text: >
    Licensed under the MIT License — for legal, educational, and research use only.
    Commercial use is permitted, but users assume full legal responsibility for compliance.

disclaimer: >
  ⚠️ **Important Notice**

  Smore is intended for **educational purposes**, **security research**, and **authorized experimentation** only.

  - Do not use this software to attempt unauthorized access to wallets or funds.
  - This tool does **not guarantee results**, nor is it built for malicious purposes.
  - The developer assumes **no responsibility** for misuse, damage, or legal issues resulting from improper use.

  Always comply with your local laws and use this tool **ethically and responsibly**.

author:
  alias: "Great-Code-Vibes"
  about: >
    I build privacy-focused, automation-driven software — from crypto research tools to
    stealthy security frameworks. I focus on clean design, modular structure, and responsible engineering.

badges:
  - "![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)"
  - "![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)"

screenshot:
  title: "Smore GUI Preview"
  image: "images/smore-gui.png"
  caption: "Customtkinter interface for controlling scans and viewing stats in real-time"
