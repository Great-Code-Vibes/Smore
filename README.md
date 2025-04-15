# Smore: Advanced Bitcoin Wallet Brute-Force Tool

![Smore Banner]([https://i.imgur.com/C0Ch2nM.png]

<div align="center">
  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CUDA Enabled](https://img.shields.io/badge/CUDA-Enabled-76B900.svg)](https://developer.nvidia.com/cuda-toolkit)
[![OpenCL Support](https://img.shields.io/badge/OpenCL-Support-ED1C24.svg)](https://www.khronos.org/opencl/)

</div>

A high-performance Bitcoin wallet brute-force tool designed for red team operations, security auditing, and cryptocurrency recovery scenarios. This framework leverages GPU acceleration to maximize key generation and address derivation speed.

## Features

- **Real Cryptography**: Generate authentic secp256k1 private keys with full keyspace range (1 to 2^256 - 1)
- **Multiple Address Formats**: Support for both P2PKH and P2WPKH address formats
- **Flexible Target Verification**:
  - Custom target address list from file or manual input
  - Blockstream API integration for balance checking
- **Hardware Acceleration**:
  - CUDA support for NVIDIA GPUs
  - OpenCL support for AMD/Intel GPUs
  - CPU fallback mode when no GPU is available
- **Modern UI Options**:
  - CustomTkinter-based interface with dark theme
  - High-performance PyQt alternative for resource-intensive operations
- **Comprehensive Logging**: Detailed event tracking and match recording
- **Resumable Operations**: Save and restore progress between sessions
- **Docker Support**: Easy deployment with GPU passthrough
- **Multiple Attack Modes**:
  - Default (All Keys)
  - BTC Puzzle Challenge
  - Pattern Search
  - Range Splitting

## Screenshots

<div align="center">
  <img src="https://imgur.com/a/Hki9Zxz" width="800px" />
  <p><i>Smore Dashboard with Real-time Monitoring</i></p>
  
  <br />
  
  <img src="https://imgur.com/a/xq5sIqA" width="800px" />
  <p><i>Optimized Smore Dashboard</i></p>
</div>

## Requirements

- Python 3.8+
- CUDA-compatible GPU (recommended for maximum performance)
- OpenCL-compatible GPU (alternative acceleration)
- Docker (for containerized deployment)

## Installation

### Standard Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/smore.git
cd smore
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
# For the default CustomTkinter interface
python run.py

# For the high-performance PyQt interface
python run_optimized.py
```

### Docker Installation

1. Build and run using Docker Compose:
```bash
docker-compose up --build
```

2. For GPU support, ensure you have:
   - NVIDIA Container Toolkit installed for NVIDIA GPUs
   - Docker configured for GPU passthrough

## Configuration Options

- **Target Addresses**: Input manually or load from .txt file
- **Key Generation Range**: Define custom starting point
- **Address Format**: Toggle between P2PKH and P2WPKH
- **Balance Threshold**: Set minimum BTC balance for match logging
- **GPU Acceleration**: Automatically leverages available hardware
- **Attack Modes**: Choose between Default, Puzzle, Pattern, or Range modes
- **Performance Settings**: Configure batch size, thread count, and memory usage
- **API Settings**: Customize blockchain API provider and options

## Technical Details

Smore utilizes:

- **ECDSA**: For Bitcoin key pair generation
- **SHA256/RIPEMD160**: For address derivation
- **CUDA/OpenCL**: For parallel processing of cryptographic operations
- **CustomTkinter/PyQt**: For modern GUI implementation
- **Matplotlib**: For real-time performance visualization

## Usage

1. **Launch the application**: Run `python run.py` or `python run_optimized.py`
2. **Configure settings**:
   - Load target addresses (from file or manual entry)
   - Set minimum balance threshold
   - Choose address format (P2PKH/P2WPKH)
   - Configure GPU acceleration options
   - Select attack mode and mode-specific settings
3. **Start the brute-force operation**:
   - Press the Start button to begin
   - Monitor real-time progress on the dashboard
   - View matches in the Results tab
4. **Export results**:
   - Use the Export button to save matches to a file

## Logs and Output

- `smore/logs/matches.log`: Detailed log of all matches
- `smore/logs/performance.log`: Performance metrics over time
- `smore/logs/progress.json`: Saved progress for resuming operations

## Disclaimer

This tool is intended for legitimate security testing, auditing purposes, and recovery of lost cryptocurrency with proper authorization only. Usage must comply with all applicable laws and regulations.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions, issues, and feature requests are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Acknowledgments

- The Bitcoin community for documentation and standards
- CUDA and OpenCL teams for GPU acceleration frameworks
- CustomTkinter and PyQt developers for the UI toolkits 
