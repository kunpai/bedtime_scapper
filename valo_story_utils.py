"""
Valorant story utility functions for bedtime story generation.
Integrates with valo_bot_scapper to fetch live match data for story context.
"""

import sys
import os
from typing import Dict, List, Optional

# Add the valo_bot_scapper directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'valo_bot_scapper'))

try:
    from scapping_funcs import getLiveMatches, getMatchScore
except (ImportError, Exception) as e:
    print(f"Warning: Could not import valo_bot_scapper functions: {e}")
    getLiveMatches = None
    getMatchScore = None


def fetch_valorant_story_seed() -> str:
    """
    Fetch live Valorant match data and return a summary suitable for bedtime story generation.
    
    Returns:
        str: A child-friendly summary of current Valorant matches that can be woven into a bedtime story.
             Returns a default message if no live matches are available or if there's an error.
    """
    if getLiveMatches is None:
        return "In the magical world of Valorant, brave agents are always ready for adventure!"
    
    try:
        # Get current live matches
        live_matches = getLiveMatches()
        
        if not live_matches:
            # No live matches - return a general Valorant-themed seed
            return ("In the world of Valorant, brave agents from different teams are preparing for their next mission. "
                   "They train hard, work together, and always help each other succeed!")
        
        # Format the live matches into a child-friendly story seed
        story_seed = "In the exciting world of Valorant, there are brave agents having adventures right now! "
        
        # Limit to first 2 matches to keep the story concise
        for i, match in enumerate(live_matches[:2]):
            team1 = match.get('team1', 'Team Alpha')
            team2 = match.get('team2', 'Team Beta')
            
            if i == 0:
                story_seed += f"The {team1} agents are working together with the {team2} agents to complete an important mission. "
            else:
                story_seed += f"Meanwhile, the {team1} team and {team2} team are also on a special quest. "
        
        story_seed += ("All these brave agents show us how teamwork, friendship, and helping each other "
                      "can make any challenge possible to overcome!")
        
        return story_seed
        
    except Exception as e:
        # Log the error (in a real app, we'd use proper logging)
        print(f"Error fetching Valorant data: {e}")
        
        # Return a safe fallback message
        return ("In the world of Valorant, brave agents are always ready for teamwork and friendship. "
               "They show us that working together makes everything possible!")


def get_valorant_match_details(match_data: Dict) -> Optional[Dict]:
    """
    Get detailed information about a specific Valorant match.
    
    Args:
        match_data: Dictionary containing match information from getLiveMatches()
        
    Returns:
        Optional[Dict]: Detailed match information, or None if error occurs
    """
    if getMatchScore is None:
        return None
        
    try:
        return getMatchScore(match_data)
    except Exception as e:
        print(f"Error getting match details: {e}")
        return None


def is_valorant_request(user_request: str) -> bool:
    """
    Check if the user request is asking for a Valorant-related story.
    
    Args:
        user_request: The user's story request
        
    Returns:
        bool: True if the request mentions Valorant, False otherwise
    """
    valorant_keywords = ['valorant', 'valo', 'agent', 'agents', 'spike', 'radiant']
    request_lower = user_request.lower()
    
    return any(keyword in request_lower for keyword in valorant_keywords)