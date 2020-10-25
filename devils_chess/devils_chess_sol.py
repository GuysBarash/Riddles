import numpy as np

BOARD = 8
SQUARES = BOARD ** 2


def _int2arr(num):
    bytes = int(np.ceil(SQUARES / 8.0))
    num_arr = np.arange(num, num + 1, dtype='>i%d' % bytes)
    res = np.unpackbits(num_arr.view(np.uint8))[-1 * SQUARES:]
    res_flipped = res[::-1]
    return res_flipped


def _arr2int(arr):
    return arr.dot(1 << np.arange(arr.size)[::-1])


def flip(arr, pos):
    mask = arr.copy()
    mask[pos] = 1 - mask[pos]
    return mask


def arr2coin(arr):
    err_bits = int(np.floor(np.log2(arr.shape[0])))
    res_arr = np.zeros(err_bits, dtype=int)
    for idx in range(err_bits):
        idxes_to_check = [t for t in range(SQUARES) if _int2arr(t)[idx] == 1]
        for t_idx in idxes_to_check:
            res_arr[idx] ^= arr[t_idx]

    return _arr2int(res_arr)


arr = np.random.randint(0, 2, size=BOARD ** 2)
devils_coin_to_coin_to_flip = dict()
for coin_to_flip in range(SQUARES):
    flipped_arr = flip(arr, coin_to_flip)
    calc_results = arr2coin(flipped_arr)
    devils_coin_to_coin_to_flip[calc_results] = coin_to_flip

print(f"Original arr: {arr}")
already_used = list()
for possible_coin in range(SQUARES):
    coin_to_flip = devils_coin_to_coin_to_flip.get(possible_coin, '<< MISSING >> ')
    print(f"If the devil chose coin {possible_coin} you should flip coin {coin_to_flip}")
