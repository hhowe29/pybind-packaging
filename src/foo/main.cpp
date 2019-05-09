#include <pybind11/pybind11.h>
#include <iostream>

using namespace std;
namespace py = pybind11;

int add(int x, int y)
{
    cout << __PRETTY_FUNCTION__ << endl;
    return x + y;

}

PYBIND11_MODULE(baz, m)
{
    m.def("add", &add, "Add two numbers");
}
