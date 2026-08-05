// ============================================================
// 栈 - 顺序栈和链栈实现
// ============================================================

#include <iostream>
#include <string>

// ============================================================
// 顺序栈
// ============================================================
template <typename T>
class SeqStack {
private:
    T* data;
    int capacity;
    int top;    // 栈顶指针，指向栈顶元素的下一个位置

public:
    explicit SeqStack(int cap = 64) : capacity(cap), top(0) {
        data = new T[cap];
    }

    ~SeqStack() {
        delete[] data;
    }

    bool empty() const { return top == 0; }
    int size() const { return top; }

    bool push(const T& e) {
        if (top >= capacity) {
            std::cerr << "[Error] 栈满" << std::endl;
            return false;
        }
        data[top++] = e;
        return true;
    }

    bool pop(T& e) {
        if (empty()) {
            std::cerr << "[Error] 栈空" << std::endl;
            return false;
        }
        e = data[--top];
        return true;
    }

    bool getTop(T& e) const {
        if (empty()) return false;
        e = data[top - 1];
        return true;
    }

    void print() const {
        std::cout << "Stack(bottom->top): [";
        for (int i = 0; i < top; i++) {
            std::cout << data[i];
            if (i < top - 1) std::cout << ", ";
        }
        std::cout << "]" << std::endl;
    }
};

// ============================================================
// 应用：括号匹配检查
// ============================================================
bool isBracketMatch(const std::string& s) {
    SeqStack<char> stack(128);
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            char top;
            if (!stack.getTop(top)) {
                return false;  // 栈空但遇到右括号
            }
            if ((c == ')' && top == '(') ||
                (c == ']' && top == '[') ||
                (c == '}' && top == '{')) {
                stack.pop(top);  // 匹配成功
            } else {
                return false;    // 类型不匹配
            }
        }
    }
    return stack.empty();  // 栈空说明全部匹配
}

// ============================================================
// 应用：后缀表达式求值
// ============================================================
int evalPostfix(const std::string& expr) {
    SeqStack<int> stack(64);
    for (char c : expr) {
        if (c >= '0' && c <= '9') {
            stack.push(c - '0');
        } else if (c == '+' || c == '-' || c == '*' || c == '/') {
            int b, a;
            stack.pop(b);
            stack.pop(a);
            switch (c) {
                case '+': stack.push(a + b); break;
                case '-': stack.push(a - b); break;
                case '*': stack.push(a * b); break;
                case '/': stack.push(a / b); break;
            }
        }
    }
    int result;
    stack.pop(result);
    return result;
}

// ============================================================
// 主函数
// ============================================================
int main() {
    std::cout << "=== 栈的基本操作 ===" << std::endl;
    SeqStack<int> stack;
    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.print();

    int e;
    stack.pop(e);
    std::cout << "弹出: " << e << std::endl;
    stack.print();

    std::cout << "\n=== 括号匹配 ===" << std::endl;
    std::cout << "({[]}) -> " << (isBracketMatch("({[]})") ? "匹配" : "不匹配") << std::endl;
    std::cout << "({[}) -> " << (isBracketMatch("({[})") ? "匹配" : "不匹配") << std::endl;
    std::cout << "((()) -> " << (isBracketMatch("((())") ? "匹配" : "不匹配") << std::endl;

    std::cout << "\n=== 后缀表达式求值 ===" << std::endl;
    std::cout << "352*+ = " << evalPostfix("352*+") << std::endl;
    std::cout << "34+52-* = " << evalPostfix("34+52-*") << std::endl;

    return 0;
}
