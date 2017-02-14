# Easy-Digraph-Draw
I just wanted to draw a simply directed graph that didn't look like shit in ubuntu, python3. Everything was broken or complicated or both, so I did this. Note: It works without the fucking gts triangulation library compile flag that people have been asking to get into the repository for ten years.

## Install, Run Example

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

## Examples

![example 0](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/ABC.png "Example 0")
![example 1](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/1.png "Example 1")
![example 2](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/2.png "Example 2")
![example 3](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/3.png "Example 3")
![example 4](https://github.com/darkhipo/Easy-Digraph-Draw/blob/master/examples/4.png "Example 4")
