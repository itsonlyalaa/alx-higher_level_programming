#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
    int x = 0, lst_len = 0;
    PyObject *item;
    PyListObject *clone = (PyListObject *) p;

    lst_len = Py_SIZE(p);
    printf("[*] Size of the Python List = %d\n", lst_len);
    printf("[*] Allocated = %d\n", (int) clone->allocated);

    for (; x < lst_len; ++x)
    {
        item = PyList_GET_ITEM(p, x);
        printf("Element %d: %s\n", x, item->ob_type->tp_name);
    }
    return;
}
