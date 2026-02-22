.

🔷 C++ MASTER NOTES — From Fundamentals to Systems Programming (Elite Edition)

Author: Systems Programming Guide
Purpose: Master C++ from basics to advanced systems programming, STL, memory, OOP, templates, and modern C++
Version: Complete Elite Edition with Memory Model, OOP, STL, Templates, and OS Interaction

📋 TABLE OF CONTENTS
PART 1: FOUNDATIONS

Introduction to C++

First C++ Program

Variables and Data Types

Operators

Input and Output

Control Flow

Loops

Functions

PART 2: CORE CONCEPTS

Arrays

Strings

Pointers

References

Dynamic Memory

Function Overloading

Inline Functions

PART 3: OBJECT ORIENTED PROGRAMMING

Classes and Objects

Constructors and Destructors

Encapsulation

Inheritance

Polymorphism

Abstraction

Operator Overloading

PART 4: MEMORY AND SYSTEMS

Stack vs Heap

new and delete

Smart Pointers

Memory Management Patterns

PART 5: STL

vector

list

stack

queue

map

set

algorithms

PART 6: ADVANCED C++

Templates

Exception Handling

Lambda Functions

Multithreading

File Handling

PART 1: FOUNDATIONS
1. Introduction to C++
What is C++?

C++ is an extension of C that adds:

Object Oriented Programming

Classes and Objects

Templates

STL (Standard Template Library)

Exception handling

Multithreading

Developed by Bjarne Stroustrup (1979).

Why C++ is important

Used in:

Operating systems

Game engines (Unreal Engine)

Trading systems

Databases

Embedded systems

2. First C++ Program
#include <iostream>

int main()
{
    std::cout << "Hello World" << std::endl;
    return 0;
}

Output:

Hello World
Explanation
#include <iostream>

Imports input-output library

std::cout

Standard output stream

std::endl

New line + flush buffer

Using namespace
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello World";
}
Compilation
g++ program.cpp -o program
./program
3. Variables and Data Types
#include <iostream>
using namespace std;

int main()
{
    int age = 20;
    float height = 5.9;
    char grade = 'A';
    double pi = 3.14159;
    bool isStudent = true;

    cout << age << endl;
}
Data type sizes
#include <iostream>
using namespace std;

int main()
{
    cout << sizeof(int) << endl;
    cout << sizeof(double) << endl;
}
PART 3: OOP
16. Classes and Objects
#include <iostream>
using namespace std;

class Student
{
public:
    int id;
    string name;

    void display()
    {
        cout << id << " " << name << endl;
    }
};

int main()
{
    Student s;

    s.id = 1;
    s.name = "Prerak";

    s.display();
}
Constructor
class Student
{
public:

    Student()
    {
        cout << "Constructor called" << endl;
    }
};
Destructor
~Student()
{
    cout << "Destructor called";
}
Inheritance
class Animal
{
public:
    void speak()
    {
        cout << "Animal sound";
    }
};

class Dog : public Animal
{
public:
    void bark()
    {
        cout << "Dog bark";
    }
};
Polymorphism
class Animal
{
public:
    virtual void speak()
    {
        cout << "Animal";
    }
};

class Dog : public Animal
{
public:
    void speak()
    {
        cout << "Dog";
    }
};
STL Vector
#include <vector>

vector<int> v;

v.push_back(10);
v.push_back(20);

cout << v[0];
Smart Pointer
#include <memory>

unique_ptr<int> ptr = make_unique<int>(10);
Multithreading
#include <thread>

void task()
{
    cout << "Thread running";
}

int main()
{
    thread t(task);
    t.join();
}
