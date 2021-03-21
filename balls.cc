#include <iostream>

#define ballz true

unsigned int balls_count;

void balls()
{
  balls_count++;
  printf("balls %d\n", balls_count);
}

int main()
{
  while(ballz)
  {
    balls();
  }
}
