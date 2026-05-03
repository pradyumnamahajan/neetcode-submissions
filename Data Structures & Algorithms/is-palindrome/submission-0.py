class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized_arr = []
        for char in s:
            is_valid = (ord(char) >= ord('A') and ord(char) <= ord('Z')) or \
                    (ord(char) >= ord('a') and ord(char) <= ord('z')) or \
                    (ord(char) >= ord('0') and ord(char) <= ord('9'))

            if is_valid:
                sanitized_arr.append(char)
        
        sanitized_str = "".join(sanitized_arr).lower()
        sanitized_arr.reverse()
        reverse_sanitized_str = "".join(sanitized_arr).lower()

        return sanitized_str == reverse_sanitized_str 