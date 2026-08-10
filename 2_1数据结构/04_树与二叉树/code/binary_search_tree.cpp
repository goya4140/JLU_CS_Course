#include <iostream>
#include <memory>

class BinarySearchTree {
    struct Node {
        int key;
        std::unique_ptr<Node> left, right;
        explicit Node(int value) : key(value) {}
    };
    std::unique_ptr<Node> root_;

    static void insert(std::unique_ptr<Node>& node, int key) {
        if (!node) node = std::make_unique<Node>(key);
        else if (key < node->key) insert(node->left, key);
        else if (key > node->key) insert(node->right, key);
    }
    static bool contains(const Node* node, int key) {
        while (node) {
            if (key == node->key) return true;
            node = key < node->key ? node->left.get() : node->right.get();
        }
        return false;
    }
    static void inorder(const Node* node) {
        if (!node) return;
        inorder(node->left.get());
        std::cout << node->key << ' ';
        inorder(node->right.get());
    }
public:
    void insert(int key) { insert(root_, key); }
    bool contains(int key) const { return contains(root_.get(), key); }
    void printInorder() const { inorder(root_.get()); std::cout << '\n'; }
};

int main() {
    BinarySearchTree tree;
    for (int key : {10, 5, 15, 1, 6, 12}) tree.insert(key);
    tree.printInorder();
    std::cout << std::boolalpha << tree.contains(6) << '\n';
}
