import json
def read_genesis_block(file_path):
  with open(file_path, "rb") as f:
    # Read the first 80 bytes (block header size)
    block_header = f.read(80)

    # Define an empty dictionary for block information
    block_data = {}

    # Parse header fields (replace with desired fields)
    block_data["version"] = int.from_bytes(block_header[:4], byteorder="little")
    block_data["previous_hash"] = block_header[4:36].hex()
    block_data["merkle_root"] = block_header[36:68].hex()
    block_data["timestamp"] = int.from_bytes(block_header[68:72], byteorder="little")
    block_data["nonce"] = int.from_bytes(block_header[72:], byteorder="little")

  return block_data

if __name__ == "__main__":
  file_path = "blk00000-f10.blk"

  genesis_block = read_genesis_block(file_path)

  # Print the JSON-formatted block data
  print(json.dumps(genesis_block, indent=2))
