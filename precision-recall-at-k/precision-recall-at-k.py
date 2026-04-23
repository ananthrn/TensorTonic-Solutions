def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    set_recommended = set(recommended[:k])
    set_relevant = set(relevant)

    intersect = set_recommended.intersection(set_relevant)

    return [len(intersect)/k, len(intersect)/len(relevant)]
    # Write code here