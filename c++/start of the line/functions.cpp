#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int main() {
    int result = add(5, 3);
    cout << "Result: " << result << endl; // Added the missing `>` symbol
    return 0;
}
