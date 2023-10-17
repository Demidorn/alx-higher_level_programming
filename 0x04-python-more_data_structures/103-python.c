#include <Python.h>

/*
 * File: 103-python.c
 * Auth: Demidorn
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *data;
	
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
	printf("  first %ld bytes: ", size < 10 ? size : 10);

	data = ((PyBytesObject *)p)->ob_sval;
	
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", data[i]);
		if (i < size - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
}


/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @argc: ...
 * @argv: ....
 * Return: Always successfull
 */
int main(int argc, char *argv[])
{
	Py_Initialize();
	PyObject *pyBytes = PyBytes_FromStringAndSize("Python Bytes", 11);
	print_python_bytes(pyBytes);
	Py_Finalize();
	
	return (0);
}
