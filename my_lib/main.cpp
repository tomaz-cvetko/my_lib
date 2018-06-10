#include <iostream>
#include "vektor.h"
#include "matrika.h"

int main(int argc, char **argv) {
    
    my::DMatrix a(2, 3);
    my::DMatrix b(3, 1);
    std::cout << a << "\n" << b <<std::endl;
    a.randomize(-5, 5);
    b.randomize(-5, 5);
    std::cout << a << "\n" << b <<std::endl;
    
    my::DMatrix c = a*b;
    
    
    
    //std::cout << "Hello, world!" << std::endl;
    return 0;
}
