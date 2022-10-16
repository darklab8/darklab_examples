# include <stdlib.h>
# include <math.h>

const int cursor_max = 10000000;

const char FizzBuzz[] = "FizzBuzz";
const int FizzBuzz_count = 8;
const char Fizz[] = "Fizz";
const char Buzz[] = "Buzz";
const int Fizz_count = 4;
const int Buzz_count = 4;

char *fizz(int n){

  char *result = malloc(cursor_max);
  int cursor = 0;
  
  char number_as_str[10];
  int number_length;
  
  for(int number=1; number<=n; number++) 
  {
      if(((number%3)||(number%5))== 0)
      {
        for (int k = 0; k < FizzBuzz_count; k++) {
          result[cursor] = FizzBuzz[k];
          cursor++;
        }
        
      }
      else if((number%3)==0)
      {
        for (int k = 0; k < Fizz_count; k++) {
          result[cursor] = Fizz[k];
          cursor++;
        }
      }
      else if((number%5)==0)
      {
        for (int k = 0; k < Buzz_count; k++) {
          result[cursor] = Buzz[k];
          cursor++;
        }
      }
      else
      {
        sprintf(number_as_str, "%d", number);
        number_length = strlen(number_as_str);
        for (int k = 0; k < number_length; k++) {
          result[cursor] = number_as_str[k];
          cursor++;
        }
      }

      result[cursor] = ','; cursor++;
  }

  result[cursor-1] = '\0';
  return result;
}