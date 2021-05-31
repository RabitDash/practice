import numpy as np
import pickle
'''
测试用语言模型
'''
f_handle = open("vocab.pkl", "rb")
vocab = pickle.load(f_handle)
vocab = vocab[2:] # remove <pad>, <unk>

candidate_num = 1000 #候选词数量

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def linguistic_model(context:list):
    # shuffle
    seed = 0
    for token in context:
        seed += vocab.index(token)
    np.random.seed(seed)
    index = [i for i in range(len(vocab))]
    np.random.shuffle(index)
    candidate_token_index = index[:candidate_num]
    candidate_token_str   = list(map(lambda i: vocab[i], candidate_token_index))
    # make prob
    candidate_probability = softmax(np.random.standard_normal(candidate_num))
    # make dict
    candidate_token_prob_dict = dict(zip(candidate_token_str, candidate_probability))
    return candidate_token_prob_dict, context