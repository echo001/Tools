# GHack
This tool allows to get subdomains from google search engine with google hack words.
GHack does not use brute-force, it just use google search engine through google hack words like site:google.com .
This tool will get subdomains and sensitive websites.
Q:Because of preventing google's bot detection,the time sleep is 5.So this tool will run slowly.

## Getting started
Please, follow the instructions below for installing and run Ghack.

### Pre-requisites
Make sure you have installed the following tools.
'''
Python 3.0 or later.
'''

### Installing
'''bash
$ git clone https://github.com/echo001/Tools/Ghack.git
$ cd Ghack
$ pip3 install -r requirements.txt

### Runing
'''bash
$ python3 ghack.py --help
'''

## Usage
Parameters and examples of use.

### Parameters
'''
-d --domain [target_domain](required)
-o --output [output_file](optional)
'''

### examples
'''bash
$ python3 ghack.py -d traderepublic.com
'''
'''bash
$ python3 ghack.py -d traderepublic.com -o results.txt

## Screenshots
<p align="center">
  <img src=" https://github.com/echo001/Tools/Ghack/png/ghack.png" />
</p>
<p align="center">
  <img src="https://github.com/echo001/Tools/Ghack/png/result.png" />
</p>

## Author
* *Echo001
