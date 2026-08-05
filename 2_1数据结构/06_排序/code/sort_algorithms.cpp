// ============================================================
// 排序算法综合实现
// 包含：直接插入排序、希尔排序、冒泡排序、快速排序
// ============================================================

#include <iostream>
#include <vector>
#include <algorithm>

// 打印数组
void printArray(const int a[], int n) {
    std::cout << "[";
    for (int i = 0; i < n; i++) {
        std::cout << a[i];
        if (i < n - 1) std::cout << ", ";
    }
    std::cout << "]" << std::endl;
}

// ============================================================
// 1. 直接插入排序
// ============================================================
void insertSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int key = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = key;
    }
}

// ============================================================
// 2. 希尔排序
// ============================================================
void shellSort(int a[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int key = a[i];
            int j = i - gap;
            while (j >= 0 && a[j] > key) {
                a[j + gap] = a[j];
                j -= gap;
            }
            a[j + gap] = key;
        }
    }
}

// ============================================================
// 3. 冒泡排序
// ============================================================
void bubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                std::swap(a[j], a[j + 1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

// ============================================================
// 4. 快速排序
// ============================================================
int partition(int a[], int left, int right) {
    int pivot = a[right];
    int i = left - 1;
    for (int j = left; j < right; j++) {
        if (a[j] <= pivot) {
            i++;
            std::swap(a[i], a[j]);
        }
    }
    std::swap(a[i + 1], a[right]);
    return i + 1;
}

void quickSortHelper(int a[], int left, int right) {
    if (left < right) {
        int pivotPos = partition(a, left, right);
        quickSortHelper(a, left, pivotPos - 1);
        quickSortHelper(a, pivotPos + 1, right);
    }
}

void quickSort(int a[], int n) {
    quickSortHelper(a, 0, n - 1);
}

// ============================================================
// 主函数：测试所有排序算法
// ============================================================
int main() {
    const int N = 10;
    int original[N] = {64, 34, 25, 12, 22, 11, 90, 5, 77, 30};
    int a[N];

    std::cout << "原始数组: ";
    printArray(original, N);

    // 直接插入排序
    std::copy(original, original + N, a);
    std::cout << "\n直接插入排序: ";
    insertSort(a, N);
    printArray(a, N);

    // 希尔排序
    std::copy(original, original + N, a);
    std::cout << "希尔排序: ";
    shellSort(a, N);
    printArray(a, N);

    // 冒泡排序
    std::copy(original, original + N, a);
    std::cout << "冒泡排序: ";
    bubbleSort(a, N);
    printArray(a, N);

    // 快速排序
    std::copy(original, original + N, a);
    std::cout << "快速排序: ";
    quickSort(a, N);
    printArray(a, N);

    return 0;
}
