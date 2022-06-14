import java.util.*;

class acronym{
    public static void main(String[] args){
        //Make a program to create acronyms from words in Java
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a phrase[Note:- The letters in upper case will be taken only]: ");
        String phrase = sc.nextLine();
        String[] words = phrase.split(" ");
        String acronym = "";
        for(int i = 0; i < words.length; i++){
            if(words[i].length() > 2){
                acronym += words[i].charAt(0);
            }
        }
        System.out.println("The acronym we generated is: " + acronym);
    }
}