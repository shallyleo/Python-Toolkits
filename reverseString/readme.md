# Reverse a String

This program takes a string as input and prints its reverse.

## Usage

Run the following code to reverse a string:

```python
stringInp = str(input("Input a word: "))
print("Your input is : " + stringInp)

reversedString = ""
i = len(stringInp)
while i >= 1:
  reversedString+=(stringInp[i-1])
  i -=1
print("The reverse is: " + reversedString.lower())
```

## Example

Input: Hello, World!
Output: !dlrow ,olleh

## Explanation

The code first takes a string as input using the `input()` function. Then, it creates an empty string called `reversedString`. It then iterates over the input string in reverse order, appending each character to the `reversedString`. Finally, it prints the `reversedString`.

## License

This code is licensed under the MIT License. This means that you are free to use, modify, and distribute the code for any purpose, as long as you include the original copyright notice and license in any copies you distribute.

## Contact

If you have any questions or feedback, please feel free to contact me at kayveengee@gmail.com

