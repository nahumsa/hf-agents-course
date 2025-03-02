from smolagents import CodeAgent, tool, HfApiModel
from enum import Enum

class OccasionEnum(Enum):
    CASUAL = "casual"
    FORMAL = "formal"
    SUPERHERO = "superhero"
    OTHER = "other"

@tool
def suggest_menu(occasion: OccasionEnum) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion: The type of occasion for the party.
    """
    match occasion:
        case OccasionEnum.CASUAL:
            return "Pizza, snacks, and drinks."
        case OccasionEnum.FORMAL:
            return "3-course dinner with wine and dessert."
        case OccasionEnum.SUPERHERO:
            return "Buffet with high-energy and healthy food."
        case _:
            return "Custom menu for the butler."

# Alfred, the butler, preparing the menu for the party
agent = CodeAgent(tools=[suggest_menu], model=HfApiModel())

# Preparing the menu for the party
agent.run("Prepare a formal menu for the party.")
