// Multithreaded balls
#ifndef _MULTI_BALLS
#define _MULTI_BALLS
#include <iostream>
#include <thread>

bool noBalls = false;

void balls() {
  while ( !noBalls ) {
    std::cout << "balls\n";
  }
}

int main() {
  std::thread ball(balls);
  std::cin.get();
  noBalls = true; // :sadge:
  ball.join();
  std::cout << "tfw no balls :sadge:\n";
}
#endif // _MULTI_BALLS
