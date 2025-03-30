import os
import subprocess
from datetime import datetime

def push_to_github(problem_name, code, language_extension):
    # Format filename (e.g., "Two_Sum_20240330.py")
    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"{problem_name.replace(' ', '_')}_{timestamp}.{language_extension}"
    
    # Organize by topic (e.g., "Arrays/Two_Sum.py")
    folder = "GFG-Solutions"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as f:
        f.write(f"# GeeksforGeeks: {problem_name}\n# Problem URL: [PASTE_URL_HERE]\n\n{code}")
    
    # Git commands
    subprocess.run(['git', 'add', filepath])
    subprocess.run(['git', 'commit', '-m', f"Added solution for {problem_name}"])
    subprocess.run(['git', 'push'])

# Example usage (after solving a problem on GFG):
 push_to_github("Two Sum", "// User function template for C++

/*
class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/
class Solution {
  public:
    int height(Node* node) {
        // Base case: If the node is NULL, return -1 (edge-based height)
        if (node == NULL) {
            return -1;
        }

        return 1 + max(height(node->left), height(node->right));
    }
};", "py")