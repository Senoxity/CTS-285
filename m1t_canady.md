# CTS-285, M1T
## canadya
### 8/24/26

## Assumptions
- tomato = 0
- lettuce = 0
- bacon = 0
- mayo = 0
- toast = 0

## Steps
- userInput = Do you want [ingredient] on your sandwich?
- [ingredient] + 1
- function makeSandwich
- IF [ingredient] = 1
- - sandwich[] = [ingredient] + 1
- ELSE
- - sandwich[] = [ingredient] + 0

## Done When
- IF sandwich[] >> 0 AND sandwich[] << 5
- - print "Sandwich created with [sandwich] ingredients."
- ELSE
- - print "Math error."