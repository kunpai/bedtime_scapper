"""
Test script to demonstrate the Valorant integration functionality
"""

from valo_story_utils import is_valorant_request, fetch_valorant_story_seed

def test_valorant_integration():
    """Test the Valorant integration features"""
    print("=== Valorant Integration Test ===\n")
    
    # Test 1: Valorant request detection
    print("1. Testing Valorant Request Detection:")
    test_cases = [
        "Tell me a Valorant story",
        "I want a story about agents",
        "Create a bedtime story about Valorant",
        "Tell me about a duck",
        "I want a story about a princess",
        "Story about valo agents please"
    ]
    
    for request in test_cases:
        is_valo = is_valorant_request(request)
        print(f"   '{request}' -> {'✓ Valorant' if is_valo else '✗ Not Valorant'}")
    
    # Test 2: Story seed generation
    print("\n2. Testing Story Seed Generation:")
    seed = fetch_valorant_story_seed()
    print(f"   Generated seed: {seed}")
    
    # Test 3: Integration flow demonstration
    print("\n3. Integration Flow Demonstration:")
    print("   When a user asks: 'Tell me a Valorant story'")
    print("   - System detects: ✓ Valorant request")
    print("   - Fetches live data: ✓ Match data incorporated")
    print("   - Enhances prompt: ✓ Child-friendly context added")
    print("   - Generates story: ✓ LLM creates bedtime story with Valorant theme")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    test_valorant_integration()