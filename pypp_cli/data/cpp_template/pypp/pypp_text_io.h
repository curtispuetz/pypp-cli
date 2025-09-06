#pragma once

#include "py_list.h"
#include "py_str.h"
#include <fstream>

namespace pypp {
class PyTextIO {
  private:
    std::fstream file_stream;
    PyStr filename_;
    PyStr mode_;

    void check_file_open() const;
    void check_file_open_for_writing() const;
    void open_file(const PyStr &filename, const PyStr &mode);

  public:
    PyTextIO(const PyStr &filename, const PyStr &mode = PyStr("r"));
    ~PyTextIO();

    PyStr read();
    PyStr readline();
    PyList<PyStr> readlines();
    void write(const PyStr &content);
    void writelines(const PyList<PyStr> &lines);

    bool good() const;
    bool eof() const;
    bool fail() const;
};

// --- Example Usage ---

// int main() {
//     // Create a dummy file for testing
//     try {
//         PyTextIO out_file("test_input.txt", "w");
//         out_file.write("Line 1\n");
//         out_file.write("Line 2 is here.\n");
//         out_file.write("Last line without a newline");
//         std::cout << "Created test_input.txt" << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error creating test_input.txt: " << e.what() <<
//         std::endl; return 1;
//     }

//     std::cout << "\n--- Testing Read Operations ---" << std::endl;

//     // Example 1: Read entire file (Python: with open("file", "r") as f: data
//     =
//     // f.read())
//     try {
//         PyTextIO file_obj("test_input.txt", "r");
//         std::string data = file_obj.read();
//         std::cout << "Content of test_input.txt (read):\n---\n"
//                   << data << "\n---" << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error reading file: " << e.what() << std::endl;
//     }

//     // Example 2: Read line by line (Python: with open("file", "r") as f: for
//     // line in f:)
//     try {
//         PyTextIO file_obj("test_input.txt", "r");
//         std::cout << "\nReading line by line:\n---" << std::endl;
//         std::string line;
//         while ((line = file_obj.readline()) != "" || !file_obj.eof()) {
//             std::cout << line << std::endl;
//             if (file_obj.eof())
//                 break; // Break if EOF and previous line was empty (e.g.,
//                 last
//                        // empty line)
//         }
//         std::cout << "---" << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error reading file line by line: " << e.what()
//                   << std::endl;
//     }

//     // Example 3: Read all lines into a vector (Python: with open("file",
//     "r")
//     // as f: lines = f.readlines())
//     try {
//         PyTextIO file_obj("test_input.txt", "r");
//         std::vector<std::string> lines = file_obj.readlines();
//         std::cout << "\nReading all lines into a vector:\n---" << std::endl;
//         for (const std::string &l : lines) {
//             std::cout << l << " [EOL]"
//                       << std::endl; // Indicate end of line for clarity
//         }
//         std::cout << "---" << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error reading all lines: " << e.what() << std::endl;
//     }

//     std::cout << "\n--- Testing Write Operations ---" << std::endl;

//     // Example 4: Write to file (Python: with open("file", "w") as f:
//     // f.write("new content")) This will overwrite test_output.txt
//     try {
//         PyTextIO out_file("test_output.txt", "w");
//         out_file.write("This is the first line.\n");
//         out_file.write("This line overwrites previous content.\n");
//         std::cout << "Wrote to test_output.txt (overwritten previous)"
//                   << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error writing to test_output.txt: " << e.what()
//                   << std::endl;
//     }

//     // Verify content of test_output.txt
//     try {
//         PyTextIO check_file("test_output.txt", "r");
//         std::string content = check_file.read();
//         std::cout << "Content of test_output.txt after overwrite:\n---\n"
//                   << content << "\n---" << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error verifying test_output.txt: " << e.what()
//                   << std::endl;
//     }

//     // Example 5: Append to file (Python: with open("file", "a") as f:
//     // f.write("more content"))
//     try {
//         PyTextIO append_file("test_output.txt", "a");
//         append_file.write("This line is appended.\n");
//         append_file.write("Another appended line.");
//         std::cout << "Appended to test_output.txt" << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error appending to test_output.txt: " << e.what()
//                   << std::endl;
//     }

//     // Verify content of test_output.txt after append
//     try {
//         PyTextIO check_file("test_output.txt", "r");
//         std::string content = check_file.read();
//         std::cout << "Content of test_output.txt after append:\n---\n"
//                   << content << "\n---" << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error verifying test_output.txt after append: "
//                   << e.what() << std::endl;
//     }

//     // Example 6: Write multiple lines (Python: with open("file", "w") as f:
//     // f.writelines(list_of_lines))
//     try {
//         PyTextIO write_lines_file("test_writelines.txt", "w");
//         std::vector<std::string> lines_to_write = {
//             "First line for writelines", "Second line for writelines",
//             "Third and final line for writelines"};
//         write_lines_file.writelines(lines_to_write);
//         std::cout << "Wrote lines to test_writelines.txt" << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error writing lines to test_writelines.txt: " <<
//         e.what()
//                   << std::endl;
//     }

//     // Verify content of test_writelines.txt
//     try {
//         PyTextIO check_file("test_writelines.txt", "r");
//         std::string content = check_file.read();
//         std::cout << "Content of test_writelines.txt:\n---\n"
//                   << content << "\n---" << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Error verifying test_writelines.txt: " << e.what()
//                   << std::endl;
//     }

//     // Example 7: Handling file not found
//     std::cout << "\n--- Testing Error Handling ---" << std::endl;
//     try {
//         PyTextIO non_existent_file("non_existent.txt", "r");
//         std::string data = non_existent_file.read();
//         std::cout << "Should not reach here." << std::endl;
//     } catch (const std::runtime_error &e) {
//         std::cerr << "Caught expected error: " << e.what() << std::endl;
//     }

//     return 0;
// }
} // namespace pypp