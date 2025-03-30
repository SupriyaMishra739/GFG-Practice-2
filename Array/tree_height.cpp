
// User function template for C++

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
class Solution
{
public:
    int height(Node *node)
    {
        // Base case: If the node is NULL, return -1 (edge-based height)
        if (node == NULL)
        {
            return -1;
        }

        return 1 + max(height(node->left), height(node->right));
    }
};