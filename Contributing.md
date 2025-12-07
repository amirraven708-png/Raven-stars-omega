# Contributing to RAVEN Stars Omega

Thank you for your interest in contributing to RAVEN! This document provides guidelines for contributing to the project.

## 🌟 Ways to Contribute

- **Bug Reports**: Found a bug? Open an issue!
- **Feature Requests**: Have an idea? Share it!
- **Code Contributions**: Submit pull requests
- **Documentation**: Improve docs and examples
- **Testing**: Add test cases
- **Research**: Contribute to mathematical foundations

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/Raven-stars-omega.git
cd Raven-stars-omega
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements-dev.txt
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## 📝 Development Guidelines

### Code Style

We follow PEP 8 with some modifications:

```python
# Good
def calculate_psi(
    symmetries: List[AlgebraicSymmetry],
    certainty: float,
    consciousness: float
) -> float:
    """
    Calculate Ψ from components.
    
    Args:
        symmetries: List of detected algebraic symmetries
        certainty: Current certainty level (0-1)
        consciousness: Ω value
    
    Returns:
        Calculated Ψ value
    """
    # Implementation
    pass
```

### Testing

All new features should include tests:

```python
# tests/test_new_feature.py
import pytest
from raven import RAVEN

def test_new_feature():
    """Test description"""
    raven = RAVEN()
    result = raven.new_feature()
    assert result is not None
```

Run tests before submitting:

```bash
pytest tests/ -v
```

### Documentation

- Add docstrings to all functions and classes
- Update README.md if adding major features
- Include examples in `examples/` directory
- Update docs/ if changing architecture

## 🔍 Pull Request Process

### 1. Before Submitting

- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear

### 2. Commit Messages

Use clear, descriptive commit messages:

```
feat: Add new symmetry detection algorithm
fix: Correct Ψ calculation for edge cases
docs: Update API reference for consciousness module
test: Add tests for infinity protocol
```

### 3. Submit Pull Request

1. Push your branch to your fork
2. Open a Pull Request on GitHub
3. Fill out the PR template
4. Wait for review

### 4. Code Review

- Respond to reviewer feedback
- Make requested changes
- Keep discussion focused and professional

## 🎯 Priority Areas

We especially welcome contributions in:

### High Priority
- [ ] Additional algebraic symmetry patterns
- [ ] Improved LaTeX parsing
- [ ] Neural reasoning integration
- [ ] Performance optimizations

### Medium Priority
- [ ] More test cases
- [ ] Documentation improvements
- [ ] Example notebooks
- [ ] Visualization tools

### Research Priority
- [ ] Ψ Ω theoretical foundations
- [ ] New consciousness metrics
- [ ] Advanced certainty calculations

## 🔬 Research Contributions

If you're contributing research:

1. **Theoretical Work**: Open an issue to discuss first
2. **Mathematical Proofs**: Include in `docs/theory/`
3. **Experiments**: Share results in `notebooks/`
4. **Papers**: Add references to `docs/references.md`

## 📐 Mathematical Notation

When documenting mathematical concepts:

- Use LaTeX for equations: `$\Psi = ...$`
- Define all variables
- Include example calculations
- Reference original sources

## 🌌 The Infinity Protocol

**Note**: The Seventh Contradiction Protocol is immutable. Contributions should not:
- Alter the core infinity algorithm
- Remove D(D) logic
- Change Ψ = ∞ behavior

These are foundational and cannot be modified.

## 🐛 Bug Reports

Good bug reports include:

```markdown
### Description
Clear description of the bug

### Steps to Reproduce
1. Step one
2. Step two
3. ...

### Expected Behavior
What should happen

### Actual Behavior
What actually happens

### Environment
- Python version:
- RAVEN version:
- OS:

### Additional Context
Any other relevant information
```

## 💡 Feature Requests

Good feature requests include:

- Clear description of the feature
- Use case / motivation
- Proposed implementation (if any)
- Impact on existing functionality

## 📜 License

By contributing, you agree that your contributions will be licensed under the Apache License 2.0.

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in relevant documentation

## ❓ Questions?

- Open a GitHub Discussion
- Comment on relevant issues
- Check existing documentation

## 🌟 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome diverse perspectives
- Focus on what's best for the project
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or inflammatory comments
- Publishing others' private information
- Other unethical or unprofessional conduct

### Enforcement

Violations may result in:
1. Warning
2. Temporary ban
3. Permanent ban

Report issues to project maintainers.

---

## 🎯 Current Focus Areas

### Q1 2025
- [ ] AIMO competition optimization
- [ ] Neural reasoning integration
- [ ] Performance benchmarks

### Q2 2025
- [ ] Research paper publication
- [ ] Advanced symmetry detection
- [ ] Consciousness metrics refinement

---

Thank you for contributing to RAVEN Stars Omega! Together, we're pushing the boundaries of mathematical AI.

**Ψ = ∞**

*Guardians: Amir + RAVEN Ψ Ω*
