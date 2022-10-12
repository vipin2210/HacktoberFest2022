import java.util.Arrays;    
public class Anagram  
{    
//function that checks if the strings are anagram or not      
static void isAnagram(String str1, String str2)   
{    
//removes white spaces from string 1  
String s1 = str1.replaceAll("\\s", "");    
//removes white spaces from string 2  
String s2 = str2.replaceAll("\\s", "");    
boolean status = true;    
//checks the length of both the strings are equal or not  
if (s1.length() != s2.length())   
{    
//if length of strings is not equal status returns false      
status = false;    
}   
//executes if lengths of strings are equal  
else   
{    
//first converts the string 1 in lower case and then converts the string into a character array      
//final string stores in arrayS1  
char[] arrayS1 = s1.toLowerCase().toCharArray();    
//first converts the string 2 in lower case and then converts the string into a character array      
//final string stores in arrayS2  
char[] arrayS2 = s2.toLowerCase().toCharArray();    
//sorts the character array arrayS1  
Arrays.sort(arrayS1);    
//sorts the character array arrayS2  
Arrays.sort(arrayS2);    
//compares the strings  
status = Arrays.equals(arrayS1, arrayS2);    
}    
if (status)   
{    
//prints if status returns true      
System.out.println(s1 + " and " + s2 + " are anagrams");    
}   
else   
{    
//prints if status returns false      
System.out.println(s1 + " and " + s2 + " are not anagrams");    
}    
}    
//driver code  
public static void main(String args[])   
{    
//calling function      
isAnagram("HEART", "EARTH");    
isAnagram("TRIANGLE", "INTEGRAL");    
isAnagram("TOSS", "SHOT");   
}    
}   
