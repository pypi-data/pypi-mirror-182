/*
 * A custom wrapper for the (opaque) FSRef structure.
 */
#include "pyobjc.h"
#import <CoreServices/CoreServices.h>

NS_ASSUME_NONNULL_BEGIN

#pragma GCC diagnostic   ignored "-Wdeprecated-declarations"
#pragma clang diagnostic ignored "-Wdeprecated-declarations"

/*
 * Interface of the FSRef type:
 *
 * FSRef.from_pathname(value)
 *   # -> returns new FSRef instance for posix path 'value'
 *
 * aref.as_pathname()
 *  # -> returns a Unicode string with the posix path
 *
 * aref.as_carbon()
 *  # -> return a Carbon.File.FSRef instance (only
 *  #    available when Carbon support is enabled in Python)
 *
 * aref.data
 *  # -> read-only property with the bytes in the FSRef
 */

typedef struct {
    PyObject_HEAD

    FSRef ref;
} PyObjC_FSRefObject;

static PyObject* _Nullable fsref_as_bytes(PyObject* ref, void* _Nullable closure
                                          __attribute__((__unused__)))
{
    return PyBytes_FromStringAndSize((char*)&((PyObjC_FSRefObject*)ref)->ref,
                                     sizeof(FSRef));
}

static PyObject* _Nullable fsref_sizeof(PyObject* ref)
{
    return PyLong_FromSsize_t(Py_TYPE(ref)->tp_basicsize);
}

static PyObject* _Nullable fsref_as_path(PyObject* ref)
{
    OSStatus rc;
    UInt8    buffer[1024];

    rc = FSRefMakePath(&((PyObjC_FSRefObject*)ref)->ref, buffer, sizeof(buffer));
    if (rc != 0) {
        PyErr_Format(PyExc_OSError, "MAC Error %d", rc);

        return NULL;
    }

    return PyUnicode_DecodeFSDefault((char*)buffer);
}

static PyObject* _Nullable fsref_from_path(PyObject* self __attribute__((__unused__)),
                                           PyObject* path)
{
    PyObject* value;
    FSRef     result;
    Boolean   isDirectory;
    OSStatus  rc;

    if (!PyUnicode_Check(path)) {
        PyErr_SetString(PyExc_TypeError, "Expecting string");
        return NULL;
    }

    value = PyUnicode_EncodeFSDefault(path);
    if (value == NULL)
        return NULL;
    PyObjC_Assert(PyBytes_Check(value), NULL);

    rc = FSPathMakeRef((UInt8*)PyBytes_AsString(value), &result, &isDirectory);
    Py_DECREF(value);
    if (rc != 0) {
        PyErr_Format(PyExc_OSError, "MAC Error %d", rc);
        return NULL;
    }

    return PyObjC_decode_fsref(&result);
}

static PyGetSetDef fsref_getset[] = {{
                                         .name = "data",
                                         .get  = fsref_as_bytes,
                                         .doc  = "bytes in the FSRef",
                                     },
                                     {
                                         .name = NULL /* SENTINEL */
                                     }};

static PyMethodDef fsref_methods[] = {
    {.ml_name  = "as_pathname",
     .ml_meth  = (PyCFunction)fsref_as_path,
     .ml_flags = METH_NOARGS,
     .ml_doc   = "as_pathname()\n" CLINIC_SEP "\nReturn POSIX path for this object"},
    {.ml_name  = "from_pathname",
     .ml_meth  = (PyCFunction)fsref_from_path,
     .ml_flags = METH_O | METH_CLASS,
     .ml_doc =
         "from_pathname(path)\n" CLINIC_SEP "\nCreate FSRef instance for an POSIX path"},

    {
        .ml_name  = "__sizeof__",
        .ml_meth  = (PyCFunction)fsref_sizeof,
        .ml_flags = METH_NOARGS,
    },
    {
        .ml_name = NULL /* SENTINEL */
    }};

PyTypeObject PyObjC_FSRefType = {
    PyVarObject_HEAD_INIT(&PyType_Type, 0).tp_name = "objc.FSRef",
    .tp_basicsize                                  = sizeof(PyObjC_FSRefObject),
    .tp_itemsize                                   = 0,
    .tp_getattro                                   = PyObject_GenericGetAttr,
    .tp_setattro                                   = PyObject_GenericSetAttr,
    .tp_flags                                      = Py_TPFLAGS_DEFAULT,
    .tp_methods                                    = fsref_methods,
    .tp_getset                                     = fsref_getset,
};

int
PyObjC_encode_fsref(PyObject* value, void* buffer)
{
    if (PyObjC_FSRefCheck(value)) {
        *(FSRef*)buffer = ((PyObjC_FSRefObject*)value)->ref;
        return 0;
    }

    PyErr_SetString(PyExc_ValueError, "Cannot convert value to FSRef");
    return -1;
}

PyObject* _Nullable PyObjC_decode_fsref(const void* buffer)
{
    PyObjC_FSRefObject* result = PyObject_New(PyObjC_FSRefObject, &PyObjC_FSRefType);

    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    result->ref = *(const FSRef*)buffer;
    return (PyObject*)result;
}

NS_ASSUME_NONNULL_END
