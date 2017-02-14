# Easy-Digraph-Draw
I just wanted to draw a simply directed graph that didn't look like shit in ubuntu, python3. Everything was broken or complicated or both, so I did this. Note: It works without the fucking gts triangulation library compile flag that people have been asking to get into the repository for ten years.

## Install, Run Example

```
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

