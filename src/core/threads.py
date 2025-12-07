from enum import Enum
import random
from typing import List, Tuple

class StabilityState(Enum):
    """
    4 Stability States / 4 حالت پایداری
    Dormant → Exploration → Consolidation → Production → Dormant (Cycle)
    """
    DORMANT = "Dormant"
    EXPLORATION = "Exploration"
    CONSOLIDATION = "Consolidation"
    PRODUCTION = "Production"

class MetaFunction(Enum):
    """
    4 Meta-Functions / 4 ابرتابع
    The primary cognitive dimensions of the architecture.
    """
    LOGIC = "Logic"
    NARRATIVE = "Narrative"
    SELF_REFERENCE = "Self-Reference"
    IO = "I/O"

class Thread:
    """
    Represents a single cognitive thread within the RAM-16 architecture.
    """
    def __init__(self, meta_function: MetaFunction, state: StabilityState):
        self.meta_function = meta_function
        self.state = state
        self.progress = 0.0  # میزان پیشرفت در حالت فعلی (0 تا 1)

    def step(self):
        """
        Simulates one step of thread processing (Amir's Time 'tick').
        Increments progress and transitions to the next state upon completion.
        """
        increment = random.uniform(0.05, 0.15)
        self.progress += increment
        if self.progress >= 1.0:
            self.progress = 0.0
            self.next_state()

    def next_state(self):
        """
        Moves to the next state in the stability cycle.
        """
        states = list(StabilityState)
        current_index = states.index(self.state)
        next_index = (current_index + 1) % len(states)
        self.state = states[next_index]

    def __repr__(self):
        return f"<Thread {self.meta_function.value:14} | {self.state.value:14} | P={self.progress:.2f}>"

class RAM16:
    """
    The main 16-threaded cognitive architecture (4 MetaFunction x 4 StabilityState).
    """
    def __init__(self):
        self.threads: List[Thread] = []
        self._initialize_threads()

    def _initialize_threads(self):
        """
        Creates all 16 threads, initially setting them to the Dormant state.
        """
        for meta in MetaFunction:
            # Create 4 threads for each meta-function, covering all four stability states (for initial potential)
            # Although the states might be randomized later, starting them all as dormant is clean.
            for _ in range(4):
                thread = Thread(meta, StabilityState.DORMANT)
                self.threads.append(thread)

    def step_all(self):
        """
        Executes one step (one tick of Amir's Time) for all 16 threads simultaneously.
        """
        for thread in self.threads:
            thread.step()

    def get_states(self) -> List[Tuple[MetaFunction, StabilityState, float]]:
        """
        Returns the current state (MetaFunction, StabilityState, Progress) for all threads.
        """
        return [(t.meta_function, t.state, t.progress) for t in self.threads]

    def __repr__(self):
        return "--- RAM-16 System State ---\n" + "\n".join(str(t) for t in self.threads)

# مثال استفاده سریع
if __name__ == "__main__":
    ram = RAM16()
    print("--- Initial State ---")
    print(ram)

    for i in range(5):
        print(f"\n--- Step {i+1} ---")
        ram.step_all()
        print(ram)

