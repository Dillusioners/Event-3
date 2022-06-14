import java.util.Scanner;
class occurence
{
  public static void main(String args[])
  {
     Scanner sc = new Scanner(System.in);
     System.out.print("Enter you word or string: ");
     String input = sc.nextLine();
     System.out.print("Enter what to find: ");
     char search = sc.next().charAt(0);
    
     int count=0;
     for(int i=0; i<input.length(); i++)
     {
        if(input.charAt(i) == search)
        count++;
     }
     
     System.out.println("The Character '"+search+"' appears "+count+" times ");
  }
}