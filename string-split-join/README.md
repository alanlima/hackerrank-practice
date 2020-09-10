# Problem

**Source: [HackerRank String Split and Join](https://www.hackerrank.com/challenges/python-string-split-and-join/problem)**

In Python, a string can be split on a delimiter.

## Example

```python
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings.
>>> print a
['this', 'is', 'a', 'string']
```

Joing a string is simple:

```python
>>> a = "-".join(a)
>>> print a
this-is-a-string
```

## Task

You are given a string. Split the string on a `" "` (space) delimiter and join using a `-` hyphen.

## Input Format

The first line contains a string consisting of space separared words.

## Output Format

Print the formatted string as explained above.

## Sample Input

```text
this is a string
```

## Sample Output

```text
this-is-a-string
```
