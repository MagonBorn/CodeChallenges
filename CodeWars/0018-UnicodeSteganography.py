import timeit
import unittest

# ---------- Initial Solution ----------
def decode_hidden_data(encoded_message):
    result = []
    for i in encoded_message:
        if ord(i) > 256:
            result.append(chr(int(f'{ord(i):08b}'[-8::], 2)))
    decoded = "".join(result)
    return decoded

def encode_hidden_data(visible_text, hidden_data):
    encoded_message = ""
    for i in hidden_data:
        x = "111000000001" + str(f'{int(ord(i)):08b}')
        encoded_message += chr(int(x, 2))
    return visible_text + encoded_message

# ---------- Additional Solution ----------
def decode_hidden_data_two(encoded_message, key=917760):
    return "".join(chr(ord(c) - key) for c in encoded_message if ord(c) > 10**5)

def encode_hidden_data_two(visible_text, hidden_data, key=917760):
    return visible_text + "".join(chr(ord(c) + key) for c in hidden_data)

#  ---------- Testing Data ----------
decodeTestData = [
    ['WWWWW󠅍󠅡󠅤󠅥󠄠󠅢󠅹󠄺󠄠󠅓󠅩󠅭󠅰󠅬󠅥󠄠󠅒󠅩󠅣󠅫󠄠󠄲󠄰󠄲󠄵','Made by: Simple Rick 2025'],
    ['This is visible text. 󠅔󠅨󠅩󠅳󠄠󠅩󠅳󠄠󠅴󠅨󠅥󠄠󠅳󠅥󠅣󠅲󠅥󠅴󠄠󠅭󠅥󠅳󠅳󠅡󠅧󠅥',
        'This is the secret message'],
    ['Another visible message. 󠅁󠅮󠅯󠅴󠅨󠅥󠅲󠄠󠅨󠅩󠅤󠅤󠅥󠅮󠄠󠅴󠅥󠅸󠅴',  'Another hidden text'],
    ['Unicode steganography!󠅒󠅯󠅣󠅫󠅳󠄡',       'Rocks!']
  ]

encodeTestData = [
    ['message',                   'SECRET',                      'message󠅓󠅅󠅃󠅒󠅅󠅔'],
    ['This is visible text. ',    'This is the secret message',
        'This is visible text. 󠅔󠅨󠅩󠅳󠄠󠅩󠅳󠄠󠅴󠅨󠅥󠄠󠅳󠅥󠅣󠅲󠅥󠅴󠄠󠅭󠅥󠅳󠅳󠅡󠅧󠅥'],
    ['Another visible message. ', 'Another hidden text',
        'Another visible message. 󠅁󠅮󠅯󠅴󠅨󠅥󠅲󠄠󠅨󠅩󠅤󠅤󠅥󠅮󠄠󠅴󠅥󠅸󠅴'],
    ['Unicode steganography!',    'Rocks!',
        'Unicode steganography!󠅒󠅯󠅣󠅫󠅳󠄡']
]

# ---------- Unit Tests ----------
class Test(unittest.TestCase):
    def test_decode_data(self):
        for data in decodeTestData:
            self.assertEqual(decode_hidden_data(data[0]), data[1])
    
    def test_encode_data(self):
        for data in encodeTestData:
            self.assertEqual(encode_hidden_data(data[0], data[1]), data[2])


if __name__ == '__main__':
    # ---------- Efficiency Tests ----------

    # print(
    #     f'Decode Hidden Data Function: {timeit.timeit(lambda: decode_hidden_data(decodeTestData[0][0]), number=1000000)}')

    # print(
    #     f'Decode Hidden Data Two Function: {timeit.timeit(lambda: decode_hidden_data_two(decodeTestData[0][0]), number=1000000)}')
    # print(
    #     f'Encode Hidden Data Function: {timeit.timeit(lambda: encode_hidden_data(encodeTestData[0][0], encodeTestData[0][1]), number=1000000)}')

    # print(
    #     f'Encode Hidden Data Two Function: {timeit.timeit(lambda: encode_hidden_data_two(encodeTestData[0][0], encodeTestData[0][1]), number=1000000)}')
    
    # Decode Hidden Data Function: 15.850283200001286
    # Decode Hidden Data Two Function: 5.048987099999067
    # Encode Hidden Data Function: 3.9308648000005633
    # Encode Hidden Data Two Function: 1.3685863999999128

   # ---------- Function Results ----------
    for data in decodeTestData:
      result = decode_hidden_data(data[0])
      print(result)
    
    for data in encodeTestData:
        result = encode_hidden_data_two(data[0], data[1])
        print(result)

# ---------- Run Unit Tests ----------
unittest.main()