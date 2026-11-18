class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        result = []
        
        # Iterate over each offset to handle all possible word alignments
        for i in range(word_len):
            left = i
            current_count = defaultdict(int)
            matched = 0
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_count:
                    current_count[word] += 1
                    matched += 1
                    
                    # If we have more instances of a word than needed, shrink from left
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        matched -= 1
                        left += word_len
                    
                    # If matched count equals total words, we found a valid starting index
                    if matched == num_words:
                        result.append(left)
                else:
                    # Reset window if word is not in words list
                    current_count.clear()
                    matched = 0
                    left = right + word_len
                    
        return result