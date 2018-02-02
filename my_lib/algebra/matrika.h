#ifndef MATRIKA_H
#define MATRIKA_H

#include <iostream>

namespace my
{
    class DMatrix
    {
    public:
        const int m;
        const int n;
        
        DMatrix(int rows, int cols); // Default prazna
        
        ~DMatrix(); // Destructor
        
        void randomize(double max=0, double min=0);
        
        void set(int i, int j, double value);
        
        double get(int i, int j) const;
        
        
    private:
        double** matrix;
        
        //friend std::ostream& operator<<(std::ostream& os, const my::DMatrix& obj);
    };
};

std::ostream& operator<<(std::ostream& os, const my::DMatrix& obj);


#endif
