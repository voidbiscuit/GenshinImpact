import re
import json
import codecs

# Load Ciphers
ciphers = json.load(open('data/ciphers.json'))

# Load HU
messages = ciphers['Hu']
decoded_message = []
for message_name, message in messages.items():
    # Base 3
    base_3_message = message
    # Convert to base 3
    base_3_message = re.sub(r'\.', '0', base_3_message)
    base_3_message = re.sub(r'2', '1', base_3_message)
    base_3_message = re.sub(r'3', '2', base_3_message)
    # Get characters from base 3 charcode
    base_3_message = ''.join(list(map(lambda x: chr(int(x, 3) + (ord('@'))) if x else '', base_3_message.split('-'))))
    # Perform ROT 13
    base_3_message_rot_13 = codecs.encode(base_3_message, 'rot13')
    # Build decoded message
    decoded_message.append(base_3_message_rot_13)

# Output
print(' '.join(decoded_message))