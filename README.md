# recursive task sample

## dependencies
- python3
- flask (app.py)


## how to try this

```sh
./app.py >/dev/null & PID=$! && sleep 5 && ansible-playbook site.yml && sleep 5 ; kill $PID
```


## app.py

- binded: 0.0.0.0:34000
- GET /home
    - returned:
```
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
```
- GET /home?next=20
    - returned:
```
[20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
```
