#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <python.h>

int main(int argc, char *argv[]);
void print_python_string(PyObject *p);

/**
 * print_python_string - Prints a Python string.
 * @p: The PyObject representing the Python string to print.
 *
 * Return: 0 when successful
 */

void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
		/*Convert the PyObject to a Python Unicode string*/
		PyObject *unicode_string = PyUnicode_AsUnicodeEscapeString(p);

		if (unicode_string != NULL)
		{
			printf("'%s'\n", PyBytes_AS_STRING(unicode_string));
			Py_XDECREF(unicode_string);
		}
		else
		{
			PyErr_Print();
		}
	}
	else
	{
		printf("Object is not a valid string.\n");
	}
}


/**
 * main - entry of the function
 * @argv: array of arguments
 * @argc: characters
 *
 * Return: 0 always successful
 */

int main(int argc, char *argv[])
{
	/*Initialize the Python interpreter*/
	Py_Initialize();
	/* Creates a Python string*/
	PyObject *python_string = PyUnicode_DecodeUTF8("Hello,
			Python!", 13, "strict");
	print_python_string(python_string);
	Py_Finalize();
	return (0);
}
