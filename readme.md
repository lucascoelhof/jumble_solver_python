# Jumble Solver

Given a file with a list of words (e.g. [this](https://github.com/dwyl/english-words)) and an English word, it will find all [Jumble](https://en.wikipedia.org/wiki/Jumble) solutions for it, including substrings and anagrams.

# Usage
``` bash
python3 jumble.py [-h] word_list word
```
Positional arguments
* *word_list*: File containing a list of words, one per line
* *word*: Word used to find Jumble solutions

On this repository, there is a example word list file, from [this repo](https://github.com/dwyl/english-words).

# Example

Using words.txt and dog as arguments, we get the following output:
```
$ python3 jumble.py words.txt dog
do
od
dg
gd
go
og
god
```

# Implementation
As a reference for the time complexity, I've used [this official Python page](https://wiki.python.org/moin/TimeComplexity) and [these lecture notes](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt).
I've separated the code into the following parts:

## main
Parses the arguments, calls the [parse_word_list_file](#parse_word_list_file) and [jumble](#jumble) functions, then prints the result.

## parse_word_list_file
Creates a jumble dictionary from a file containing a list of words. The keys of this _dict_ are lowercase words with their letters sorted alphabetically, while the values are a list of original words. Storing the lowercase sorted words as the key ensures we will find anagrams with O(1) using Python _dict_.

## jumble
Given the Jumble _dict_ object and an input word, it will search for all jumble solutions for this word. Since we also want to search for substrings, it first finds the unique combinations of all letters for the input, from 2 to input word length. For each combination, we sort it and remove any whitespaces, then search on our jumble dictionary. If we find the sorted word on the jumble _dict_, we then merge the original words list our temporary _dict_ object. We use it to avoid duplicates. The implementation of [itertools.combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations) returns unique combinations considering the **position**, not the value of the element. For example, the word "robot" would give the combination "ot" two times. However, as we will see in [Complexity Analysis](#complexity-analysis) section, the complexity of this code scales exponentially with the size of the input word, and the insertion on a _dict_ is constant. So, in terms of time complexity, it is better to not remove the duplicates and let _dict_ deal with the duplicates, because it has an O(1) index and store complexity.


# Complexity analysis

Consider N the number of words on file and S the length of a given word. On [parse_word_list_file](#parse_word_list_file) function, we iterate over all words in file O(N) and run the following operations with their given complexity:
1. strip: O(S)
2. lower: O(S)
3. sorted: O(S log S)
4. setdefault: O(1)
5. append: O(1)

Given that, the complexity of parse_word_list_file function is: 

O(N) \* (O(S) + O(S) + O(S log S) + O(1)) = O(N \* (2S + S log S + 1)) = O(2NS + NS log S + N) = O(NS log S)

[The average word length in English is 4.7 ~= 5 characters](https://wolfgarbe.medium.com/the-average-word-length-in-english-language-is-4-7-35750344870f#:~:text=The%20average%20word%20length%20in%20English%20language%20is%204.7%20characters), so by replacling we get:

O(N 5 log 5) = **O(N)**


On [jumble](#jumble), consider L the length of the input word, R the combination size, N the number of words from the input file, and [C() the choose operator](https://en.wikipedia.org/wiki/Combination#Number_of_k-combinations). Then, we do the following operations:
* Loop R from 2 to input word length: so O(L-1) = O(L)
  * Find the combinations, and iterate over their result: [O(C(L,R)\*R)](https://stackoverflow.com/questions/53419536/what-is-the-computational-complexity-of-itertools-combinations-in-python)
    * For each combination, we lower and sort, worst case it has length L: O(L) + O*(L log L)
    * Then we search for the word on the jumble dict: O(1)
    * Append the result to another list: O(1)

Thus, the final complexity of jumble is O(L) \* O(C(L, R) \* R) \* (O*(L log L) + O(L) + O(1) + O(1))).
But, from R=1 to L, the complexity of O(L)\*O(C(L,R)\*R) is O(2^L -1), [and from R=2 to L](https://www.wolframalpha.com/input/?i=sum+k%3D2+to+n+n%21%2F%28%28k%29%21*%28n-k%29%21%29), O(2^L-L-1) = O(2^L). Then, simplifying the complexity of jumble, we get:
O(2^L) \* (O(L log L) + O(L) + O(1) + O(1)) = **O(2^L * L log L)**

On main, we iterate over the results from jumble and print. In worst case, we have all words from the initial file, so for printing the results we would have an O(N) complexity. Finally, adding main, jumble, and parse_word_list_file complexities, we get:

O(N) + O(N) + O(2^L * L log L)  = **O(N) + O(2^L * L log L)**
