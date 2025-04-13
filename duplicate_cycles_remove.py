def normalize_cycle(nodes, weights):
    nodes = nodes[:-1]
    n = len(nodes)
    min_index = min(range(n), key=lambda i: nodes[i])


    rotated_nodes = nodes[min_index:] + nodes[:min_index]
    rotated_weights = weights[min_index:] + weights[:min_index]

    rotated_nodes.append(rotated_nodes[0])

    return tuple(rotated_nodes), tuple(rotated_weights)

def remove_duplicate_cycles(cycles_list):
    seen = set()
    unique = []

    for path, weights in cycles_list:
        norm_nodes, norm_weights = normalize_cycle(path, weights)
        if (norm_nodes, norm_weights) not in seen:
            seen.add((norm_nodes, norm_weights))
            unique.append((list(norm_nodes), list(norm_weights)))

    return unique
