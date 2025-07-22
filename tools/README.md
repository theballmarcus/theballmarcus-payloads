# BallFuzz

## General syntax:
`F<num>Z<MODE><SUFFIX>:<OPTIONS>:Z`

## Guessing using wordlists:
1. `F1ZW:somewordlist.txt:Z`

## Guessing using integers: (Using I after first Z followed by specifications)
1. `F1ZIZ` -> Will add integer that just goes from 0 and up
3. `F1ZI:start=0,end=100,step=1:Z`
4. `F1ZI:follow=1,start=1:Z`

## Multiple FUZZ in request: (Based on the int after F)
1. `F2ZW:somewordlist.txt:Z`
2. `F3ZW:somewordlist.txt:Z`
3. `F3ZIZ` -> Will add integer that just goes from 0 and up

## Guessing characters one at a time: (Using G after Z)
1. `F1ZGZ` -> Will try one character at a time.
2. `F1ZG:set=hex:Z` -> Will try one character at a time.

## Builtin wordslists:
1. `rockyou` -> `Rockyou.txt`
2. `usernames` -> `Someusernamewodlist.txt`
3. `directories` -> `Somedirectory`

## Scripts
Scripts can be used to bypass even more restrictions. These keywords are accessible for scripts:
`shots_fired`
`shot_number`
`response`
Include a python script file like
```python
if shot_number == 3:
    print(response.text)
``` 