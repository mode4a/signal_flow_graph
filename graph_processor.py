from duplicate_cycles_remove import remove_duplicate_cycles

def dfs_forward_paths(cur_node, graph, visited, cur_path, paths, cur_weight):
    if visited[cur_node] == 1 or (len(cur_path) > 0 and cur_path[-1] > cur_node):
        return

    visited[cur_node] = 1
    cur_path.append(cur_node)

    if cur_node == len(graph) - 1:
        paths.append((cur_path.copy(), cur_weight.copy()))
    else:
        for node, weight in graph[cur_node]:
            cur_weight.append(weight)
            dfs_forward_paths(node, graph, visited, cur_path, paths, cur_weight)
            cur_weight.pop()

    cur_path.pop()
    visited[cur_node] = 0

def forward_paths(graph):
    visited = [0 for _ in range(len(graph))]
    cur_path = []
    cur_weight = []
    paths = []
    dfs_forward_paths(0, graph, visited, cur_path, paths, cur_weight)
    return paths

def dfs_cycles(cur_node, graph, visited, cur_path, cycles, cur_weight):
    if visited[cur_node] == 1:
        if cur_path[-1] < cur_node:
            return
        idx = cur_path.index(cur_node)
        cur_path.append(cur_node)
        cycles.append((cur_path[idx:].copy(), cur_weight[idx:].copy()))
        cur_path.pop()
        return

    visited[cur_node] = 1
    cur_path.append(cur_node)

    for node, weight in graph[cur_node]:
        cur_weight.append(weight)
        dfs_cycles(node, graph, visited, cur_path, cycles, cur_weight)
        cur_weight.pop()

    cur_path.pop()
    visited[cur_node] = 0

def cycles(graph):
    visited = [0 for _ in range(len(graph))]
    cur_path = []
    cur_weight = []
    cycles = []
    dfs_cycles(0, graph, visited, cur_path, cycles, cur_weight)
    return remove_duplicate_cycles(cycles)

