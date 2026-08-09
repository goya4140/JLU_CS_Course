#include <iostream>
#include <stdexcept>
#include <vector>

class MinHeap {
    std::vector<int> data_;
    void siftUp(std::size_t i) {
        while (i > 0) {
            std::size_t parent = (i - 1) / 2;
            if (data_[parent] <= data_[i]) break;
            std::swap(data_[parent], data_[i]);
            i = parent;
        }
    }
    void siftDown(std::size_t i) {
        while (2 * i + 1 < data_.size()) {
            std::size_t child = 2 * i + 1;
            if (child + 1 < data_.size() && data_[child + 1] < data_[child]) ++child;
            if (data_[i] <= data_[child]) break;
            std::swap(data_[i], data_[child]);
            i = child;
        }
    }
public:
    void push(int value) { data_.push_back(value); siftUp(data_.size() - 1); }
    int pop() {
        if (data_.empty()) throw std::underflow_error("empty heap");
        int result = data_.front();
        data_.front() = data_.back();
        data_.pop_back();
        if (!data_.empty()) siftDown(0);
        return result;
    }
};

int main() {
    MinHeap heap;
    for (int value : {7, 2, 9, 1, 5}) heap.push(value);
    for (int i = 0; i < 5; ++i) std::cout << heap.pop() << ' ';
    std::cout << '\n';
}
