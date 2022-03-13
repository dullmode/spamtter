# spamtter

spamtter create favorites automatically and regurally

# Requirement

* python3
* tweepy==3.9.0
* twitter api keys(Elevated Access)

# Installation

```bash
git clone https://github.com/dullmode/spamtter.git
```

# Usage

you need to create .env file in service/
```bash
git clone https://github.com/dullmode/spamtter.git

cd spamtter/

echo -e API_KEY=xxxxxxxx\\n\
    API_KEY_SECRET=xxxxxxxx\\n\
    ACCESS_TOKEN=xxxxxxxx\\n\
    ACCESS_TOKEN_SECRET=xxxxxxxx\\n\
    COUNT=40\\n\
    INTERVAL=3600\\n\
    QUERY=xxxxxxxx > service/.env
```
* QUERY is the word you want to make favorites.
* COUNT is number of tweets you search.
* INTERVAL is time to excute program regurally.


then, create and run docker.
```bash
python3 service/main.py
```

# Note

I accept no responsibility for any loss resulting from spamtter.

# License

spamtter is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
