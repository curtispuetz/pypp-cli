#include "custom.h"

GLuint gl_gen_buffer()
{
    GLuint buffer;
    glGenBuffers(1, &buffer);
    return buffer;
}

pypp::PyList<GLuint> gl_gen_buffers(int n)
{
    pypp::PyList<GLuint> buffers(n);
    glGenBuffers(n, buffers.data_ref().data());
    return buffers;
}

void gl_delete_buffer(GLuint buffer) { glDeleteBuffers(1, &buffer); }

void gl_delete_buffers(pypp::PyList<GLuint> &buffers)
{
    glDeleteBuffers(buffers.len(), buffers.data_ref().data());
}

GLuint gl_gen_vertex_array()
{
    GLuint array;
    glGenVertexArrays(1, &array);
    return array;
}

pypp::PyList<GLuint> gl_gen_vertex_arrays(int n)
{
    pypp::PyList<GLuint> arrays(n);
    glGenVertexArrays(n, arrays.data_ref().data());
    return arrays;
}

void gl_delete_vertex_array(GLuint array) { glDeleteVertexArrays(1, &array); }

void gl_delete_vertex_arrays(pypp::PyList<GLuint> &arrays)
{
    glDeleteVertexArrays(arrays.len(), arrays.data_ref().data());
}

void gl_shader_source(GLuint shader, pypp::PyStr &source)
{
    const char *src = source.str().c_str();
    glShaderSource(shader, 1, &src, nullptr);
}

void gl_shader_sources(GLuint shader, pypp::PyList<pypp::PyStr> &sources)
{
    std::vector<const char *> c_strs;
    c_strs.reserve(sources.len());
    for (int i = 0; i < sources.len(); ++i)
    {
        c_strs.push_back(sources[i].str().c_str());
    }
    glShaderSource(shader, static_cast<GLsizei>(c_strs.size()), c_strs.data(),
                   nullptr);
}

GLint gl_get_shader_iv(GLuint shader, GLenum pname)
{
    int param;
    glGetShaderiv(shader, pname, &param);
    return param;
}

GLint gl_get_program_iv(GLuint program, GLenum pname)
{
    int param;
    glGetProgramiv(program, pname, &param);
    return param;
}

pypp::PyStr gl_get_shader_info_log(GLuint shader)
{
    char infoLog[512];
    glGetShaderInfoLog(shader, 512, nullptr, infoLog);
    return pypp::PyStr(infoLog);
}

pypp::PyStr gl_get_program_info_log(GLuint program)
{
    char infoLog[512];
    glGetProgramInfoLog(program, 512, nullptr, infoLog);
    return pypp::PyStr(infoLog);
}
