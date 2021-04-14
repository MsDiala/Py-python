#Python basic operators
Operators are the constructs which can manipulate the value of operands.

## Types of Operators
- Arithmetic Operators
- Comparison (Relational) Operators
- Assignment Operators
- Logical Operators
- Bitwise Operators
- Membership Operators
- Identity Operators
<p>Let us have a look on all operators one by one.</p>
<h2>Python Arithmetic Operators</h2>
<p>Assume variable a holds 10 and variable b holds 20, then &minus;</p>
<p>
<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th>
<th style="width:45%">Description</th>
<th>Example</th>
</tr>
<tr>
<td>+ Addition</td>
<td>Adds values on either side of the operator.</td>
<td>a + b = 30</td>
</tr>
<tr>
<td>- Subtraction</td>
<td>Subtracts right hand operand from left hand operand.</td>
<td>a – b = -10</td>
</tr>
<tr>
<td>\* Multiplication</td>
<td>Multiplies values on either side of the operator</td>
<td>a * b = 200</td>
</tr>
<tr>
<td>/ Division</td>
<td>Divides left hand operand by right hand operand</td>
<td>b / a = 2</td>
</tr>
<tr>
<td>% Modulus</td>
<td>Divides left hand operand by right hand operand and returns remainder</td>
<td>b % a = 0</td>
</tr>
<tr>
<td>\*\* Exponent</td>
<td>Performs exponential (power) calculation on operators</td>
<td>a\*\*b =10 to the power 20</td>
</tr>
<tr>
<td>//</td>
<td>Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity):</td>
<td>9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0</td>
</tr>
</table>
<h2>Python Comparison Operators</h2>
<p>These operators compare the values on either sides of them and decide the relation among them. They are also called Relational operators.</p>
<p>Assume variable a holds 10 and variable b holds 20, then &minus;</p>
<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
</tr>
<tr>
<td>==</td>
<td>If the values of two operands are equal, then the condition becomes true.</td>
<td> (a == b) is not true.</td>
</tr>
<tr>
<td>!=</td>
<td>If values of two operands are not equal, then condition becomes true.</td>
</tr>
<!--<tr>
<td>&lt;&gt;</td>
<td>If values of two operands are not equal, then condition becomes true.</td>
<td> (a &lt;&gt; b) is true. This is similar to != operator.</td>
</tr>-->
<tr>
<td>&gt;</td>
<td>If the value of left operand is greater than the value of right operand, then condition becomes true.</td>
<td> (a &gt; b) is not true.</td>
</tr>
<tr>
<td>&lt;</td>
<td>If the value of left operand is less than the value of right operand, then condition becomes true.</td>
<td> (a &lt; b) is true.</td>
</tr>
<tr>
<td>&gt;=</td>
<td>If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.</td>
<td> (a &gt;= b) is not true. </td>
</tr>
<tr>
<td>&lt;=</td>
<td>If the value of left operand is less than or equal to the value of right operand, then condition becomes true.</td>
<td> (a &lt;= b) is true. </td>
</tr>
</table>
<h2>Python Assignment Operators</h2>
<p>Assume variable a holds 10 and variable b holds 20, then &minus;</p>
<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th>
<th style="width:45%">Description</th>
<th>Example</th>
</tr>
<tr>
<td>=</td>
<td>Assigns values from right side operands to left side operand</td>
<td>c = a + b assigns value of a + b into c</td>
</tr>
<tr>
<td>+=
Add AND</td>
<td>It adds right operand to the left operand and assign the result to left operand</td>
<td>c += a is equivalent to c = c + a</td>
</tr>
<tr>
<td>-=
Subtract AND</td>
<td>It subtracts right operand from the left operand and assign the result to left operand</td>
<td>c -= a is equivalent to c = c - a</td>
</tr>
<tr>
<td> \*=
Multiply AND</td>
<td>It multiplies right operand with the left operand and assign the result to left operand</td>
<td>c \*= a is equivalent to c = c \* a</td>
</tr>
<tr>
<td>/=
Divide AND</td>
<td>It divides left operand with the right operand and assign the result to left operand</td>
<td>c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a</td>
</tr>
<tr>
<td>%=
Modulus AND</td>
<td>It takes modulus using two operands and assign the result to left operand</td>
<td>c %= a is equivalent to c = c % a</td>
</tr>
<tr>
<td> \*\* =
Exponent AND</td>
<td>Performs exponential (power) calculation on operators and assign value to the left operand</td>
<td>c \*\* = a is equivalent to c = c \*\* a</td>
</tr>
<tr>
<td>//=
Floor Division</td>
<td>It performs floor division on operators and assign value to the left operand</td>
<td>c //= a is equivalent to c = c // a</td>
</tr>
</table>
<h2>Python Bitwise Operators</h2>
<p>Bitwise operator works on bits and performs bit by bit operation. Assume if a = 60; and b = 13; Now in binary format they will be as follows &minus;</p>
<p>a = 0011 1100</p>
<p>b = 0000 1101</p>
<p>-----------------</p>
<p>a&amp;b = 0000 1100</p>
<p>a|b = 0011 1101</p>
<p>a^b = 0011 0001</p>
<p>~a&nbsp; = 1100 0011</p>
<p>There are following Bitwise operators supported by Python language</p>
<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th>
<th style="width:45%">Description</th>
<th>Example</th>
</tr>
<tr>
<td>&amp; Binary AND</td>
<td>Operator copies a bit to the result if it exists in both operands </td>
<td> (a &amp; b) (means 0000 1100)</td>
</tr>
<tr>
<td>| Binary OR</td>
<td>It copies a bit if it exists in either operand.</td>
<td> (a | b) = 61 (means 0011 1101)</td>
</tr>
<tr>
<td>^ Binary XOR</td>
<td>It copies the bit if it is set in one operand but not both.</td>
<td> (a ^ b) = 49 (means 0011 0001)</td>
</tr>
<tr>
<td>~ Binary
Ones Complement</td>
<td>It is unary and has the effect of 'flipping' bits.</td>
<td> (~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.</td>
</tr>
<tr>
<td>&lt;&lt; Binary Left Shift</td>
<td>The left operands value is moved left by the number of bits specified by the right operand.</td>
<td> a &lt;&lt; = 240
(means 1111 0000)</td>
</tr>
<tr>
<td>&gt;&gt; Binary Right Shift</td>
<td>The left operands value is moved right by the number of bits specified by the right operand.</td>
<td> a &gt;&gt; = 15
(means 0000 1111)</td>
</tr>
</table>
<h2>Python Logical Operators</h2>
<p>There are following logical operators supported by Python language. Assume variable a holds 10 and variable b holds 20 then</p>
Used to reverse the logical state of its operand.
<h2>Python Membership Operators</h2>
<p>Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as explained below</p>
<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
</tr>
<tr>
<td>in</td>
<td>Evaluates to true if it finds a variable in the specified sequence and false otherwise.</td>
<td>x in y, here in results in a 1 if x is a member of sequence y.</td>
</tr>
<tr>
<td>not in</td>
<td>Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.</td>
<td>x not in y, here not in results in a 1 if x is not a member of sequence y.</td>
</tr>
</table>
<h2>Python Identity Operators</h2>
<p>Identity operators compare the memory locations of two objects. There are two Identity operators explained below:</p>
<table class="table table-bordered">
<tr>
<th style="width:10%">Operator</th><th style="width:45%">Description</th><th>Example</th>
</tr>
<tr>
<td>is</td><td>Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.</td><td> x is y, here <b>is</b> results in 1 if id(x) equals id(y).</td>
</tr>
<tr>
<td>is not</td><td>Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.</td><td> x is not y, here <b>is not</b> results in 1 if id(x) is not equal to id(y).</td>
</tr>
</table>
<h2>Python Operators Precedence</h2>
<p>The following table lists all operators from highest precedence to lowest.</p>
<table  class="table table-bordered">
<tr><th>Operator</th><th>Description</th></tr>
<tr>
<td> \*\* </td>
<td>Exponentiation (raise to the power)</td>
</tr><tr>
<td>~ + -</td>
<td>Complement, unary plus and minus (method names for the last two are +@ and -@)</td>
</tr><tr>
<td>\*/ % //</td>
<td>Multiply, divide, modulo and floor division</td>
</tr><tr>
<td>+ -</td>
<td>Addition and subtraction</td>
</tr>
<tr>
<td>&gt;&gt; &lt;&lt;</td>
<td>Right and left bitwise shift</td>
</tr><tr>
<td>&amp;</td>
<td>Bitwise 'AND'<td>
</tr>
<tr>
<td>^ |</td>
<td>Bitwise exclusive 'OR' and regular 'OR'</td>
</tr><tr>
<td>&lt;= &lt; &gt; &gt;=</td>
<td>Comparison operators</td>
</tr><tr>
<td>&lt;&gt; == !=</td>
<td>Equality operators</td>
</tr>
<tr>
<td>= %= /= //= -= +=  \*=  \*\* =</td>
<td>Assignment operators</td>
</tr>
<tr>
<td>is is not</td>
<td>Identity operators</td>
</tr>
<tr>
<td>in not in</td>
<td>Membership operators</td>
</tr><tr>
<td>not or and</td>
<td>Logical operators</td>
</tr>
</table>
