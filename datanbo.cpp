#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {
    std::ifstream file("sample_traffic_data.csv");
    if (!file.is_open()) {
        std::cerr << "Error: Unable to open the CSV file." << std::endl;
        return 1;
    }

    std::string line;
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }

    file.close();
    return 0;
}
