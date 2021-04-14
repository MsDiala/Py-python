# Regular Expressions in Python
## Introduction
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern.

The `re` module was added in Python 1.5, and provides **Perl-style** regular expression patterns. Earlier versions of Python came with the `regex` module, which provided **Emacs-style** patterns. The regex module was removed completely in Python 2.5.

## Using Regular Expressions
### The <b>match</b> function
searches for a match in `re` pattern to string with two optional flags.
The syntax is:
```python
import re
re.match(pattern,string,flags= 0)
```
#### <u>Parameter Description</u>:
<table>
<tbody>
<tr>
<th>Parameter</th>
<th>Description</th>
</tr>
<tr>
<td>pattern</td>
<td>This is the regular expression to be matched.</td>
</tr>
<tr>
<td>string</td>
<td>This is the string, which would be searched to match the pattern at the beginning of string.</td>
</tr>
<tr>
<td>flags</td>
<td>You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.</td>
</tr>
</tbody>
</table>

<table>
<tbody><tr>
<th>Match Object Methods</th>
<th>Description</th>
</tr>
<tr><td>group(num=0)</td><td>This method returns entire match (or specific subgroup num)</td></tr>
<tr>
<td>groups()</td>
<td>This method returns all matching subgroups in a tuple (empty if there weren't any)</td>
</tr></tbody>
</table>

The `re.match` return match object if successful else returns `None`

#### Example
```python
#!/usr/bin/python
import re

line = "Tigers are smarter than Lions"

mat = re.match( r'(.*) than (.*?) .*', line, re.M|re.I)

if mat:
   print "mat.group() : ", mat.group()
   print "mat.group(1) : ", mat.group(1)
   print "mat.group(2) : ", mat.group(2)
else:
   print "No match!!"
```
when executed the ouput will be
```
mat.group() :  Tigers are smarter than Lions
mat.group(1) :  smarter
mat.group(2) :  Lions
```
### The <b>search</b> function
searches for the first occurence of `re` pattern within string with optional flags.

Syntax:
```python
import re
re.search(pattern, string, flags=0)
```
#### <u>Parameter Description</u>:
<table>
<tbody><tr>
<th>Parameter</th><th>Description</th>
</tr>
<tr><td>pattern</td><td>This is the regular expression to be matched.</td></tr>
<tr><td>string</td><td>This is the string, which would be searched to match the pattern anywhere in the string.</td></tr>
<tr><td>flags</td><td>You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.</td></tr>
</tbody></table>

<table>
<tbody><tr>
<th>Match Object Methods</th><th>Description</th>
</tr>
<tr><td>group(num=0)</td><td>This method returns entire match (or specific subgroup num)</td></tr>
<tr><td>groups()</td><td>This method returns all matching subgroups in a tuple (empty if there weren't any)</td></tr>
</tbody></table>

The `re.search` returns a match object if successful else returns `None`.
#### Example
```python
#!/usr/bin/python
import re

line = "Tigers are smarter than Lions";

searc = re.search( r'(.*) than (.*?) .*', line, re.M|re.I)

if searc:
   print "searc.group() : ", searc.group()
   print "searc.group(1) : ", searc.group(1)
   print "searc.group(2) : ", searc.group(2)
else:
   print "Nothing found!!"
```
The output will be like
```
searc.group() :  Tigers are smarter than Lions
searchObj.group(1) :  samrter
searchObj.group(2) :  Lions
```
### The <b>sub</b> function
searches for `re` pattern and replaces it with user specified string in the given string.

Syntax
```python
import re
re.sub(pattern, repl, string, max=0)
```
#### Example
```python
#!/usr/bin/python
import re
phone = "8500-451-999 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num
# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print "Phone Num : ", num
```
Output
```
Phone Num :  8500-451-999
Phone Num :  8500451999
```
### The <b>findall</b> function
The expression `re.findall()` returns all the non-overlapping matches of patterns in a string as a list of strings.

Syntax
```python
import re
re.findall(r'pattern',string)
```
#### Example
```python
import re
print(re.findall(r'\w','Greycampus'))
```
Output
```python
['G', 'r', 'e', 'y', 'c', 'a', 'm', 'p', 'u', 's']
```
### The <b>split</b> function
The `re.split()` expression splits the string by occurrence of a pattern.

Syntax
```python
import re
re.split(pattern,string)
```
#### Example
```python
import re
print(re.split(r'-','Greycampus-Python'))
```
Output
```python
['Greycampus', 'Python']
```
### The `start` and `end` functions
These expressions return the indices of the `start` and `end` of the substring matched by the group.
#### Example
```python
import re
k = re.search(r'\d+','13vv1a1238')
k.end()
k.start()
```
ouput
```
2
0
```
### Regular Expression Modifiers: Option Flags
<table>
<tbody><tr><th>Modifier</th><th>Description</th></tr>
<tr><td>re.I</td><td>Performs case-insensitive matching.</td></tr>
<tr><td>re.L</td><td>Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior
(\b and \B).</td></tr>
<tr><td>re.M</td><td>Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).</td></tr>
<tr><td>re.S</td><td>Makes a period (dot) match any character, including a newline.</td></tr>
<tr><td>re.U</td><td>Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.</td></tr>
<tr><td>re.X</td><td>Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.</td></tr>
</tbody></table>

### Regular Expression Patterns
Except control characters  + ? . * ^ $ ( ) [ ] { } | \ all characters match themselves. You can escape a control character by preceeding it with a backslash.

<table>
<tbody><tr><th>Pattern</th><th>Description</th></tr>
<tr><td>^</td><td>Matches beginning of line.</td></tr>
<tr><td>$</td><td>Matches end of line.</td></tr>
<tr><td>.</td><td>Matches any single character except newline. Using m option allows it to match newline as well.</td></tr>
<tr><td>[...]</td><td>Matches any single character in brackets.</td></tr>
<tr><td>[^...]</td><td>Matches any single character not in brackets</td></tr>
<tr><td>re*</td><td>Matches 0 or more occurrences of preceding expression.</td></tr>
<tr><td>re+</td><td>Matches 1 or more occurrence of preceding expression.</td></tr>
<tr><td>re?</td><td>Matches 0 or 1 occurrence of preceding expression.</td></tr>
<tr><td>re{ n}</td><td>Matches exactly n number of occurrences of preceding expression.</td></tr>
<tr><td>re{ n,}</td><td>Matches n or more occurrences of preceding expression.</td></tr>
<tr><td>re{ n, m}</td><td>Matches at least n and at most m occurrences of preceding expression.</td></tr>
<tr><td>a| b</td><td>Matches either a or b.</td></tr>
<tr><td>(re)</td><td>Groups regular expressions and remembers matched text.</td></tr>
<tr><td>(?imx)</td><td>Temporarily toggles on i, m, or x options within a regular expression. If in parentheses, only that area is affected.</td></tr>
<tr><td>(?-imx)</td><td>Temporarily toggles off i, m, or x options within a regular expression. If in parentheses, only that area is affected.</td></tr>
<tr><td>(?: re)</td><td>Groups regular expressions without remembering matched text.</td></tr>
<tr><td>(?imx: re)</td><td>Temporarily toggles on i, m, or x options within parentheses.</td></tr>
<tr><td>(?-imx: re)</td><td>Temporarily toggles off i, m, or x options within parentheses.</td></tr>
<tr><td>(?#...)</td><td>Comment.</td></tr>
<tr><td>(?= re)</td><td>Specifies position using a pattern. Doesn't have a range.</td></tr>
<tr><td>(?! re)</td><td>Specifies position using pattern negation. Doesn't have a range.</td></tr>
<tr><td>(?>; re)</td><td>Matches independent pattern without backtracking.</td></tr>
<tr><td>\w</td><td>Matches word characters.</td></tr>
<tr><td>\W</td><td>Matches nonword characters.</td></tr>
<tr><td>\s</td><td>Matches whitespace. Equivalent to [\t\n\r\f].</td></tr>
<tr><td>\S</td><td>Matches nonwhitespace.</td></tr>
<tr><td>\d</td><td>Matches digits. Equivalent to [0-9].</td></tr>
<tr><td>\D</td><td>Matches nondigits.</td></tr>
<tr><td>\A</td><td>Matches beginning of string.</td></tr>
<tr><td>\Z</td><td>Matches end of string. If a newline exists, it matches just before newline.</td></tr>
<tr><td>\z</td><td>Matches end of string.</td></tr>
<tr><td>\G</td><td>Matches point where last match finished.</td></tr>
<tr><td>\b</td><td>Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets.</td></tr>
<tr><td>\B</td><td>Matches nonword boundaries.</td></tr>
<tr><td>\n, \t, etc.</td><td>Matches newlines, carriage returns, tabs, etc.</td></tr>
<tr><td>\1...\9</td><td>Matches nth grouped subexpression.</td></tr>
<tr><td>\10</td><td>Matches n<sup>th</sup> grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.</td></tr>
</tbody></table>

### Character classes

<table>
<tbody><tr><th>Example</th><th>Description</th></tr>
<tr><td>[Pp]ython </td><td>Match "Python" or "python"</td></tr>
<tr><td>rub[ye]</td><td>Match "ruby" or "rube"</td></tr>
<tr><td>[aeiou]</td><td>Match any one lowercase vowel</td></tr>
<tr><td>[0-9]</td><td>Match any digit; same as [0123456789]</td></tr>
<tr><td>[a-z]</td><td>Match any lowercase ASCII letter</td></tr>
<tr><td>[A-Z]</td><td>Match any uppercase ASCII letter</td></tr>
<tr><td>[a-zA-Z0-9]</td><td>Match any of the above</td></tr>
<tr><td>[^aeiou]</td><td>Match anything other than a lowercase vowel</td></tr>
<tr><td>[^0-9]</td><td>Match anything other than a digit</td></tr>
</tbody></table>

### Special Character classes

<table>
<tbody><tr><th>Example</th><th>Description</th></tr>
<tr><td>.</td><td>Match any character except newline</td></tr>
<tr><td>\d</td><td>Match a digit: [0-9]</td></tr>
<tr><td>\D </td><td>Match a nondigit: [^0-9]</td></tr>
<tr><td>\s</td><td>Match a whitespace character: [ \t\r\n\f]</td></tr>
<tr><td>\S</td><td>Match nonwhitespace: [^ \t\r\n\f]</td></tr>
<tr><td>\w</td><td>Match a single word character: [A-Za-z0-9_]</td></tr>
<tr><td>\W</td><td>Match a nonword character: [^A-Za-z0-9_]</td></tr>
</tbody></table>

### Repetition cases

<table>
<tbody><tr><th>Example</th><th>Description</th></tr>
<tr><td>python? </td><td>Match "pytho" or "python": the n is optional</td></tr>
<tr><td>ruby* </td><td>Match "rub" plus 0 or more ys</td></tr>
<tr><td>python+</td><td>Match "pytho" plus 1 or more ns</td></tr>
<tr><td>\d{5}</td><td>Match exactly 5 digits</td></tr>
<tr><td>\d{3,}</td><td>Match 3 or more digits</td></tr>
<tr><td>\d{6,8}</td><td>Match 6, 7, or 8 digits</td></tr>
</tbody></table>
