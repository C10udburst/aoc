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
    map<char, int> expected = {
        {
            'r', 12
        },
        {
            'g', 13
        },
        {
            'b', 14
        }
    };

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
        for (auto [color, count]: counts) {
            if (count > expected[color]) {
                goto too_big;
            }
        }
        
        sum += gameid;
        too_big:
        continue;
    }

    cout << sum << endl;

    infile.close();
}