# metrics.py

import json
import math
from typing import List, Dict

def calculate_scoring_metrics(output: str, expected: List[Dict]) -> Dict:
    scored_papers = json.loads(output)
    expected_dict = {paper['id']: paper['relevance'] for paper in expected}
    
    # Mean Absolute Error
    mae = sum(abs(paper['relevance'] - expected_dict[paper['id']]) for paper in scored_papers) / len(scored_papers)
    
    # Root Mean Square Error
    rmse = math.sqrt(sum((paper['relevance'] - expected_dict[paper['id']]) ** 2 for paper in scored_papers) / len(scored_papers))
    
    # Spearman's Rank Correlation
    scored_ranks = {paper['id']: rank for rank, paper in enumerate(sorted(scored_papers, key=lambda x: x['relevance'], reverse=True))}
    expected_ranks = {paper['id']: rank for rank, paper in enumerate(sorted(expected, key=lambda x: x['relevance'], reverse=True))}
    n = len(scored_papers)
    d_squared = sum((scored_ranks[paper['id']] - expected_ranks[paper['id']]) ** 2 for paper in scored_papers)
    spearman = 1 - (6 * d_squared) / (n * (n**2 - 1))
    
    return {
        'pass': mae < 1.0 and rmse < 1.5 and spearman > 0.7,  # Adjust thresholds as needed
        'score': spearman,  # Using Spearman's correlation as the main score
        'reason': f'MAE: {mae:.2f}, RMSE: {rmse:.2f}, Spearman: {spearman:.2f}'
    }

def calculate_metrics(output: str, expected: List[Dict]) -> Dict:
    selected_papers = json.loads(output)
    relevant_papers = [paper for paper in expected if paper['relevance'] >= 3]
    
    k = 5
    precision_at_k = len([p for p in selected_papers[:k] if any(rp['id'] == p['id'] for rp in relevant_papers)]) / k
    recall_at_k = len([p for p in selected_papers[:k] if any(rp['id'] == p['id'] for rp in relevant_papers)]) / len(relevant_papers)
    
    f1_score = 2 * (precision_at_k * recall_at_k) / (precision_at_k + recall_at_k) if (precision_at_k + recall_at_k) > 0 else 0
    
    ndcg = sum((next((rp['relevance'] for rp in relevant_papers if rp['id'] == paper['id']), 0) / (math.log2(i + 2)))
               for i, paper in enumerate(selected_papers))
    
    return {
        'pass': f1_score > 0.7,  # Adjust threshold as needed
        'score': f1_score,
        'reason': f'Precision@{k}: {precision_at_k:.2f}, Recall@{k}: {recall_at_k:.2f}, F1: {f1_score:.2f}, NDCG: {ndcg:.2f}'
    }