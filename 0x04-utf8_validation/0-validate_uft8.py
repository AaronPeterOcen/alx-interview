#!/usr/bin/python3
"""
 Method that determines if a given data set represents a valid UTF-8 encoding.
"""

def validUTF8(data):
  """
  This function checks if a given data set represents a valid UTF-8 encoding.
  """
  def is_start_byte(byte):
        return byte >> 6 != 0b10

        num_bytes = 0

        for byte in data:
            if num_bytes == 0:
                # Determine the number of bytes to follow based on the leading bits of the start byte
                if byte >> 5 == 0b110:
                    num_bytes = 1
                elif byte >> 4 == 0b1110:
                    num_bytes = 2
                elif byte >> 3 == 0b11110:
                    num_bytes = 3
                elif byte >> 7:
                    return False
            else:
                # If it's a continuation byte, it should start with 10
                if not (byte >> 6 == 0b10):
                    return False
                num_bytes -= 1

        return num_bytes == 0
