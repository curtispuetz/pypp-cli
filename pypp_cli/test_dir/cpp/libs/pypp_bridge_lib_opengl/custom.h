#include "py_list.h"
#include "py_str.h"
#include <glad/gl.h>

GLuint gl_gen_buffer();
pypp::PyList<GLuint> gl_gen_buffers(int n);
void gl_delete_buffer(GLuint buffer);
void gl_delete_buffers(pypp::PyList<GLuint> &buffers);
GLuint gl_gen_vertex_array();
pypp::PyList<GLuint> gl_gen_vertex_arrays(int n);
void gl_delete_vertex_array(GLuint array);
void gl_delete_vertex_arrays(pypp::PyList<GLuint> &arrays);
void gl_shader_source(GLuint shader, pypp::PyStr &source);
void gl_shader_sources(GLuint shader, pypp::PyList<pypp::PyStr> &sources);
GLint gl_get_shader_iv(GLuint shader, GLenum pname);
GLint gl_get_program_iv(GLuint program, GLenum pname);
pypp::PyStr gl_get_shader_info_log(GLuint shader);
pypp::PyStr gl_get_program_info_log(GLuint program);
