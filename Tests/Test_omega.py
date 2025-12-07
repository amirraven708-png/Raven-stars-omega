"""
Tests for Omega-Score calculator.
"""

import pytest
from src.metrics.omega import OmegaCalculator, ConversationTurn, OmegaMetrics


def test_conversation_turn_creation():
    """Test creating a conversation turn."""
    turn = ConversationTurn(
        timestamp=0.0,
        speaker="user",
        text="Hello world"
    )
    
    assert turn.timestamp == 0.0
    assert turn.speaker == "user"
    assert turn.text == "Hello world"
    assert len(turn.concepts) > 0  # Auto-extracted


def test_omega_calculator_initialization():
    """Test calculator initialization."""
    calc = OmegaCalculator()
    assert calc.golden_threshold == 0.75
    
    calc_custom = OmegaCalculator(golden_threshold=0.8)
    assert calc_custom.golden_threshold == 0.8


def test_compute_omega_empty_conversation():
    """Test Omega calculation with empty conversation."""
    calc = OmegaCalculator()
    metrics = calc.compute_omega([])
    
    assert metrics.FI == 0.0
    assert metrics.RI == 0.0
    assert metrics.DI == 0.0
    assert metrics.SI == 0.0
    assert metrics.omega == 0.0
    assert metrics.is_golden_zone == False


def test_compute_omega_single_turn():
    """Test Omega calculation with single turn."""
    calc = OmegaCalculator()
    conversation = [
        ConversationTurn(0.0, "user", "Test message")
    ]
    
    metrics = calc.compute_omega(conversation)
    
    # With only one turn, most metrics should be 0 or low
    assert metrics.FI == 0.0  # Need at least 2 turns
    assert metrics.omega >= 0.0


def test_compute_omega_basic_conversation():
    """Test Omega calculation with basic conversation."""
    calc = OmegaCalculator()
    conversation = [
        ConversationTurn(0.0, "user", "What is AI?"),
        ConversationTurn(5.0, "assistant", "AI is artificial intelligence"),
        ConversationTurn(10.0, "user", "Tell me more about AI"),
    ]
    
    metrics = calc.compute_omega(conversation)
    
    # Check all metrics are computed
    assert 0.0 <= metrics.FI <= 1.0
    assert 0.0 <= metrics.RI <= 1.0
    assert 0.0 <= metrics.DI <= 1.0
    assert 0.0 <= metrics.SI <= 1.0
    assert 0.0 <= metrics.omega <= 1.0


def test_frequency_index():
    """Test FI calculation specifically."""
    calc = OmegaCalculator()
    
    # High frequency (many turns in short time)
    fast_conversation = [
        ConversationTurn(0.0, "user", "Hi"),
        ConversationTurn(1.0, "assistant", "Hello"),
        ConversationTurn(2.0, "user", "How are you?"),
        ConversationTurn(3.0, "assistant", "Good"),
    ]
    
    fi_fast = calc.compute_FI(fast_conversation)
    
    # Low frequency (few turns in long time)
    slow_conversation = [
        ConversationTurn(0.0, "user", "Hi"),
        ConversationTurn(300.0, "assistant", "Hello"),  # 5 min later
    ]
    
    fi_slow = calc.compute_FI(slow_conversation)
    
    # Fast should have higher FI
    assert fi_fast > fi_slow


def test_resonance_index():
    """Test RI calculation specifically."""
    calc = OmegaCalculator()
    
    # High resonance (repeated concepts)
    high_resonance = [
        ConversationTurn(0.0, "user", "quantum physics entanglement"),
        ConversationTurn(5.0, "assistant", "quantum entanglement particles"),
        ConversationTurn(10.0, "user", "quantum theory particles"),
    ]
    
    ri_high = calc.compute_RI(high_resonance)
    
    # Low resonance (different concepts)
    low_resonance = [
        ConversationTurn(0.0, "user", "weather today sunny"),
        ConversationTurn(5.0, "assistant", "stocks market trading"),
        ConversationTurn(10.0, "user", "cooking recipe pasta"),
    ]
    
    ri_low = calc.compute_RI(low_resonance)
    
    # High resonance should have higher RI
    assert ri_high > ri_low


def test_golden_zone_detection():
    """Test Golden Zone detection."""
    calc = OmegaCalculator(golden_threshold=0.5)
    
    # Create a conversation likely to have high scores
    good_conversation = [
        ConversationTurn(i * 5.0, "user" if i % 2 == 0 else "assistant", 
                        "This is a long and detailed message about quantum mechanics and entanglement " * 5)
        for i in range(10)
    ]
    
    metrics = calc.compute_omega(good_conversation)
    
    # This should be a decent conversation
    assert metrics.omega > 0.3  # At least moderate quality


def test_compute_timeline():
    """Test timeline computation."""
    calc = OmegaCalculator()
    
    conversation = [
        ConversationTurn(i * 5.0, "user" if i % 2 == 0 else "assistant", f"Message {i}")
        for i in range(10)
    ]
    
    timeline = calc.compute_timeline(conversation, window_size=3)
    
    # Should have 10 - 3 + 1 = 8 windows
    assert len(timeline) == 8
    
    # All should be OmegaMetrics
    for metrics in timeline:
        assert isinstance(metrics, OmegaMetrics)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
