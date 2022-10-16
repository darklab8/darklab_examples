# Dependencies

requires installed `gcc` at least
and `pip install -r requirements.txt -c constraints.txt`
use `python3 make.py` to get available commands in those examples

# Result

`python3 make.py fizz` launches python only fizz (in file https://github.com/dd84ai/darklab_examples/blob/master/python_c_extensions/fizbuzz_pure.py), outputing string in bit form

```
b'1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,FizzBuzz,31,32,Fizz,34,Buzz,Fizz,37,38,Fizz,Buzz,41,Fizz,43,44,FizzBuzz,46,47,Fizz,49,Buzz,Fizz,52,53,Fizz,Buzz,56,Fizz,58,59,FizzBuzz,61,62,Fizz,64,Buzz,Fizz,67,68,Fizz,Buzz,71,Fizz,73,74,FizzBuzz,76,77,Fizz,79,Buzz,Fizz,82,83,Fizz,Buzz,86,Fizz,88,89,FizzBuzz,91,92,Fizz,94,Buzz,Fizz,97,98,Fizz,Buzz'
```

for fizz out of million numbers it yields time

```
len(fizz_result())=6274072
main finished at 0.21506524085998535
```

===================================
`python3 make.py fizz_extension`  invokes my python code, that invokes function written in C and inserted into python xD
files:
https://github.com/dd84ai/darklab_examples/blob/master/python_c_extensions/fizz_extension_build.py
https://github.com/dd84ai/darklab_examples/blob/master/python_c_extensions/fizz_run.py
https://github.com/dd84ai/darklab_examples/blob/master/python_c_extensions/fizz.c
https://github.com/dd84ai/darklab_examples/blob/master/python_c_extensions/fizz.h

for 100 numbers, result is b`string pretty much the same

```
b'1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17,Fizz,19,Buzz,Fizz,22,23,Fizz,Buzz,26,Fizz,28,29,FizzBuzz,31,32,Fizz,34,Buzz,Fizz,37,38,Fizz,Buzz,41,Fizz,43,44,FizzBuzz,46,47,Fizz,49,Buzz,Fizz,52,53,Fizz,Buzz,56,Fizz,58,59,FizzBuzz,61,62,Fizz,64,Buzz,Fizz,67,68,Fizz,Buzz,71,Fizz,73,74,FizzBuzz,76,77,Fizz,79,Buzz,Fizz,82,83,Fizz,Buzz,86,Fizz,88,89,FizzBuzz,91,92,Fizz,94,Buzz,Fizz,97,98,Fizz,Buzz'
```

for million numbers we have same ammount of yielded chracters but 5.546019625202892 times faster!!!!

```
len(ffi.string(result))=6274072
main finished at 0.03877830505371094
```
