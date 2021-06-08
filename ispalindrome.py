def ispalindrome(n):
      r=0
      s=0
      while(n):
            r=n%10
            n=n//10
            s=s*10+r
      return s
n=int(input())
s=ispalindrome(n)
if(n==s):
      print("yes it is a palindrome")
else:
      print("yes it is not a palindrome")
