import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
      BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
int i=0;
     while(true){
    StringTokenizer st=new StringTokenizer(br.readLine());
        int a=Integer.parseInt(st.nextToken());
        int b=Integer.parseInt(st.nextToken());
            if (a == 0 && b == 0)
{
        break;
    }
        StringBuilder sb=new StringBuilder();
    sb.append(a+b).append('\n');
    System.out.print(sb.toString());
 
}
        i+=i;
    }
}