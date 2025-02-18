import java.util.ArrayList;
import java.util.Scanner;

public class largest_ele{
    public static void main(String[] args) {
        ArrayList<Integer> arr= new ArrayList<Integer>();
        int count;
        int max=0;
        Scanner sc=new Scanner(System.in);
        count = sc.nextInt();
        System.out.println("Enter the number");
        for(int i=0;i<count;i++){
            
            arr.add(sc.nextInt());
        }

        for(int i=0;i<count;i++){
            if(arr.get(i)>max){
                max=arr.get(i);
            }
        }

        System.out.println("The largest number is: "+max);
    }
}