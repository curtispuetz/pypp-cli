#pragma once
#include <chrono>
#include <thread>

namespace pypp_time {
// Returns the current wall time point (system_clock::time_point)
inline std::chrono::system_clock::time_point start() {
    return std::chrono::system_clock::now();
}

// Returns the elapsed wall time in seconds since start_time
inline double end(std::chrono::system_clock::time_point start_time) {
    return std::chrono::duration_cast<std::chrono::duration<double>>(
               std::chrono::system_clock::now() - start_time)
        .count();
}

// Sleeps for the given number of seconds (can be fractional)
inline void sleep(double seconds) {
    if (seconds > 0.0) {
        std::this_thread::sleep_for(std::chrono::duration<double>(seconds));
    }
}

// Returns the current high-resolution performance counter time point
// (high_resolution_clock::time_point)
inline std::chrono::high_resolution_clock::time_point perf_counter_start() {
    return std::chrono::high_resolution_clock::now();
}

// Returns the elapsed high-resolution time in seconds since start_time
inline double
perf_counter_end(std::chrono::high_resolution_clock::time_point start_time) {
    return std::chrono::duration_cast<std::chrono::duration<double>>(
               std::chrono::high_resolution_clock::now() - start_time)
        .count();
}

} // namespace pypp_time
