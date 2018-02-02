#include <iostream>
#include "vektor.h"
#include "matrika.h"

int main(int argc, char **argv) {
    
    my::Vektor<float> a(3.12, 4.15, 2.6);
    
    my::Vektor<float> b = my::Vektor<float>::fromCylindric(2.00, 3.14, 1.12);
    
    std::cout << a*b;
    std::cout << a;
    
    my::DMatrix c(10, 5);
    std::cout << std::endl << c;
    c.randomize(-2.9, 12.5);
    std::cout << c;
    
    std::cout << "Hello, world!" << std::endl;
    return 0;
}
