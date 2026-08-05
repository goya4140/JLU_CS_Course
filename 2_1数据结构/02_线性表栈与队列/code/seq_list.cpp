// ============================================================
// 线性表 - 顺序表实现
// 支持动态扩容的顺序表模板类
// ============================================================

#include <iostream>
#include <stdexcept>

template <typename T>
class SeqList {
private:
    T* data;          // 存储空间基址
    int capacity;     // 当前分配的容量
    int length;       // 当前长度

    // 扩容为原来的 2 倍
    void expand() {
        int newCap = capacity == 0 ? 1 : capacity * 2;
        T* newData = new T[newCap];
        for (int i = 0; i < length; i++) {
            newData[i] = data[i];
        }
        delete[] data;
        data = newData;
        capacity = newCap;
        std::cout << "[Info] 扩容至容量: " << capacity << std::endl;
    }

public:
    // 构造函数
    explicit SeqList(int initCapacity = 8) : capacity(initCapacity), length(0) {
        data = new T[capacity];
    }

    // 析构函数
    ~SeqList() {
        delete[] data;
    }

    // 获取长度
    int size() const { return length; }

    // 判空
    bool empty() const { return length == 0; }

    // 按位访问（1-based）
    T& operator[](int i) {
        if (i < 1 || i > length) {
            throw std::out_of_range("索引越界");
        }
        return data[i - 1];
    }

    const T& operator[](int i) const {
        if (i < 1 || i > length) {
            throw std::out_of_range("索引越界");
        }
        return data[i - 1];
    }

    // 在位置 i（1-based）插入元素 e
    bool insert(int i, const T& e) {
        if (i < 1 || i > length + 1) {
            return false;
        }
        if (length >= capacity) {
            expand();
        }
        // 元素后移
        for (int j = length - 1; j >= i - 1; j--) {
            data[j + 1] = data[j];
        }
        data[i - 1] = e;
        length++;
        return true;
    }

    // 在末尾添加元素
    void pushBack(const T& e) {
        insert(length + 1, e);
    }

    // 删除位置 i（1-based）的元素
    bool remove(int i, T& e) {
        if (i < 1 || i > length) {
            return false;
        }
        e = data[i - 1];
        for (int j = i; j < length; j++) {
            data[j - 1] = data[j];
        }
        length--;
        return true;
    }

    // 按值查找，返回位置（1-based），找不到返回 0
    int locate(const T& e) const {
        for (int i = 0; i < length; i++) {
            if (data[i] == e) {
                return i + 1;
            }
        }
        return 0;
    }

    // 遍历输出
    void print() const {
        std::cout << "SeqList(" << length << "/" << capacity << "): [";
        for (int i = 0; i < length; i++) {
            std::cout << data[i];
            if (i < length - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }

    // 清空
    void clear() {
        length = 0;
    }
};

// ============================================================
// 使用示例
// ============================================================
int main() {
    std::cout << "=== 顺序表示例 ===" << std::endl;

    SeqList<int> list(4);  // 初始容量为 4

    // 添加元素
    std::cout << "\n[添加元素 10, 20, 30]" << std::endl;
    list.pushBack(10);
    list.pushBack(20);
    list.pushBack(30);
    list.print();

    // 插入元素
    std::cout << "\n[在位置 2 插入 15]" << std::endl;
    int removed;
    if (list.insert(2, 15)) {
        list.print();
    }

    // 触发扩容
    std::cout << "\n[继续添加 40, 50, 60，触发扩容]" << std::endl;
    list.pushBack(40);
    list.pushBack(50);
    list.pushBack(60);
    list.print();

    // 按值查找
    std::cout << "\n[查找 30 的位置]: " << list.locate(30) << std::endl;

    // 删除
    std::cout << "\n[删除位置 3 的元素]" << std::endl;
    if (list.remove(3, removed)) {
        std::cout << "删除的元素: " << removed << std::endl;
        list.print();
    }

    // 随机访问
    std::cout << "\n[访问位置 2]: " << list[2] << std::endl;

    return 0;
}
