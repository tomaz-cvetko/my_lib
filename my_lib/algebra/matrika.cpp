#include "matrika.h"
#include <stdexcept>
#include <iostream>
#include <random>

my::DMatrix::DMatrix(int rows, int cols):m(rows), n(cols)
{
    matrix = new double*[rows];
    
    for(int i = 0; i < m; ++i){
        matrix[i] = new double[n]();
    }
}

my::DMatrix::~DMatrix()
{
    for(int i = 0; i < m; ++i){
        delete matrix[i];
    }
    
    delete matrix;
}




std::ostream& operator<<(std::ostream& os, const my::DMatrix& obj)
{
    for(int i = 0; i < obj.m; ++i){
        os << "| ";
        for(int j = 0; j < obj.n; ++j){
            os << obj.get(i, j) << " ";
        }
        os << "|\n";
    }
    return os;
}

void my::DMatrix::set(int i, int j, double value)
{
    if(i < m && j < n && i >= 0 && j >= 0){
        matrix[i][j] = value;
    }
    else{
        throw std::out_of_range("Index out of range!");
    }
}

double my::DMatrix::get(int i, int j) const
{
    if(i < m && j < n && i >= 0 && j >= 0){
        return matrix[i][j];
    }
    else{
        throw std::out_of_range("Index out of range!");
    }
}

void my::DMatrix::randomize(double max, double min)
{
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(min, max);
    
    for(int i = 0; i < m; ++i){
        for(int j = 0; j < n; ++j){
            matrix[i][j] = dis(gen);
        }
    }
}

my::DMatrix my::DMatrix::operator*(const my::DMatrix& rhs) const
{
    if(this->n != rhs.m){
        throw std::out_of_range("Matrices are of wrong dimensions!");
    }
    else{
        my::DMatrix result(this->m, rhs.n);
        
        for(int i = 0; i < this->m; ++i){
            for(int j = 0; j < rhs.n; ++j){
                double result_ij = 0.0;
                for(int k = 0; k < this->n; ++k){
                    result_ij += this->matrix[i][k]*rhs.matrix[k][j];
                }
                result.matrix[i][j] = result_ij;
            }
        }
        return result;
    }
}





