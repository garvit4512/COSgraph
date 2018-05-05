#include "hello.h"


char const* greet(char* s)
{
	praneet a;
	a.t = 50;
	greete(a);
}

#include <boost/python.hpp>

BOOST_PYTHON_MODULE(hello)
{
    using namespace boost::python;
    def("greet", greet);
}