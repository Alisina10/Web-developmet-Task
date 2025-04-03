// lab 1
for ( i = 0; i < 10; i++) {
    console.log(i);
}

// lab 2

let num = 10;
while (num >= 1) {
    console.log (num);
    num--;
}

// lab 3

let userInput;
do {
    userInput = pareseInt(prompt("Enter a number greater than 10"), 10);

} while (userInput <= 10);
console.log("valid input received:", userInput);

// lab 4

let fruits = ["apple", "banana", "cherry", "date", "elderberry"];
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// lab 5

let fruits = ["apple", "banana", "cherry", "date", "elderberry"];
let i = 0;
while (i < fruits.length) {
    console.log(fruits[i]);
    i++;
}

// lab 6
let num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for (let i = 0; i < num.length; i++) {
    if (num [i] === 12) {
        console.log("number 12 is found, stopping the loop");
        break;
    }
    console.log(num[i]);
}

// lab 7

let number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

for (let i = 0; i < num.length; i++) {
    if (number[i] === 5 ){
        continue
    }
    console.log(number[i]);
}


