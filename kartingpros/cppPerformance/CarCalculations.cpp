
#include <iostream>
#include "CarCalculations.h"
#include <vector>
#include <chrono>
#include <math.h>
using namespace std;
// int main()
// {
//     vector<int> nums;
//     for (int i = 0; i > -500; i--)
//         nums.push_back(i);
//     auto start_time = chrono::high_resolution_clock::now();
//     for (auto x : nums)
//         sin(x);
//     auto finish_time = chrono::high_resolution_clock::now();
//     auto duration = chrono::duration_cast<chrono::nanoseconds>(finish_time - start_time);
//     cout << duration.count() << endl;
// }
double CarCalculations::calcRad(int direction)
{
    return M_PI * direction / 180;
}
// g++ -c -fPIC CarCalculations.cpp -o CarCalculations.o
// g++ -shared -Wl,-soname,CarCalculations.so -o CarCalculations.so  CarCalculations.o