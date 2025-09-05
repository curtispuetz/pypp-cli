#include "py_list.h"
#include "py_str.h"
#include <glad/gl.h>

GLuint gl_gen_buffer();
PyList<GLuint> gl_gen_buffers(int n);
void gl_delete_buffer(GLuint buffer);
void gl_delete_buffers(PyList<GLuint> &buffers);
GLuint gl_gen_vertex_array();
PyList<GLuint> gl_gen_vertex_arrays(int n);
void gl_delete_vertex_array(GLuint array);
void gl_delete_vertex_arrays(PyList<GLuint> &arrays);
void gl_shader_source(GLuint shader, PyStr &source);
void gl_shader_sources(GLuint shader, PyList<PyStr> &sources);
GLint gl_get_shader_iv(GLuint shader, GLenum pname);
GLint gl_get_program_iv(GLuint program, GLenum pname);
PyStr gl_get_shader_info_log(GLuint shader);
PyStr gl_get_program_info_log(GLuint program);
