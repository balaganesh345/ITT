// Main Wrapper Class
public class bst {

    // 1. Define the internal Node structure
    static class Node {
        int data;
        Node left;
        Node right;

        // Constructor to create a new node
        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }

    // Root pointer of the BST
    private Node root;

    public bst() {
        this.root = null;
    }

    // Public method to insert a value
    public void insert(int value) {
        root = insertRecursive(root, value);
    }

    // Helper method to recursively find the right spot and insert
    private Node insertRecursive(Node current, int value) {
        // If we reach an empty spot, create and return the new node
        if (current == null) {
            return new Node(value);
        }

        // Smaller values go to the left subtree
        if (value < current.data) {
            current.left = insertRecursive(current.left, value);
        } 
        // Larger values go to the right subtree
        else if (value > current.data) {
            current.right = insertRecursive(current.right, value);
        }

        // Return the unchanged node pointer
        return current;
    }

    // Public method for In-Order Traversal
    public void inOrder() {
        inOrderRecursive(root);
        System.out.println(); // Print a new line at the end
    }

    // Helper method to print elements in sorted ascending order
    private void inOrderRecursive(Node current) {
        if (current != null) {
            inOrderRecursive(current.left);       // 1. Visit Left
            System.out.print(current.data + " "); // 2. Visit Root Data
            inOrderRecursive(current.right);      // 3. Visit Right
        }
    }

    // --- Main Method to Test the Tree ---
    public static void main(String[] args) {
        bst b = new bst();

        // Insert unsorted values
        b.insert(15);
        b.insert(7);
        b.insert(27);
        b.insert(4);
        b.insert(10);
        b.insert(20);
        b.insert(88);

        // Print the sorted output
        System.out.print("Sorted Elements in Java BST: ");
        b.inOrder();
    }
}
