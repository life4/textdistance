# Algorithms

* **h -- hamming: substitution**. Compute the Hamming distance between the two or more sequences. The Hamming distance is the number of differing items in ordered sequences.
* **l -- levenstein: deletion, insertion, substitution**. Compute the absolute Levenshtein distance between the two sequences. The Levenshtein distance is the minimum number of edit operations necessary for transforming one sequence into the other.
* **dl -- damerau-levenshtein: deletion, insertion, substitution, transposition**. Compute the absolute Damerau-Levenshtein distance between the two sequences. The Levenshtein distance is the minimum number of edit operations necessary for transforming one sequence into the other.
* **s -- sorensen**. Compute the Sorensen distance between the two sequences. They should contain hashable items. The return value is a float between 0 and 1, where 0 means equal, and 1 totally different.
* **j -- jaccard**. Compute the Jaccard distance between the two sequences. They should contain hashable items. The return value is a float between 0 and 1, where 0 means equal, and 1 totally different.

# Installation

```bash
sudo pip3 install textdistance
```

# Usage

## Importing

```python
>>> from textdistance import distance

```

## Hamming

```python
>>> distance('h', 'lorem', 'lorum')
1
>>> distance('h', 'lorem', 'loremus')
2
>>> distance('h', 'lorem', 'lorimus')
3
>>> distance('h', 'lorimus', 'larem')
4
>>> distance.h(lorimus', 'larem')
4
```

## Sorensen

```python
>>> distance('s', 'lorem', 'lorem')
0.0
>>> distance('s', 'lorem', 'lorum')
0.19999999999999996
>>> distance('s', 'lorem', 'lorme')
0.0
>>> distance('s', 'lorem', 'melor')
0.0
>>> distance('s', 'lorem', 'loremus')
0.16666666666666663
>>> distance.s('lorem', 'loremus')
0.16666666666666663
```

## Jaccard

```python
>>> distance('j', 'lorem', 'lorem')
0.0
>>> distance('j', 'lorem', 'lorum')
0.33333333333333337
>>> distance('j', 'lorem', 'lorme')
0.0
>>> distance('j', 'lorem', 'melor')
0.0
>>> distance('j', 'lorem', 'loremus')
0.2857142857142857
>>> distance.j('lorem', 'loremus')
0.2857142857142857
```

## Levenstein

```python
>>> distance('l', 'lorem', 'lorim')
1
>>> #substitution
... distance('l', 'lorem', 'lorim')
1
>>> #insertion
... distance('l', 'lorem', 'loriem')
1
>>> #deletion
... distance('l', 'lorem', 'lrem')
1
>>> distance.l('lorem', 'lrem')
1
```

## Damerau-Levenshtein

```python
>>> distance('dl', 'lorem', 'lorim')
1
>>> #substitution
... distance('dl', 'lorem', 'lorim')
1
>>> #insertion
... distance('dl', 'lorem', 'loriem')
1
>>> #deletion
... distance('dl', 'lorem', 'lrem')
1
>>> #transposition
... distance('dl', 'lorem', 'lorme')
1
>>> distance.dl('lorem', 'lorme')
1
```

## Test with words permutations

```python
>>> distance('dlw', 'lorem ipsum', 'ipsum lorum')
1
>>> distance('dlw', 'lorem ipsum dolor', 'ipsum lorum')
7
>>> distance('dlwe', 'lorem ipsum dolor', 'ipsum lorum')
1
```

## Find minimal text by distance

```python
>>> distance.find_minimal('h', 'lorem', ['larum', 'lorum'])
(1, 'lorum')
```
