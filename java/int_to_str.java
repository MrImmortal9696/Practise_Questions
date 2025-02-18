import java.util.Scanner;

public class int_to_str {

    public static void main(String[] args) throws Exception{
        System.out.println("Enter Enumber :");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        String s="0123456789";
        int i=num;
        if(i==0){
            System.out.println("0");
        }

        String result="";
        while (i>0){
            result = s.charAt(i % 10) + result;
            i = i / 10;   
        }
        sc.close();
        System.out.println(result.getClass().getName());
        System.out.println(result);
    }
    
}
