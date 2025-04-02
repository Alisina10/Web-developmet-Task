// lab 1

let a = 10;
let b = 3;

console.log("addition:", a+b);
console.log("Subtraction:", a-b);
console.log("Multipilication:", a*b);
console.log("Division:", a/b);
console.log("Modulus:", a % b);
console.log("Expoentiation:", a+b);

// lab 2

let age = 15;
let isRegistered = true;


if (age >= 18 && isRegistered){
  console.log ("you are Eligible to vote.")
} else {
  console.log ("you are not Eligible to vote");

}

// lab 3

let a = 12;
let b = 12;

if (a > b){

  console.log(" a is greater than b")
} else if (a < b ){

  console.log ( " b is greater than a"
  )
} else {
  console.log ("a and b is Equal.")
}

// lab 4:

let num = -4;

if (num> 0 ){

  console.log ("number is Positive.");
} else if ( num < 0){
  console.log ("number is Nagative.");
} else {
  console.log("the number is zero");
}

// lab 5

let day = "Tuesday";

switch (day) {
  case "Monday":
    console.log("Start of the week!");
    break;
  case "Friday":
    console.log("Weekend is near!");
    break;
  case "Sunday":
    console.log("It's a rest day.");
    break;
  default:
    console.log("It's a regular day.");
}


// lab 6

let num = 7;

let result = (num % 2 === 0) ? "Even" : "Odd";
console.log("The number is:", result);
