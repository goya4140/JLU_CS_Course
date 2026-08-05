// ============================================================
// 线性表 - 单链表实现
// 带头结点的单链表模板类
// ============================================================

#include <iostream>

template <typename T>
class LinkedList {
private:
    struct Node {
        T data;
        Node* next;
        Node(const T& val, Node* p = nullptr) : data(val), next(p) {}
    };
    Node* head;      // 头结点
    int length;

public:
    // 构造函数：创建头结点
    LinkedList() : length(0) {
        head = new Node(T());  // 头结点的数据域无意义
    }

    // 析构函数：释放所有结点
    ~LinkedList() {
        Node* p = head;
        while (p) {
            Node* temp = p;
            p = p->next;
            delete temp;
        }
    }

    // 获取长度
    int size() const { return length; }

    // 判空
    bool empty() const { return head->next == nullptr; }

    // 在位置 i（1-based）插入元素 e
    bool insert(int i, const T& e) {
        if (i < 1 || i > length + 1) return false;

        Node* p = head;
        int j = 0;
        // 找到第 i-1 个结点
        while (p && j < i - 1) {
            p = p->next;
            j++;
        }

        if (!p) return false;

        // 插入新结点
        p->next = new Node(e, p->next);
        length++;
        return true;
    }

    // 在表尾添加
    void pushBack(const T& e) {
        insert(length + 1, e);
    }

    // 在表头添加
    void pushFront(const T& e) {
        insert(1, e);
    }

    // 删除位置 i（1-based）的元素
    bool remove(int i, T& e) {
        if (i < 1 || i > length) return false;

        Node* p = head;
        int j = 0;
        // 找到第 i-1 个结点
        while (p && j < i - 1) {
            p = p->next;
            j++;
        }

        if (!(p->next)) return false;

        Node* q = p->next;     // q 指向要删除的结点
        e = q->data;
        p->next = q->next;     // 绕过 q
        delete q;
        length--;
        return true;
    }

    // 按值查找，返回位置（1-based），找不到返回 0
    int locate(const T& e) const {
        Node* p = head->next;
        int i = 1;
        while (p) {
            if (p->data == e) return i;
            p = p->next;
            i++;
        }
        return 0;
    }

    // 获取位置 i 的元素
    bool get(int i, T& e) const {
        if (i < 1 || i > length) return false;
        Node* p = head->next;
        int j = 1;
        while (p && j < i) {
            p = p->next;
            j++;
        }
        if (p) {
            e = p->data;
            return true;
        }
        return false;
    }

    // 遍历输出
    void print() const {
        std::cout << "LinkedList(" << length << "): head";
        Node* p = head->next;
        while (p) {
            std::cout << " -> " << p->data;
            p = p->next;
        }
        std::cout << " -> nullptr" << std::endl;
    }

    // 清空链表（保留头结点）
    void clear() {
        Node* p = head->next;
        while (p) {
            Node* temp = p;
            p = p->next;
            delete temp;
        }
        head->next = nullptr;
        length = 0;
    }
};

// ============================================================
// 使用示例
// ============================================================
int main() {
    std::cout << "=== 单链表示例 ===" << std::endl;

    LinkedList<int> list;

    // 添加元素
    std::cout << "\n[表尾添加 10, 20, 30]" << std::endl;
    list.pushBack(10);
    list.pushBack(20);
    list.pushBack(30);
    list.print();

    // 表头添加
    std::cout << "\n[表头添加 5]" << std::endl;
    list.pushFront(5);
    list.print();

    // 插入
    std::cout << "\n[在位置 3 插入 15]" << std::endl;
    list.insert(3, 15);
    list.print();

    // 查找
    std::cout << "\n[查找 20 的位置]: " << list.locate(20) << std::endl;

    // 删除
    std::cout << "\n[删除位置 2 的元素]" << std::endl;
    int removed;
    if (list.remove(2, removed)) {
        std::cout << "删除的元素: " << removed << std::endl;
        list.print();
    }

    return 0;
}
