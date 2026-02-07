import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        int[] arr = new int[9];
         BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
       for(int i=0;i<9;i++){
          
           int n=Integer.parseInt(br.readLine());
           arr[i]=n;
       }
        int max=arr[0];
        int index=1;

        for(int i=1;i<9;i++){
            if(arr[i]>max){
                max=arr[i];
                index=i+1;
            }
        }
        System.out.println(max);
        System.out.println(index);
    }
}