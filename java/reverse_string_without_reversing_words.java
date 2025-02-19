public class reverse_string_without_reversing_words {

    public static void main(String[] args) {
        String s="I am a student";
        int len = s.length();
        String result="";
        String word ="";

        for(int i=len-1;i>=0;i--){
            if(s.charAt(i)==' ')
            {
                result = result + word+" ";
                word = "";
            }
            else{
                word = s.charAt(i) + word;
            }
        }
        result=result+word;
        System.out.println(result);
    }
    
}
