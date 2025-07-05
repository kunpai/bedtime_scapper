"""
Cost-benefit analysis utility for decision making in bedtime story generation.
"""

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Option:
    """
    Represents an option with associated cost and benefit values.
    
    Attributes:
        name: The name/description of the option
        cost: The cost value (e.g., time, money, emotional load)
        benefit: The benefit value (e.g., narrative impact, audience engagement)
    """
    name: str
    cost: float
    benefit: float


def evaluate_options(options: List[Option]) -> List[Tuple[str, float]]:
    """
    Evaluate a list of options by comparing their cost and benefit scores.
    
    Args:
        options: List of Option objects to evaluate
        
    Returns:
        List of (name, score) tuples sorted by descending benefit-to-cost ratio
    """
    scored = [(opt.name, opt.benefit / (opt.cost + 1e-5)) for opt in options]
    return sorted(scored, key=lambda x: x[1], reverse=True)


def analyze_cost_benefit(options: List[Option], threshold: float = 1.0) -> dict:
    """
    Perform comprehensive cost-benefit analysis on a list of options.
    
    Args:
        options: List of Option objects to analyze
        threshold: Minimum benefit-to-cost ratio to be considered viable
        
    Returns:
        Dictionary containing analysis results including rankings, viable options, and poor tradeoffs
    """
    if not options:
        return {
            'rankings': [],
            'viable_options': [],
            'poor_tradeoffs': [],
            'summary': 'No options provided for analysis'
        }
    
    # Get rankings
    rankings = evaluate_options(options)
    
    # Identify viable options (above threshold)
    viable_options = [(name, score) for name, score in rankings if score >= threshold]
    
    # Identify poor tradeoffs (below threshold)
    poor_tradeoffs = [(name, score) for name, score in rankings if score < threshold]
    
    # Generate summary
    best_option = rankings[0] if rankings else None
    summary = f"Best option: {best_option[0]} (score: {best_option[1]:.2f})" if best_option else "No viable options"
    
    return {
        'rankings': rankings,
        'viable_options': viable_options,
        'poor_tradeoffs': poor_tradeoffs,
        'summary': summary
    }