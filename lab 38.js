// lab 1
function parseJSON(jsonStr) {
  try {
    const parsed = JSON.parse(jsonStr);
    console.log("Parsed object:", parsed);
  } catch (error) {
    console.error("Invalid JSON format");
  }
}

// lab2
parseJSON('{"name": "Alice", "age": 25}');
parseJSON('{"name": "Alice", "age": }');

// lab2
const numbers = [5, 8, 13, 2, 10, 7];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
  const num = numbers[i];
  console.log("Current number:", num);

  if (num % 2 === 0) {
    sum += num;
    console.log("Even number, added to sum:", sum);
  }
}

console.log("Final sum of even numbers:", sum);

//3
let user = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 },
    { name: "Charlie", age: 22 }
];
console.log(user);

// lab4
function divide(a,b){
    try {
        if (b === 0) {
            throw new Error("Division by zero is not allowed.");
        }
        return a / b;
    } catch (error) {
        console.error("Error:", error.message);
    }
}

console.log(divide(10, 2));
console.log(divide(10, 0));

// lab 5

try {
    console.log(myVariable);
} catch (error) {
    console.error("Error:", error.message);
}