from random import randint
from string import ascii_lowercase

from PIL import Image

NAME_OUT = 'pic.png'
FLAG = 'ytctfnicesubstitutioncipherinpng'

def make():
    text = '''In cryptography, a substitution cipher is a method of encrypting by which units of plaintext are replaced with ciphertext, according to a fixed system; the "units" may be single letters (the most common), pairs of letters, triplets of letters, mixtures of the above, and so forth. The receiver deciphers the text by performing the inverse substitution.

    Substitution ciphers can be compared with transposition ciphers. {} In a transposition cipher, the units of the plaintext are rearranged in a different and usually quite complex order, but the units themselves are left unchanged. By contrast, in a substitution cipher, the units of the plaintext are retained in the same sequence in the ciphertext, but the units themselves are altered.

    There are a number of different types of substitution cipher. If the cipher operates on single letters, it is termed a simple substitution cipher; a cipher that operates on larger groups of letters is termed polygraphic. A monoalphabetic cipher uses fixed substitution over the entire message, whereas a polyalphabetic cipher uses a number of substitutions at different positions in the message, where a unit from the plaintext is mapped to one of several possibilities in the ciphertext and vice versa.

    Substitution of single letters separately simple substitution can be demonstrated by writing out the alphabet in some order to represent the substitution. This is termed a substitution alphabet. The cipher alphabet may be shifted or reversed (creating the Caesar and Atbash ciphers, respectively) or scrambled in a more complex fashion, in which case it is called a mixed alphabet or deranged alphabet. Traditionally, mixed alphabets may be created by first writing out a keyword, removing repeated letters in it, then writing all the remaining letters in the alphabet in the usual order.

    Using this system, the keyword "zebras" gives us the following alphabets: 

    Although the traditional keyword method for creating a mixed substitution alphabet is simple, a serious disadvantage is that the last letters of the alphabet (which are mostly low frequency) tend to stay at the end. A stronger way of constructing a mixed alphabet is to perform a columnar transposition on the ordinary alphabet using the keyword, but this is not often done.

    Although the number of possible keys is very large (26! ≈ 288.4, or about 88 bits), this cipher is not very strong, and is easily broken. Provided the message is of reasonable length (see below), the cryptanalyst can deduce the probable meaning of the most common symbols by analyzing the frequency distribution of the ciphertext. This allows formation of partial words, which can be tentatively filled in, progressively expanding the (partial) solution (see frequency analysis for a demonstration of this). In some cases, underlying words can also be determined from the pattern of their letters; for example, attract, osseous, and words with those two as the root are the only common English words with the pattern ABBCADB. Many people solve such ciphers for recreation, as with cryptogram puzzles in the newspaper.

    According to the unicity distance of English, 27.6 letters of ciphertext are required to crack a mixed alphabet simple substitution. In practice, typically about 50 letters are needed, although some messages can be broken with fewer if unusual patterns are found. In other cases, the plaintext can be contrived to have a nearly flat frequency distribution, and much longer plaintexts will then be required by the cryptanalyst.
    One once-common variant of the substitution cipher is the nomenclator. Named after the public official who announced the titles of visiting dignitaries, this cipher uses a small code sheet containing letter, syllable and word substitution tables, sometimes homophonic, that typically converted symbols into numbers. Originally the code portion was restricted to the names of important people, hence the name of the cipher; in later years it covered many common words and place names as well. The symbols for whole words (codewords in modern parlance) and letters (cipher in modern parlance) were not distinguished in the ciphertext. The Rossignols' Great Cipher used by Louis XIV of France was one. 
    Nomenclators were the standard fare of diplomatic correspondence, espionage, and advanced political conspiracy from the early fifteenth century to the late eighteenth century; most conspirators were and have remained less cryptographically sophisticated. Although government intelligence cryptanalysts were systematically breaking nomenclators by the mid-sixteenth century, and superior systems had been available since 1467, the usual response to cryptanalysis was simply to make the tables larger. By the late eighteenth century, when the system was beginning to die out, some nomenclators had 50,000 symbols.[citation needed]
    '''.format(FLAG)

    text = text.lower()
    for i in set(j for j in text):
        if i not in ascii_lowercase:
            text = text.replace(i, '')

    pixels = set()
    while len(pixels) != len(ascii_lowercase):
        pixel = (0,) * 3
        while pixel == (0,) * 3:
            pixel = (randint(0, 255), randint(0, 255), randint(0, 255))
        pixels.add(pixel)

    pixels = {ascii_lowercase[i]: j for i, j in enumerate(pixels)}
    two_pow = 1
    while two_pow * two_pow < len(text):
        two_pow *= 2
    WIDTH, HEIGHT = (two_pow,) * 2
    SIZE = (WIDTH, HEIGHT)
    im = Image.new('RGB', SIZE)

    im.putdata([pixels[i] for i in text])
    im.save(NAME_OUT)


if __name__ == '__main__':
    make()
