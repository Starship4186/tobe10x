#include <iostream>
#include <stdexcept>

// Vector implementation on CPP
// Dynamic List
template <typename T>
class MyVector
{
private:
    T* elements; // Points to the array
    size_t size;  // Stores current size of the array
    size_t capacity; // Stores the total capacity of the array

    // Resize the array if the older array is full
    bool resize(bool new_capacity)
    {
        // new_capacity==True => Double, if false => Half
        size_t newCapacity = (new_capacity) ? capacity * 2 : capacity / 2;
        // create new pointer
        T* tmp = new T[newCapacity];

        // move all the data to new one
        if (new_capacity == true)
        {
            for ( size_t i = 0; i < capacity; i++)
            {
                tmp[i] = elements[i];

            }
        // free old pointer
            delete[] elements;
        // update the value of the pointer
            elements = tmp;
            capacity = new_capacity;
            return true;

        }
        // TODO Resize to half if the current array is used 1/4th 
        return false;
    }
public:
    // Constructors
    MyVector(){
        elements = nullptr;
        size = 0;
        capacity = 0;
    }
    MyVector(size_t initialSize){
        capacity = initialSize;
        size = 0;
        elements  = new T[capacity];
    }
    // Destructors to free things that are dynamically allocated
    // by using new
    ~MyVector(){
        if (elements != nullptr){
            delete[] elements; 
        }
    }

    size_t ret_capacity(){
        return capacity;
    }

    size_t ret_size(){
        return size;
    }

    bool is_empty(){
        return size == 0 ? true : false;
    }

    void is_insertable(){
        // if the array is full
        // Resize
        if ( capacity == size )
        {
            resize(true);
        }

    }

    // Pushes new item to the array 
    bool push(T item){
        // checks if item can be inserted
        is_insertable();
        elements[size] = item;
        size += 1;
        return true;
        
    }

    // Lists elements on the array
    void list()
    {
        for ( size_t i = 0; i < size; i++){
            std::cout << elements[i] << " "  ; 
        }
    }

    T at(size_t index)
    {
        if ( index < capacity)
        {
            return elements[index];
        }
        else
        {
            throw std::out_of_range("Index out of bounds");
        }
    }


};


int main() {
using namespace std;

    // std::cout << "Hello, World!" << std::endl;
    MyVector<int> intVector(3);

    // Testing for resize    
    intVector.push(10);
    intVector.push(20);
    intVector.push(30);
    intVector.push(40);
    // std::cout << intVector << std::endl;
    
    // cout << intVector.ret_size() << endl;
    intVector.list();
    return 0;
}
