# Easy-Digraph-Draw
I just wanted to draw a simply directed graph that didn't look like shit in ubuntu, python3. Everything was broken or complicated or both, so I did this. Note: It works without the fucking gts triangulation library compile flag that people have been asking to get into the repository for ten years.

## Install, Run Example

### Ubuntu 16.04
```bash
sudo apt-get install python3
sudo apt-get install python3-venv
cd ~/Easy-Digraph-Draw/
python3 -m venv ./my-venv
source ./my-venv/bin/activate
pip3 install graphviz
pip3 install pygraphviz
python3 ./gviz_simple.py
deactivate
```

### Win 7 AMD64
* Install [Anaconda for Win AMD64, Python3][CONDA_WIN_AMD64_PY3].
* Install [graphviz for Win][GRAPHVIZ_4_WIN]. 
* Download [pygraphviz-1.3.1-cp34-none-win_amd64.whl][CONDA_WIN_AMD64_PY34_PYGRAPHVIZ].
* Create a Conda environment with Python version 3.4: `conda create --name digraphs python=3.4 anaconda`.
* Enter the environment: `activate digraphs`.
* Install pygraphviz using pip3: `pip3 install pygraphviz-1.3.1-cp34-none-win_amd64.whl`.
* Run example: `python3 ./gviz_simple.py`.
* Exit the environment: `deactivate`

## Examples

![example 0](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/ABC.png "Example 0")
![example 1](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/1.png "Example 1")
![example 2](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/2.png "Example 2")
![example 3](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/3.png "Example 3")
![example 4](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/4.png "Example 4")

[CONDA_WIN_AMD64_PY3]: https://repo.continuum.io/archive/Anaconda3-4.4.0-Windows-x86_64.exe
[CONDA_WIN_AMD64_PY34_PYGRAPHVIZ]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygraphviz
[GRAPHVIZ_4_WIN]: http://www.graphviz.org/Download_windows.php
