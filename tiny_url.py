# LeetCode
# tiny_url 
# Created by Yigang Zhou on 2020/9/26.
# Copyright © 2020 Yigang Zhou. All rights reserved.

class Codec:
    # 62
    alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H', 'I', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                'Z']
    x = 62

    def __init__(self):
        self.count = 1
        self.url_dict = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        c = self.count
        encoded = ''
        while c > 0:
            idx = c % self.x
            encoded = self.alphabet[idx] + encoded
            c = c // self.x

        self.url_dict[encoded] = longUrl
        self.count += 1
        # print(encoded)
        return encoded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.url_dict:
            return self.url_dict[shortUrl]
        return ""

# Your Codec object will be instantiated and called as such:
url = '12213123'
codec = Codec()
codec.decode(codec.encode(url))
