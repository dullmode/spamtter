# spamtter

spamtter create favorites automatically.

# Requirement

* docker
* docker-compose
* twitter api keys(Elevated Access)

# Installation

```bash
git clone https://github.com/dullmode/spamtter.git
```

# Usage

you need to create .env file in service/
```bash
git clone https://github.com/dullmode/spamtter.git
cd spamtter/service
echo -e API_KEY=xxxxxxxx\\n\
    API_KEY_SECRET=xxxxxxxx\\n\
    ACCESS_TOKEN=xxxxxxxx\\n\
    ACCESS_TOKEN_SECRET=xxxxxxxx\\n\
    QUERY=xxxxxxxx > .env
```
QUERY is the word you want to make favorites.
then, create and run docker.
```bash
cd ../
docker-compose up --build
```

# Note

I accept no responsibility for any loss resulting from spamtter.

# License
ライセンスを明示する

spamtter is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
