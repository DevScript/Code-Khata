import java.util.*;

class Nede{ // class node for nodes
    char data;
    Nede(char data){        // constructor which takes one parameter
        this.data= data;
    }
}
class Grpha{    // class Graph for graph
    ArrayList<Node> nodes;  // array list for add nodes to the graph
    int[][] matrix; // A 2D matrix
    Grpha(int size){    // constructor initialize array and arraylist
        nodes= new ArrayList<>();
        matrix= new int[size][size];
    }
    public void addNode(Node node){ // method which add nodes to graph
        nodes.add(node);
    }
    public void addEdge(int src,int dest){  //method which add edges to nodes
        matrix[src][dest]=1;    // if value is equal to 1 then there is edge
    }
    public boolean chckEdge(int src, int dest){ //method for chcking of edge between nodes
        if (matrix[src][dest]==1){
            return true;
        }
        else{
            return false;
        }
    }
    public void print(){    // print ,method which print matrix and nodes
        System.out.print("  ");

        for(Node node: nodes){      // for each loop for print nodes
            System.out.print(node.data+" ");
        }
        System.out.println();
        for(int i=0; i<matrix.length; i++){ // for loop for print elements rows
            System.out.print(nodes.get(i).data+" ");
            for(int j=0; j<matrix[i].length; j++){    // for loop for print elements of columns
                System.out.print(matrix[i][j]+" ");
            }
            System.out.println();
        }
    }
    public void Breadth_FS(int src){    // Breadth first search method
        Queue<Integer> queue= new LinkedList<>();   // Queue
        boolean [] visited= new boolean[matrix.length]; // Array of type boolean

        queue.offer(src);   // add elements to queue
        visited[src]=true;  //  first element is true means visited

        while(queue.size()!=0){ // loop for check
            src= queue.poll();
            System.out.println(nodes.get(src).data+" = visited");

            for(int i=0; i<matrix[src].length; i++){    // loop for chchk in every row
                if(matrix[src][i]==1 && !visited[i]){
                    queue.offer(i);
                    visited[i]=true;
                }
            }
        }
    }
}
public class Breadth_First_search {
    // Breadth FS = Traverse a graph level by level
    //              Utilize a Queue
    //              Better if destination is on average close to start
    //              Siblings are visited before children


    public static void main(String[] args){
        Grpha graph= new Grpha(5);  // object of class Graph

        graph.addNode(new Node('A'));   // add Nodes to the Graph
        graph.addNode(new Node('B'));
        graph.addNode(new Node('C'));
        graph.addNode(new Node('D'));
        graph.addNode(new Node('E'));

        graph.addEdge(0,1); //  add Edges to the Graph
        graph.addEdge(1,2);
        graph.addEdge(1,4);
        graph.addEdge(2,3);
        graph.addEdge(2,4);
        graph.addEdge(4,0);
        graph.addEdge(4,2);

        graph.print();

        graph.Breadth_FS(4);

        System.out.println(graph.chckEdge(0,1));    // check for edges
        System.out.println(graph.chckEdge(3,2));    // check for edges
        System.out.println(graph.chckEdge(4,1));    // check for edges

    }

}


