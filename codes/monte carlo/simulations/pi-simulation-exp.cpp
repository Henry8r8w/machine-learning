#include <iostream>
#include <fstream>
#include <vector>
#include <random>
using namespace std;

struct indict_func {
    double x;
    double y;
    bool inside_circle;

    indict_func(double x_val, double y_val, double radius)
        :x(x_val), y(y_val), inside_circle(x_val * x_val + y_val * y_val <= radius * radius) {}
};


std::pair<double, double> generate_point(double field_length = 1.0) {
    static random_device rd;
    static mt19937 gen(rd());
    std::uniform_real_distribution<> dis(-field_length / 2.0, field_length / 2.0); // drawing +-1/2 fields centered at 0
    return {dis(gen), dis(gen)};
}


int main() {
    // To be Updated
    vector<indict_func> drops; 
    int f_xy = 0;
    double pi_estimate = 0.0;

    // To be Written
    ofstream pi_points("../outputs/raw/pi_points.csv");
    pi_points << "x,y,label\n";


    ofstream pi_estimates("../outputs/raw/pi_estimates.csv"); 
    pi_estimates << "sample,pi_estimate\n"; 

    // To Input
    double radius = 0.5;
    int S = 10000;
    for (int s = 1; s < S; ++s) {
        auto [x, y] = generate_point(1.0); 

        indict_func drop(x, y, radius);

        drops.push_back(drop); 
        if (drop.inside_circle) f_xy++;

        pi_estimate = 4.0 * f_xy / s;

        pi_estimates << (s + 1) << "," << pi_estimate << "\n";
        pi_points << x << "," << y << "," << drop.inside_circle << "\n";
        cout << "pi-estimate: " << pi_estimate << "\n";
        
    }

    std::cout << "pi-estimate: " << pi_estimate << "\n";
    return 0;
}
