Fastapi tutorial.



Operating systems is WSL-2 Ubuntu-24.04.

sudo apt install python3.12-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt ( add these lines fastapi uvicorn httpie requests httpx)
pip install -r requirements-dev.txt ( black  ruff)

pip install "fastapi[standard]"   # command line  uvicorn main:app --reload

# set the variable ( not sure it this is needed or not)
export PYTHONPATH=$PWD/src

"python main.py &"  # this still takes the terminal with python , but it has uvicorn running in the background, and was hard to   #kill
```
  223  ps aux | grep uvicorn
  224  kill 20440
  225  ps aux | grep uvicorn
  226  kill 20757
  227  ps aux | grep uvicorn
  228  ps aux
  229  ps aux | grep uvicorn
  230  python main.py
  231  psaux
  232  ps
  233  ps aux
  234  ps aux | grep sgromme
  235  ps aux | grep uvicorn
  236  pkill -f "uvicorn"
  237  ps aux | grep uvicorn
  238  python main.py
  239  lsof -i :8000
  240  kill 16126
  241  kill 16129
  242  lsof -i :8000
  ```


  ps aux | grep uvicorn | grep -v grep  # so you don't see the grep running

ways to test:
    browser and navigate to localhost:8000
    cmd line http localhost:8000/ or http -b  localhost:8000/
    cmd line httpx  http://127.0.0.1:8000
    curl http://127.0.0.1:8000  or curl -v http://127.0.0.1:8000/

# HTTP request and response headers
http -p HBh http://example.com/

# Multiple Routers










