#ifndef PyObjC_FORMAL_PROTOCOL_H
#define PyObjC_FORMAL_PROTOCOL_H

NS_ASSUME_NONNULL_BEGIN

extern PyTypeObject PyObjCFormalProtocol_Type;
#define PyObjCFormalProtocol_Check(obj)                                                  \
    PyObject_TypeCheck(obj, &PyObjCFormalProtocol_Type)

extern int PyObjCFormalProtocol_CheckClass(PyObject*, char*, PyObject*, PyObject*,
                                           PyObject*);
extern const char* _Nullable PyObjCFormalProtocol_FindSelectorSignature(PyObject*, SEL,
                                                                        int);
extern PyObject* _Nullable PyObjCFormalProtocol_ForProtocol(Protocol*);
extern Protocol* _Nullable PyObjCFormalProtocol_GetProtocol(PyObject*);

NS_ASSUME_NONNULL_END

#endif /* PyObjC_FORMAL_PROTOCOL_H */
