<p align="center">
  <h3 align="center">G FUZZ</h3>
  <p align="center">gFuzz is my fuzzing tool for websites</p>

  <p align="center">
    <a href="https://twitter.com/whoisgvb">
      <img src="https://img.shields.io/badge/twitter-@whoisgvb-red.svg">
    <a href="https://t.me/whoisgvb">
      <img src="https://img.shields.io/badge/Telegram-@whoisgvb-blue.svg">
    </a>
  </p>
</p>
<hr>

### Features
```
+ Search for directories with wordlist
+ Search directories with default wordlist (soon)
+ Search for subdomains with default or custom wordlist (soon)
+ Search with custom header (soon)
+ Search for archive ext (soon)
+ Search for directories and return your text in terminal (soon)
+ Export the data in archives (soon)
+ Error handling (soon)
```
### Install requirements
```
pip3 install --user -r requirements.txt
```

### Usage

```
Usage: gfuzz.py [OPTIONS]

Options:
-w or --wordlist  define the wordlist
-c or --code      http status code to search
-s or --site      The target URL (don't forget the http or https before)
-n or --no        Show not found URLs in terminal
-o or --open      Open the found URLs in browser
-h or --help      Help options

  ~ soon more xD
```

### Examples

```
python3 gfuzz.py -w FILENAME -s https://targeturl.com -c 200
python3 gfuzz.py -w FILENAME -s https://targeturl.com -c 200 -n -o
```

### Contact

```
[+]Email     gvbsec@protonmail.com
[+]Linkedin  linkedin.com/in/gvilela
[+]Telegram  t.me/whoisgvb
```
