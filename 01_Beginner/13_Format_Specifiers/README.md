## Format Specifiers in Python


### Format Specifiers in f-strings

Format specifiers, when used within the context of an f-string, allow for the formatting of a value based on specific flags. These flags determine how the value is displayed, including the number of decimal places, alignment, padding, and more.

#### Basic Syntax

The basic syntax for using a format specifier in an f-string is as follows:

```python
f"{value:flags}"
```

Here, `value` is the variable you want to format, and `flags` represent the formatting options.

### Practical Examples

Let’s explore various format specifiers with practical examples.

#### Initializing Values

First, we will initialize three price values:

```python
price1 = 3.14159
price2 = -987.65
price3 = 12.34
```

#### Displaying Prices with f-strings

To display the prices using f-strings, we can simply place the variables inside the f-string placeholders:

```python
print(f"Price 1 is {price1}")
print(f"Price 2 is {price2}")
print(f"Price 3 is {price3}")
```

#### Adding Decimal Precision

To format the prices to two decimal places, we use the `.2f` specifier:

```python
print(f"Price 1 is {price1:.2f}")
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.2f}")
```

Output:
```
Price 1 is 3.14
Price 2 is -987.65
Price 3 is 12.34
```

#### Adding Dollar Signs

We can enhance the readability by adding dollar signs:

```python
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")
```

Output:
```
Price 1 is $3.14
Price 2 is $-987.65
Price 3 is $12.34
```

#### Adjusting Decimal Precision

For one decimal place, use `.1f`:

```python
print(f"Price 1 is ${price1:.1f}")
print(f"Price 2 is ${price2:.1f}")
print(f"Price 3 is ${price3:.1f}")
```

Output:
```
Price 1 is $3.1
Price 2 is $-987.7
Price 3 is $12.3
```

For three decimal places, use `.3f`:

```python
print(f"Price 1 is ${price1:.3f}")
print(f"Price 2 is ${price2:.3f}")
print(f"Price 3 is ${price3:.3f}")
```

Output:
```
Price 1 is $3.142
Price 2 is $-987.650
Price 3 is $12.340
```

#### Allocating Space for Values

To allocate space, specify the total width after the colon. For example, to allocate 10 spaces:

```python
print(f"Price 1 is ${price1:10.2f}")
print(f"Price 2 is ${price2:10.2f}")
print(f"Price 3 is ${price3:10.2f}")
```

Output:
```
Price 1 is $      3.14
Price 2 is $   -987.65
Price 3 is $     12.34
```

#### Zero Padding Values

For zero-padding, precede the width with a zero:

```python
print(f"Price 1 is ${price1:010.2f}")
print(f"Price 2 is ${price2:010.2f}")
print(f"Price 3 is ${price3:010.2f}")
```

Output:
```
Price 1 is $000003.14
Price 2 is $-000987.65
Price 3 is $000012.34
```

#### Justifying Values

To left-justify, use `<`:

```python
print(f"Price 1 is ${price1:<10.2f}")
print(f"Price 2 is ${price2:<10.2f}")
print(f"Price 3 is ${price3:<10.2f}")
```

Output:
```
Price 1 is $3.14      
Price 2 is $-987.65   
Price 3 is $12.34     
```

To right-justify (default), use `>`:

```python
print(f"Price 1 is ${price1:>10.2f}")
print(f"Price 2 is ${price2:>10.2f}")
print(f"Price 3 is ${price3:>10.2f}")
```

Output:
```
Price 1 is $      3.14
Price 2 is $   -987.65
Price 3 is $     12.34
```

To center-align, use `^`:

```python
print(f"Price 1 is ${price1:^10.2f}")
print(f"Price 2 is ${price2:^10.2f}")
print(f"Price 3 is ${price3:^10.2f}")
```

Output:
```
Price 1 is $   3.14   
Price 2 is $ -987.65  
Price 3 is $  12.34   
```

#### Adding Signs

To display a plus sign for positive values, use `+`:

```python
print(f"Price 1 is ${price1:+.2f}")
print(f"Price 2 is ${price2:+.2f}")
print(f"Price 3 is ${price3:+.2f}")
```

Output:
```
Price 1 is $+3.14
Price 2 is $-987.65
Price 3 is $+12.34
```

To use a space for positive values, use a space:

```python
print(f"Price 1 is ${price1: .2f}")
print(f"Price 2 is ${price2: .2f}")
print(f"Price 3 is ${price3: .2f}")
```

Output:
```
Price 1 is $ 3.14
Price 2 is $-987.65
Price 3 is $ 12.34
```

#### Adding Thousand Separators

To add thousand separators, use a comma:

```python
price1 = 3000
price2 = -9871.23
price3 = 1200.45

print(f"Price 1 is ${price1:,.2f}")
print(f"Price 2 is ${price2:,.2f}")
print(f"Price 3 is ${price3:,.2f}")
```

Output:
```
Price 1 is $3,000.00
Price 2 is $-9,871.23
Price 3 is $1,200.45
```

#### Combining Flags

Format specifiers can be combined to achieve complex formatting. For example, to include a thousand separator, two decimal places, and a plus sign:

```python
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")
```

Output:
```
Price 1 is $+3,000.00
Price 2 is $-9,871.23
Price 3 is $+1,200.45
```

