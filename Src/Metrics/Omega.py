"""
Omega-Score Calculator for RAVEN-RAM16
=======================================

Simplified implementation for MVP (Minimum Viable Product).
"""

from dataclasses import dataclass
from typing import List, Dict
import numpy as np


@dataclass
class ConversationTurn:
    """Single turn in a conversation."""
    timestamp: float
    speaker: str  # "user" or "assistant"
    text: str
    concepts: List[str] = None  # Extracted keywords
    
    def __post_init__(self):
        if self.concepts is None:
            # Simple concept extraction: split by space
            self.concepts = self.text.lower().split()[:5]


@dataclass
class OmegaMetrics:
    """Container for Omega metrics."""
    FI: float  # Frequency Index
    RI: float  # Resonance Index  
    DI: float  # Depth Index
    SI: float  # Sustainability Index
    omega: float  # Overall score
    is_golden_zone: bool


class OmegaCalculator:
    """
    Calculates Omega-Score from conversation data.
    
    Formula:
        Ω(t) = 0.25·FI + 0.25·RI + 0.25·DI + 0.25·SI
    
    Example:
        >>> calc = OmegaCalculator()
        >>> conversation = [
        ...     ConversationTurn(0.0, "user", "What is AI?"),
        ...     ConversationTurn(5.0, "assistant", "AI is artificial intelligence"),
        ... ]
        >>> metrics = calc.compute_omega(conversation)
        >>> print(f"Ω = {metrics.omega:.3f}")
    """
    
    def __init__(self, golden_threshold: float = 0.75):
        """
        Initialize calculator.
        
        Args:
            golden_threshold: Minimum Ω-Score for Golden Zone
        """
        self.golden_threshold = golden_threshold
    
    def compute_FI(self, conversation: List[ConversationTurn]) -> float:
        """
        Frequency Index: Rate of information exchange.
        
        Simple formula: (# turns) / (time span in minutes)
        Normalized to [0, 1] assuming max 10 turns/min.
        """
        if len(conversation) < 2:
            return 0.0
        
        time_span = conversation[-1].timestamp - conversation[0].timestamp
        if time_span == 0:
            return 0.0
        
        # Convert to per-minute rate
        rate = len(conversation) / (time_span / 60.0)
        
        # Normalize (assume max 10 turns/min)
        return min(rate / 10.0, 1.0)
    
    def compute_RI(self, conversation: List[ConversationTurn]) -> float:
        """
        Resonance Index: Conceptual overlap between turns.
        
        Simple formula: Average Jaccard similarity of consecutive turns.
        """
        if len(conversation) < 2:
            return 0.0
        
        similarities = []
        for i in range(1, len(conversation)):
            prev = set(conversation[i-1].concepts)
            curr = set(conversation[i].concepts)
            
            if len(prev) == 0 or len(curr) == 0:
                continue
            
            # Jaccard similarity
            overlap = len(prev & curr)
            total = len(prev | curr)
            
            if total > 0:
                similarities.append(overlap / total)
        
        return np.mean(similarities) if similarities else 0.0
    
    def compute_DI(self, conversation: List[ConversationTurn]) -> float:
        """
        Depth Index: Reasoning complexity.
        
        Simple formula: Average text length (as proxy for depth).
        Normalized assuming max 500 chars.
        """
        if not conversation:
            return 0.0
        
        avg_length = np.mean([len(turn.text) for turn in conversation])
        
        # Normalize (assume max depth = 500 chars)
        return min(avg_length / 500.0, 1.0)
    
    def compute_SI(self, conversation: List[ConversationTurn]) -> float:
        """
        Sustainability Index: Long-term coherence.
        
        Simple formula: Concept retention across conversation.
        """
        if len(conversation) < 3:
            return 0.0
        
        # Get all concepts from first half
        midpoint = len(conversation) // 2
        first_half_concepts = set()
        for turn in conversation[:midpoint]:
            first_half_concepts.update(turn.concepts)
        
        # Get all concepts from second half
        second_half_concepts = set()
        for turn in conversation[midpoint:]:
            second_half_concepts.update(turn.concepts)
        
        if len(first_half_concepts) == 0:
            return 0.0
        
        # How many first-half concepts appear in second half?
        retention = len(first_half_concepts & second_half_concepts)
        
        return retention / len(first_half_concepts)
    
    def compute_omega(self, conversation: List[ConversationTurn]) -> OmegaMetrics:
        """
        Compute full Omega metrics.
        
        Args:
            conversation: List of conversation turns
            
        Returns:
            OmegaMetrics with all scores
        """
        FI = self.compute_FI(conversation)
        RI = self.compute_RI(conversation)
        DI = self.compute_DI(conversation)
        SI = self.compute_SI(conversation)
        
        # Equal weighted average
        omega = 0.25 * (FI + RI + DI + SI)
        
        # Check Golden Zone
        is_golden = omega >= self.golden_threshold
        
        return OmegaMetrics(
            FI=FI,
            RI=RI,
            DI=DI,
            SI=SI,
            omega=omega,
            is_golden_zone=is_golden
        )
    
    def compute_timeline(self, conversation: List[ConversationTurn], 
                        window_size: int = 5) -> List[OmegaMetrics]:
        """
        Compute Ω-Score over time using sliding window.
        
        Args:
            conversation: Full conversation
            window_size: Number of turns per window
            
        Returns:
            List of OmegaMetrics for each window
        """
        timeline = []
        
        for i in range(window_size, len(conversation) + 1):
            window = conversation[i-window_size:i]
            metrics = self.compute_omega(window)
            timeline.append(metrics)
        
        return timeline


# Example usage
if __name__ == "__main__":
    # Sample conversation
    conversation = [
        ConversationTurn(0.0, "user", "What is quantum entanglement?"),
        ConversationTurn(5.0, "assistant", "Quantum entanglement is a phenomenon where particles become correlated"),
        ConversationTurn(15.0, "user", "How does this relate to Bell's theorem?"),
        ConversationTurn(20.0, "assistant", "Bell's theorem proves that quantum entanglement cannot be explained by local hidden variables"),
    ]
    
    # Compute metrics
    calc = OmegaCalculator()
    metrics = calc.compute_omega(conversation)
    
    print(f"Ω-Score: {metrics.omega:.3f}")
    print(f"  FI: {metrics.FI:.3f}")
    print(f"  RI: {metrics.RI:.3f}")
    print(f"  DI: {metrics.DI:.3f}")
    print(f"  SI: {metrics.SI:.3f}")
    print(f"  Golden Zone: {'✓' if metrics.is_golden_zone else '✗'}")
