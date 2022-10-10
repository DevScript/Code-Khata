package data.structures;

public class BinaryTree {
    Object root;
    BinaryTree left, right;
    
    BinaryTree(){
        this.root = null;
    }
    
    BinaryTree(Object root){
        this.root = root; 
    }
    
    BinaryTree(Object root, BinaryTree left, BinaryTree right){
        this.root = root;
        this.left = left;
        this.right = right;
    }

    public Object getRoot() {
        return root;
    }

    public void setRoot(Object root) {
        this.root = root;
    }

    public BinaryTree getLeft() {
        return left;
    }

    public void setLeft(BinaryTree left) {
        this.left = left;
    }

    public BinaryTree getRight() {
        return right;
    }

    public void setRight(BinaryTree right) {
        this.right = right;
    }
    
    public String inOrder(){
        StringBuffer buffString = new StringBuffer();
        
        if(left != null)
            buffString.append(left.inOrder()).append(" ");
        
        buffString.append(root).append(" ");
        
        if( right != null)
            buffString.append(right.inOrder()).append(" ");
        
        return buffString + "";
    }
    
    public String preOrder(){
        StringBuffer buf = new StringBuffer();
        
        buf.append(root).append(" ");
        
        if( left != null)
            buf.append(left.preOrder()).append(" ");
        
        if( right != null)
            buf.append(right.preOrder()).append(" ");
        
        return buf + "";
    }
    
//    public static void PostOrder(BinaryTree Btree) {//left right root
//        if (Btree == null) {
//            return;
//        }
//        PostOrder(Btree.left);
//        PostOrder(Btree.right);
//        System.out.println(Btree.root);
//    }
    
    public String postOrder(){
        StringBuffer buf = new StringBuffer();    
        
        if(left != null)
            buf.append(left.postOrder()).append(" ");
        
        if(right != null)
            buf.append(right.postOrder()).append(" ");
        
        buf.append(root).append(" ");
        
        return buf + "";
    }
    
    public boolean isLeaf(){
        return (left == null && right == null);
    }
    
    public int size(){
        if(root == null) return 0;
        
        if(left == null && right == null)
            return 1;
        if(left == null)
            return 1+ right.size();
        if(right == null)
            return 1+ left.size();
        
        return 1 + left.size() + right.size();
    }
    
    
    public int height(){
        if(root == null) return -1;
        int leftNode = 0;
        int rightNode = 0;
        if(left != null)
            leftNode = 1 + left.height();
        
        if(right != null)
            rightNode = 1 + right.height();
        
        return leftNode>rightNode?leftNode:rightNode;
    }
    
    public boolean contain(Object target){
        if(root == target) return true;
        
        if(left != null)
            if(left.contain(target))
                return true;
        
        if(right != null)
            if(right.contain(target))
                return true;
        return false; 
    }
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree("Zohaib");
        BinaryTree left = new BinaryTree("leftHand");
        tree.setLeft(left);
        BinaryTree right = new BinaryTree("rightHand");
        tree.setRight(right);
        System.out.println(tree.size());
        System.out.println(tree.contain("Zohaib"));
        System.out.println(tree.inOrder());
    }
}