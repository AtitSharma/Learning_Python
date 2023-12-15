// console.log("hello");
// // alert("me");
// document.write("Hello guyz")
// // console.log("Alertttt")
// console.error("This is error ")
// console.assert(5==5)

// var num1 = 100;
// var num2 = 200;
// // console.log(num1 + num2);



// var str1 = "atitsharma"
// var str2 = 'sharmaatit'

// var dict = {
//     atit: 100,
//     gopal: 190,
//     lal: 300
// }


// var a = true
// var b = false

// var und;
// var arr = [1, 2, 3, 4, 5]
// var arr = ["1", "ramsharan", "atit", 7.7, 9]
// // console.log(arr[0])
// // console.log(arr[4])


// function avg(a, b) {

//     c = (a + b) / 2

//     return c

// }

// console.log("The average of", 4, 5, "is", avg(4, 5))



// function recursion(num1) {
//     if (num1 == 1) {
//         return 1
//     }
//     else {
//         return num1 + recursion(num1 - 1)
//     }
// }


// c = recursion(7)
// // console.log(c)



// var arr = [1, 3, 4, 5, 6, 7, 8, 9, 0, 10]
// for(var i=0;i< arr.length;i++){
//     // console.log(arr[i]);
// }

// // SAME THING IN ANOTHER WAY

// arr.forEach(function(element){
// //    console.log(element)
// })

// arr.forEach(function (element) {
//     // console.log(element)
// })


// var arr2 =[100,20,202,201,223,1131,334]

// var j = 0

// // while (j<arr2.length){
// //     console.log(arr2[j])
// //     j++
// // }

// arr2.push("ram")
// // console.log(arr2)
// arr2.pop()
// arr2.shift()
// arr2.unshift("AtitSharma")
// // console.log(arr2)

// arr2.toString()
// // console.log(arr2)
// m=arr2.sort()
// // console.log(m)


// mystring="Atit is very handsome boy and good"
// // console.log(mystring.length)
// // console.log(mystring.indexOf("good"))
// // console.log(mystring.lastIndexOf("good"))

// // console.log(mystring.slice(0,10))
// // x=mystring.replace("good","bad")
// // console.log(x)


// date= new Date()
// // console.log(date)
// // console.log(date.getTime())
// // console.log(date.getFullYear())
// // console.log(date.getDay())
// // console.log(date.getMinutes())
// // console.log(date.getHours())


// let elem = document.getElementsByClassName("container")
// console.log(elem)

// let elem2 =document.getElementById("click")
// console.log(elem2)

// // elem[0].style.background="yellow"
// elem[0].classList.add("bg-primary")
// elem[0].classList.remove('text-sucess')
// // elem[0].classList.add('text-sucess')

// let ele=document.getElementsByClassName("text-success")
// console.log(ele[0])
// ele[0].classList.add('text-sucess')
// ele[0].classList.remove("text-sucess")


// // console.log(ele[0].innerHTML)
// console.log(ele[0].innerText)


// tn=document.getElementsByTagName("div")
// console.log(tn)


// a=document.createElement('p')
// a.innerText="This is the element"
// tn[0].appendChild(a)

// ab=document.createElement('b')
// a.innerText="This is bold"
// tn[0].replaceChild(ab,a)



function clicked(){
    console.log('The button was clicked ')
}

// window.onload=function(){
//     console.log("The document is loaded")
// }
// elem = getElementsByTagName("click")
// console.log(elem)
 
// FirstContainer.addEventListener("click",function(){
//     console.log("Click VAYo")
// })

// FirstContainer.addEventListener('mouseover',function(){
//     console.log("mouse on container")
// })

// FirstContainer.addEventListener('mouseout',function(){
//     console.log("mouse out  container")
// })

// FirstContainer.addEventListener('mouseup',function(){
//     console.log("mouse up  container")
// })
// FirstContainer.addEventListener('mousedown',function(){
//     console.log("mouse down  container")
// })


// FirstContainer.addEventListener("click",function(){
//     document.querySelectorAll('.container')[1].innerHTML = "<b> Subscribed </b>"
//     console.log("Sucessfully Clicked")
// })

// FirstContainer.addEventListener("click",function(){
//     document.getElementsByClassName('text-success')[0].innerHTML = "<b> Subscribed Sucesfully </b>"
//     console.log("Sucessfully Clicked")
// })


// let prevHtml = document.querySelectorAll(".container")[1].innerHTML
// console.log(prevHtml)


// FirstContainer.addEventListener("mouseup",function(){
//     document.querySelectorAll(".container")[1].innerHTML= prevHtml
// })


// FirstContainer.addEventListener("mousedown",function(){
//     document.querySelectorAll(".container")[1].innerHTML= "<b> Clicked </b>"
// })




//ARROW FUNCTION


summ= (a,b)=>{
    return a+b
}

LogIt = ()=>{
    document.querySelectorAll(".container")[1].innerHTML="<b> Timer practice </b>"
    // console.log("success")
}

// setTimeout(LogIt,2000)

clr=setInterval(LogIt,2000) 



localStorage.setItem("name","AtitSharma")




var a= 100
console.log(`The value of a is ${a}`)


