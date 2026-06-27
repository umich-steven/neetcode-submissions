class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            count = 0
            word_encode = ""
            for letter in word:
                numeric = ord(letter)
                word_encode += str(numeric) + '-'
                count += 1
            encode += "?" + str(count) + '#' + word_encode 
        return encode[:-1]

            

    def decode(self, s: str) -> List[str]:
        cleaned_str = [w for w in s.strip("?").split("?") if w]
        decode_word = []
        
        for word in cleaned_str:
            parts = word.split("#")
    
            count = int(parts[0])

            if count == 0:
                decode_word.append("")
                continue

            letters = parts[1].split("-")
            full_word = ""

            for letter in letters:
                if letter:
                    full_word += chr(int(letter))

            decode_word.append(full_word)


        return decode_word




