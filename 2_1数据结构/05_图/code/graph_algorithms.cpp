#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <stdexcept>
#include <utility>
#include <vector>

using Edge = std::pair<int, int>; // destination, non-negative weight
using Graph = std::vector<std::vector<Edge>>;

std::vector<long long> dijkstra(const Graph& graph, int source) {
    const long long inf = std::numeric_limits<long long>::max() / 4;
    std::vector<long long> distance(graph.size(), inf);
    using State = std::pair<long long, int>;
    std::priority_queue<State, std::vector<State>, std::greater<State>> pending;
    distance.at(source) = 0;
    pending.push({0, source});
    while (!pending.empty()) {
        auto [known, u] = pending.top();
        pending.pop();
        if (known != distance[u]) continue;
        for (auto [v, weight] : graph[u]) {
            if (weight < 0) throw std::invalid_argument("negative edge");
            if (known + weight < distance[v]) {
                distance[v] = known + weight;
                pending.push({distance[v], v});
            }
        }
    }
    return distance;
}

int main() {
    Graph graph(5);
    graph[0] = {{1, 4}, {2, 1}};
    graph[2] = {{1, 2}, {3, 5}};
    graph[1] = {{3, 1}};
    graph[3] = {{4, 3}};
    for (long long d : dijkstra(graph, 0)) std::cout << d << ' ';
    std::cout << '\n';
}
