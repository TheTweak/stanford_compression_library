from scl.utils.bitarray_utils import BitArray

CODES = {
    "A": BitArray("10"),
    "B": BitArray("00"),
    "C": BitArray("11"),
    "D": BitArray("110")
}

R_CODES = {}

for k, v in CODES.items():
    bits = ""
    for b in v:
        bits += str(b)
    R_CODES[bits] = k


def decode(sequence: BitArray):
    assert len(sequence) >= 2

    result = ""
    s = ""
    i = len(sequence) - 1

    while i >= 0:
        s = str(sequence[i]) + s
        prev_s = str(sequence[i - 1]) if i >= 1 else "<NO_CODE>"

        if prev_s + s not in R_CODES:
            result += R_CODES[s]
            s = ""

        i -= 1

    return "".join(reversed(result))

def main():
    print(decode(BitArray("100011110110110010")))

if __name__ == "__main__":
    main()
