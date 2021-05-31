from dummy_model import linguistic_model
import bitarray
import huffman
'''
这里有个测试模型，连接语言模型和编码部分的代码
'''
def encode(hidden_msg):
    ba = bitarray.bitarray()
    ba.frombytes(hidden_msg.encode('utf-8'))
    msg_bits_list = ba.tolist()
    msg_bits_length = len(msg_bits_list)

    sentence = []
    i = 0
    encode_msg_bits = []

    while i < msg_bits_length:
        # token_prob_dict= {token : probability}
        token_prob_dict, context = linguistic_model(sentence)

        coding = huffman.HuffmanCoding()
        coding.make_heap(token_prob_dict)
        coding.merge_nodes()

        root = coding.make_codes()

        while root.token is None:
            if i >= msg_bits_length or msg_bits_list[i] == 0:
                root = root.left
            else:
                root = root.right
            i += 1

        selection = root.token
#         print(coding.get_encoded_tokens([selection]))
        sentence += [selection]
        encode_msg_bits += coding.get_encoded_tokens([selection])
    return sentence


def decode(sentence):
    decode_msg_bits = ''
    for x in range(len(sentence)):
        token_prob_dict, _ = linguistic_model(sentence[:x])
        coding = huffman.HuffmanCoding()
        coding.make_heap(token_prob_dict)
        coding.merge_nodes()
        root = coding.make_codes()
        decode_msg_bits += coding.get_encoded_tokens([sentence[x]])

    def decode_from_bits(bits):
        '''
        将bit流转化为字符串
        :param bits: list or str
        :return: 字符串
        '''
        if type(bits) is str:
            bits = list(map(int, bits))
        bits = bits[:int(len(bits) / 8) * 8]  # utf-8编码中bit长度是8的整数倍
        ba = bitarray.bitarray(bits)

        msg_str = ba.tobytes().decode('utf-8', 'ignore')
        return msg_str

    return decode_from_bits(decode_msg_bits)

if __name__ == '__main__':
    sen = encode("jjm")