import java.util.*;

class N0de{ // class N0de for N0des
    char data;
    N0de(char data){        // constructor which takes one parameter
        this.data= data;
    }
}
class Grph{    // class Graph for graph
    ArrayList<N0de> nodes;  // array list for add N0des to the graph
    int[][] matrix; // A 2D matrix
    Grph(int size){    // constructor initialize array and arraylist
        nodes= new ArrayList<>();
        matrix= new int[size][size];
    }
    public void addnode(N0de node){ // method which add N0des to graph
        nodes.add(node);
    }
    public void addEdge(int src,int dest){  //method which add edges to N0des
        matrix[src][dest]=1;    // if value is equal to 1 then there is edge
    }
    public boolean chckEdge(int src, int dest){ //method for chcking of edge between N0des
        if (matrix[src][dest]==1){
            return true;
        }
        else{
            return false;
        }
    }
    public void print(){    // print ,method which print matrix and N0des
        System.out.print("  ");

        for(N0de node: nodes){      // for each loop for print N0des
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
    public void depthfirstsearch(int src){  //  method for find visited nodes
        boolean[] visited= new boolean[matrix.length];  // boolean array which return true or false
        dFShelper( src,visited);
    }
    private void dFShelper(int src, boolean[] visited){
        if(visited[src]){
            return;
        }
        else {
            visited[src]=true;
            System.out.println(nodes.get(src).data+ " = visited");
        }
        for(int i=0; i<matrix[src].length; i++){
            if(matrix[src][i]==1){
                dFShelper(i, visited);
            }
        }
        return;
    }
}
public class Depth_First_search{
    //Depth First search = Pick a route, keep going.
    //                      if you reach a dead end , or and already visited node ,
    //                      backtrack to a previous node with unvisited adjacent neighbours

    public static void main(String[] args){
        Grph graph= new Grph(5);  // object of class Graph

        graph.addnode(new N0de('A'));   // add N0des to the Graph
        graph.addnode(new N0de('B'));
        graph.addnode(new N0de('C'));
        graph.addnode(new N0de('D'));
        graph.addnode(new N0de('E'));

        graph.addEdge(0,1); //  add Edges to the Graph
        graph.addEdge(1,2);
        graph.addEdge(1,4);
        graph.addEdge(2,3);
        graph.addEdge(2,4);
        graph.addEdge(4,0);
        graph.addEdge(4,2);

        graph.print();
        System.out.println(graph.chckEdge(0,1));    // check for edges
        System.out.println(graph.chckEdge(3,2));    // check for edges
        System.out.println(graph.chckEdge(4,1));    // check for edges

        graph.depthfirstsearch(3);  // call of depthfirstsearch method

    }

}

