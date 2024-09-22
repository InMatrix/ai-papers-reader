import json
import math
from typing import List, Dict

def get_assert(output: str, context) -> Dict:
    model_response = json.loads(output)
    topic = context['vars']['topic']
    
    # Extract all 'id' values into a list
    selected_papers = [paper['id'] for paper in model_response]
    
    # Read expected results from golden.json
    with open('golden.json', 'r') as f:
        golden = json.load(f)

    golden_papers = golden[topic]

    # Compute recall and precision
    true_positives = len(set(golden_papers) & set(selected_papers))
    recall = true_positives / len(set(golden_papers)) if golden_papers else 0.0
    precision = true_positives / len(set(selected_papers)) if selected_papers else 0.0
    
    # Compute F1 score
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

    reason = f'''
    Recall: {recall:.2f}, Precision: {precision:.2f}, F1: {f1:.2f}

    Selected papers: {selected_papers}

    Golden papers: {golden_papers}

    '''
    
    return {
        'pass': recall >= 0.7 and precision >= 0.7 and f1 >= 0.7,  # Reasonable thresholds
        'score': f1,  # Using F1 score as the main metric
        'reason': reason
    }

