import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());

        StringBuilder sb=new StringBuilder();
        for(int i=1;i<=n;i++){
            for(int j=n-1;j>=i;j--){
                sb.append(" ");
        }
            for(int j=0;j<i;j++){
             sb.append("*");
            }
              sb.append("\n");
        }
        System.out.print(sb.toString());
    }
}