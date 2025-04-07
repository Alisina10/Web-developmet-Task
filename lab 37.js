const numbers = [10, 20, 30, 40, 50];
const slicedNumbers = numbers.slice(1, 4);

console.log("Sliced array:", slicedNumbers);
console.log("Original array:", numbers);

// lab 2
const fruits = [];
fruits.push("apple", "banana", "cherry");

const removedFruits = fruits.pop();
console.log("Removed fruit:", removedFruits);
console.log("Remaining fruits:", fruits);


// lab3
const nums = [1, 2, 3, 4, 5];
const squaredNums = nums.map(num => num * num);

console.log("Original array:", nums);
console.log("Squared array:", squaredNums);

// lab 4
const ages = [12, 18, 25, 30, 15];

const adultAges = ages.filter(age => age >= 18);

console.log("Original array:", ages);
console.log("Adult ages:", adultAges);


