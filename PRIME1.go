package main

import (
   "fmt"
)

// (1 <= m <= n <= 1.000.000.000, n-m<=100000
func printPrimes(m, n int32) {
   if m==1{       
      m = 2 
   }
   if m%2==0{
      if m==2{
         fmt.Printf("%d\n",2)
      }
      m += 1   // start from odd number      
   }
   
   for i:=m; i<=n; i+=2 {
      var j int32
      prime := true
      for j=2; j*j<=i; j++{
         if i%j == 0{
            prime = false
            //fmt.Printf("%d non e primo", i)
            break
         }
      }
      if prime{
         fmt.Printf("%d\n",i)
      }
   }
   fmt.Printf("\n")
   
}

func main(){
   tests := 0
   var m,n int32
   fmt.Scanln( &tests)
   
   for i:=0; i<tests; i++{ 
      fmt.Scanln(&m, &n)
      printPrimes(m,n) 
   }
}

