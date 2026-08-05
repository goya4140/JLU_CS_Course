// ============================================================
// 队列 - 循环队列实现
// ============================================================

#include <iostream>

template <typename T>
class CircularQueue {
private:
    T* data;
    int capacity;   // 总容量（实际最多存 capacity-1 个元素）
    int front;      // 队头
    int rear;       // 队尾的下一个位置

public:
    explicit CircularQueue(int cap = 8) : capacity(cap), front(0), rear(0) {
        data = new T[cap];
    }

    ~CircularQueue() {
        delete[] data;
    }

    bool empty() const { return front == rear; }

    bool full() const { return (rear + 1) % capacity == front; }

    int size() const { return (rear - front + capacity) % capacity; }

    bool enQueue(const T& e) {
        if (full()) {
            std::cerr << "[Error] 队列满" << std::endl;
            return false;
        }
        data[rear] = e;
        rear = (rear + 1) % capacity;
        return true;
    }

    bool deQueue(T& e) {
        if (empty()) {
            std::cerr << "[Error] 队列空" << std::endl;
            return false;
        }
        e = data[front];
        front = (front + 1) % capacity;
        return true;
    }

    bool getHead(T& e) const {
        if (empty()) return false;
        e = data[front];
        return true;
    }

    void print() const {
        std::cout << "Queue(front->rear, " << size() << "/" << capacity - 1 << "): [";
        if (empty()) {
            std::cout << "empty]" << std::endl;
            return;
        }
        int i = front;
        while (i != rear) {
            std::cout << data[i];
            i = (i + 1) % capacity;
            if (i != rear) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
};

// ============================================================
// 应用：约瑟夫环（Josephus Problem）
// n 个人围成一圈，从第 1 个人开始报数，报到 m 的人出列，
// 求出列顺序。
// ============================================================
void josephus(int n, int m) {
    CircularQueue<int> queue(n + 1);
    for (int i = 1; i <= n; i++) {
        queue.enQueue(i);
    }

    std::cout << "约瑟夫环 (n=" << n << ", m=" << m << "): ";
    int count = 0;
    int person;
    while (!queue.empty()) {
        int temp;
        queue.deQueue(temp);  // 出队
        count++;
        if (count == m) {
            std::cout << temp << " ";  // 报到 m，出列
            count = 0;
        } else {
            queue.enQueue(temp);  // 未报到 m，重新入队
        }
    }
    std::cout << std::endl;
}

// ============================================================
// 主函数
// ============================================================
int main() {
    std::cout << "=== 循环队列基本操作 ===" << std::endl;
    CircularQueue<int> queue(6);  // 容量 6，最多存 5 个元素

    std::cout << "\n[入队 10, 20, 30, 40]" << std::endl;
    queue.enQueue(10);
    queue.enQueue(20);
    queue.enQueue(30);
    queue.enQueue(40);
    queue.print();

    std::cout << "\n[出队 2 次]" << std::endl;
    int e;
    queue.deQueue(e);
    std::cout << "出队: " << e << std::endl;
    queue.deQueue(e);
    std::cout << "出队: " << e << std::endl;
    queue.print();

    std::cout << "\n[入队 50, 60（利用之前出队的空间）]" << std::endl;
    queue.enQueue(50);
    queue.enQueue(60);
    queue.print();

    std::cout << "\n[尝试入队 70（队列已满）]" << std::endl;
    queue.enQueue(70);

    std::cout << "\n=== 约瑟夫环 ===" << std::endl;
    josephus(7, 3);

    return 0;
}
