# Seer
`seer` is a tool that recognizes the architecture of a binary file and visualizes a windrose chart for a visual comparison. See the [images](images) directory for diagram samples.

## How does it work?
> Each processor architecture has a unique byte histogram fingerprint, which others have described previously. This is because in machine code some types of opcodes are used more frequently than others (Register/memory move, comparison, jump/branch/call are usually the most common.)
> This gives each architecture a unique balance of bytes reflecting the designer’s choice of representation of common and uncommon opcodes. [1]

## Requirements
- Python3 
- Plotly
- SciPy

## Usage
```
$ pip3 install -r requirements.txt

$ python3 seer.py -h
usage: seer.py [-h] [-w] filename

positional arguments:
  filename        binary to analyze

optional arguments:
  -h, --help      show this help message and exit
  -w, --windrose  show windrose chart
```

## Example

```
$ python3 seer.py ~/vx5 
MIPS32          99
MIPS64          77
SH4             70
ARM64           60
M68K            59
PPC32           57
I686            53
ARM32           52
PPC64           50
X86_64          46
```

## Notes
[1] Based on [Windrose Fingerprinting of Code Architecture](https://github.com/angea/pocorgtfo/blob/master/contents/articles/21-11.pdf) [PDF] (PoC||GTFO 0x21)