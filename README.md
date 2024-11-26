# SVGA Layer Extractor

A Python script to extract and export individual layers from `.svga` animation files.

## Requirements
- Python 3.6+
- `protobuf` library for parsing `.proto` files.
- `Pillow` library for image processing.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AlirezaF80/SVGA-Layer-Extractor.git
   cd SVGA-Layer-Extractor
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. No need to compile the `svga.proto` file, as the `SVGA_pb2.py` file is already included.  
   However, if you wish to update the `.proto` file, you will need the `protoc` compiler:
   - **Linux/Mac**:
     ```bash
     sudo apt install protobuf-compiler
     ```
   - **Windows**:
     Download from the [official site](https://github.com/protocolbuffers/protobuf/releases).

   Then, run:
   ```bash
   protoc --python_out=. svga.proto
   ```

## Usage

1. Run the script to extract layers:
   ```bash
   python parse_svga.py <input_file.svga>
   ```
   Example:
   ```bash
   python parse_svga.py example.svga
   ```

2. The extracted layers will be saved in a directory named `<input_file>_output` under the same directory as the input file.

## Acknowledgments
- [SVGA-Format](https://github.com/svga/SVGA-Format) for the file format specification.