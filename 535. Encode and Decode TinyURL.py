'''
Problem:

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl 
and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

'''



'''
Solution:

It's possible that a randomly generated code has already been generated before. In that case, another random code is generated instead. 
Repeat until we have a code that's not already in use. 

How long can this take? Well, even if we get up to using half of the code space, which is a whopping 626/2 = 28,400,117,792 entries, 
then each code has a 50% chance of not having appeared yet. So the expected/average number of attempts is 2, 
and for example only one in a billion URLs takes more than 30 attempts. 

If we get to an even larger number of entries, then we can just use length 7 as we'd be running out of available codes.


Performance Analysis:

The number of URLs that can be encoded is quite large in this case, nearly of the order (10+26∗2)^6.

The length of the encoded URLs is fixed to 6 units, which is a significant reduction for very large URLs.

The performance of this scheme is quite good, due to a very less probability of repeated same codes generated.

We can increase the number of encodings possible as well, by increasing the length of the encoded strings. Thus, there exists a tradeoff between the length of the code and the number of encodings possible.

Predicting the encoding isn't possible in this scheme since random numbers are used.

'''



class Codec:

    alphanum = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

   
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:    # repeatly try until successfully encode the long URL to code and store it in the 2 dicts
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]


