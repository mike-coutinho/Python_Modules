from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    valid_ingredients = dark_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    for item in valid_ingredients:
        if item.lower() in ingredients_lower:
            return f"({ingredients} - VALID)"
    return f"({ingredients} - INVALID)"
