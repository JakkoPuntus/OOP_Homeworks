#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  int S = 0;

  int start = (long int) (1 + sqrt(1 + 8 * S)) / 2;

  cout << start << "\n";
      for (long int N = start; N > 0; N--)
  {
    double A = (double) ((double) S / N) - ((double) (N - 1) / 2);
    if ( abs(A - int(A)) < 1e-16 && A > 0)
    {
      cout << int(A) << " " << N;
      break;
    }
  }
}

//111111113