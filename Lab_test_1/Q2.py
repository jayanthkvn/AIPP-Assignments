"""Rectangle utilities with AI-generated documentation."""

AI_PROMPT = """You are an assistant that writes concise, professional
Python docstrings and inline comments for a Rectangle class with methods
area() and perimeter(). The tone should be instructional, mention units
when appropriate, and highlight assumptions about numeric inputs."""


MANUAL_DOCS = {
    "Rectangle": (
        "Manual: Represents a simple axis-aligned rectangle storing width "
        "and height without any validation or coordinate system concerns."
    ),
    "area": (
        "Manual: Multiplies width by height to report the rectangular "
        "surface size in squared units."
    ),
    "perimeter": (
        "Manual: Computes the total boundary distance by summing width and "
        "height twice."
    ),
}


class Rectangle:
    """AI: Models an axis-aligned rectangle defined by width and height."""

    def __init__(self, width: float, height: float) -> None:
        """AI: Store the provided edge lengths for later geometric queries."""
        # AI: Ensure internal state keeps raw numeric values for reuse later.
        self.width = width
        self.height = height

    def area(self) -> float:
        """AI: Return the covered surface area in squared units."""
        # AI: Multiply the orthogonal edges to obtain the planar measure.
        return self.width * self.height

    def perimeter(self) -> float:
        """AI: Return the total boundary length of the rectangle."""
        # AI: Sum both edges twice to walk around the entire outline.
        return 2 * (self.width + self.height)


def compare_documentation() -> str:
    """Return a formatted comparison between AI and manual docs."""
    lines = ["Documentation comparison:"]
    ai_docs = {
        "Rectangle": Rectangle.__doc__,
        "area": Rectangle.area.__doc__,
        "perimeter": Rectangle.perimeter.__doc__,
    }
    for key in ("Rectangle", "area", "perimeter"):
        lines.append(f"{key}:")
        lines.append(f"  AI -> {ai_docs[key]}")
        lines.append(f"  Manual -> {MANUAL_DOCS[key]}")
    return "\n".join(lines)


if __name__ == "__main__":
    sample = Rectangle(3, 4)
    print(f"Area: {sample.area()}")  # Expect 12
    print(f"Perimeter: {sample.perimeter()}")  # Expect 14
    print()
    print(compare_documentation())
    print()
    print("AI prompt used for docstrings/comments:")
    print(AI_PROMPT)

