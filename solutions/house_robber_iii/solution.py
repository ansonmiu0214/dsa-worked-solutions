from ..utils import TreeNode
from typing import Optional, Tuple

def amountIfRobOrSkip(node: Optional[TreeNode]) -> Tuple[int, int]:
    """Given the constraint of not robbing adjacent houses, return
    a tuple of:
    
    o max robbery amount from place rooted at 'node' that *includes* robbing 'node'
    o max robbery amount from place rooted at 'node' that *does not include*
      robbing 'node'."""

    if node is None:
        return 0, 0
    
    amountIfRobLeft, amountIfSkipLeft = amountIfRobOrSkip(node.left)
    amountIfRobRight, amountIfSkipRight = amountIfRobOrSkip(node.right)

    # If robbing 'node', must only rob the 'grandchildren' houses.
    amountIfRob = node.val + amountIfSkipLeft + amountIfSkipRight

    # Maximise from all combinations of skipping 'node' .
    amountIfSkip = max(amountIfRobLeft + amountIfRobRight,
                       amountIfRobLeft + amountIfSkipRight,
                       amountIfSkipLeft + amountIfRobRight,
                       amountIfSkipLeft + amountIfSkipRight)

    return amountIfRob, amountIfSkip

def rob(root: TreeNode) -> int:
    """Return maximum amount the thief can rob from town rooted at 'root'
    without alerting the police."""

    return max(amountIfRobOrSkip(root))
