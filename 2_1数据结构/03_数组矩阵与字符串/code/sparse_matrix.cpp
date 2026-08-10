#include <algorithm>
#include <iostream>
#include <stdexcept>
#include <vector>

struct Entry { int row, col, value; };

class SparseMatrix {
public:
    SparseMatrix(int rows, int cols, std::vector<Entry> entries)
        : rows_(rows), cols_(cols), entries_(std::move(entries)) {
        if (rows < 0 || cols < 0) throw std::invalid_argument("negative size");
        std::sort(entries_.begin(), entries_.end(), [](const Entry& a, const Entry& b) {
            return a.row != b.row ? a.row < b.row : a.col < b.col;
        });
    }

    SparseMatrix transpose() const {
        std::vector<int> count(cols_, 0);
        for (const auto& e : entries_) ++count.at(e.col);
        std::vector<int> next(cols_, 0);
        for (int c = 1; c < cols_; ++c) next[c] = next[c - 1] + count[c - 1];
        std::vector<Entry> result(entries_.size());
        for (const auto& e : entries_) result[next[e.col]++] = {e.col, e.row, e.value};
        return SparseMatrix(cols_, rows_, std::move(result));
    }

    void print() const {
        for (const auto& e : entries_) std::cout << e.row << ' ' << e.col << ' ' << e.value << '\n';
    }

private:
    int rows_, cols_;
    std::vector<Entry> entries_;
};

int main() {
    SparseMatrix matrix(3, 4, {{0, 1, 7}, {1, 3, 5}, {2, 0, 9}});
    matrix.transpose().print();
}
