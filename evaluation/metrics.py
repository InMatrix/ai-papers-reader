# metrics.py

import json
import math
from typing import List, Dict

# TODO: read expected results from file
def get_assert(output: str, context) -> Dict:
    scored_papers = json.loads(output)
    expected_dict = {paper['id']: paper['relevance'] for paper in context['test']['expected']}
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

