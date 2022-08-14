# CTHack
This tool will get subdomains from Certificate Transparency.It's different from subdomains brute froce,just as a supplement.

## Getting started
Please, follow the instructions below for installing and run CThack.

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
  <img src=" https://github.com/echo001/Tools/CThack/png/cthack.png" />
</p>
<p align="center">
  <img src="https://github.com/echo001/Tools/CThack/png/result.png" />
</p>

## Author
* *Echo001
