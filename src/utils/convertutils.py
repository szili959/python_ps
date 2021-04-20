file_size_up = lambda x: x / 1024

byte_to_kb = lambda x: file_size_up(x)

byte_to_mb = lambda x: file_size_up(byte_to_kb(x))

byte_to_gb = lambda x: file_size_up(byte_to_mb(x))