import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
       BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    int n=Integer.parseInt(br.readLine());
        StringBuilder sb=new StringBuilder();

        if(n>=90 &&n<=100){
            sb.append("A");
        }
        else if(n>=80&&n<=89){
            sb.append("B");
        }
        else if(n>=70&&n<=79){
            sb.append("C");
        }
        else if(n>=60&&n<=69){
            sb.append("D");
        }
        else{
            sb.append("F");
        }
         System.out.print(sb.toString());
    }
   
}