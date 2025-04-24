import enum

class BlockType(enum.Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(text):
    if text.startswith("#"):
        return BlockType.HEADING
    if text.startswith("```") and text.endswith("```"):
        return BlockType.CODE
    if text.startswith(">"):
        return BlockType.QUOTE
    if text.startswith("- "):
        return BlockType.UNORDERED_LIST
    if text.startswith("1. "):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH