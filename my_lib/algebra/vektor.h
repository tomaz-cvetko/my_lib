#ifndef VEKTOR_H
#define VEKTOR_H

#include <cmath>
#include <iostream>

namespace my
{
    template<typename T>
    class Vektor;
    
    template<typename T>
    std::ostream& operator<<(std::ostream& os, const Vektor<T>& obj);
    
    
    template<typename T>
    class Vektor
    {
    public:
        Vektor() = default;
        Vektor(T a, T b, T c):x(a), y(b), z(c){};
        
        static Vektor<T> fromCylindric(T r, T phi, T h)
        {
            return Vektor(r * std::cos(phi), r * std::sin(phi), h);
        }
        
        static Vektor<T> fromSpheric(T r, T phi, T theta)
        {
            return Vektor(r * std::cos(phi)*std::sin(theta), r * std::sin(phi) * std::sin(theta), r * std::cos(theta));
        }
        
        T operator*(const Vektor<T>& rhs) const
        {
            return (x*rhs.x + y*rhs.y + z*rhs.z);
        }
        
        Vektor<T> operator+(const Vektor<T>& rhs)
        {
            return Vektor(x+rhs.x, y+rhs.y, z+rhs.z);
        }
        
        Vektor<T> operator-(const Vektor<T>& rhs){
            return Vektor(x-rhs.x, y-rhs.y, z-rhs.z);
        }
        
        
    private:
        T x = 0;
        T y = 0;
        T z = 0;
        
        friend std::ostream& operator<< <>(std::ostream& os, const Vektor<T>& obj);
        
    };
    
    
    template<typename T>
    std::ostream& operator<<(std::ostream& os, const Vektor<T>& obj)
    {
        
        os << "(" << obj.x << ", " << obj.y << ", " << obj.z << ")";
        
        
        return os;
    }

};
#endif
