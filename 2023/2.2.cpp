#include <bits/stdc++.h>

using namespace std;

vector<string> split(string s, string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    string token;
    vector<string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != string::npos) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back (token);
    }

    res.push_back (s.substr (pos_start));
    return res;
}

int main() {
    map<int, map<char, int>> m;

    ifstream infile("2.in");

    string line;
    while (getline(infile, line)) {
        stringstream ss(line);
        ss.ignore(strlen("Game "));
        int gameid;
        ss >> gameid;
        ss.ignore(strlen(": "));
        
        string rest;
        getline(ss, rest);
        for (auto game: split(rest, ";")) {
            for (auto entry: split(game, ",")) {
                stringstream ss2(entry);
                int count;
                char color;
                ss2 >> count;
                ss2.ignore(1);
                ss2 >> color;
                m[gameid][color] = max(m[gameid][color], count);
            }
        }
    }

    int sum = 0;

    for (auto[gameid, counts]: m) {
        int power = 1;
        for (auto[_, count]: counts) {
            power *= count;
        }
        sum += power;
    }

    cout << sum << endl;

    infile.close();
}