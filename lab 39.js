console.log("Start");

setTimeout(() => {
  console.log("Inside setTimeout");
}, 2000);

console.log("End");

// lab 2
function delayedMessage(message, delay) {
  setTimeout(() => {
    console.log(message);
  }, delay);
}

delayedMessage("Hello, after 3 seconds!", 3000);

// lab3
function startCounter() {
  let counter = 1;

  const intervalId = setInterval(() => {
    console.log("Counter:", counter);
    if (counter === 5) {
      clearInterval(intervalId);
    }
    counter++;
  }, 1000);
}

// Start the counter
startCounter();

// lab 4
function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data received");
    }, 2000);
  });
}

fetchData()
  .then((result) => {
    console.log(result); // "Data received"
  })
  .finally(() => {
    console.log("Request completed");
  });


// lab 5
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = Math.random() > 0.5;
      if (success) {
        resolve("Data received");
      } else {
        reject("Error: Failed to fetch data");
      }
    }, 2000);
  });
}

// Call the function
fetchData()
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  })
  .finally(() => {
    console.log("Request completed");
  });



