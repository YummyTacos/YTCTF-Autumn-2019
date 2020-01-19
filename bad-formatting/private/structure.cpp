#include <iostream>
#include <string>

void print();

void read_flag();

void func1();

void func2();

bool check();

int main() {
    std::string flag;
    print(FLAG);
    print("Input flag\n>>> ");

    read_flag(flag);

    for (int i = 0; i < flag.length(); i++) {
        flag = func1(flag[i], flag[(i + 1) % s.length()]);
    }

    if (check()) {
        print("Good");
    } else {
        print("Bad");
    }

    return 0;
}
