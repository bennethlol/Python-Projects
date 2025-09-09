// Constant Variables, setting the standard rates
const hourly = 3.75;
const weekendMulti = 1.25;
const max = 25;

// Function to calculate the parking fees
const calculateParkingFees = (hours, isWeekend) => {
    let rate = hourly;
    // If weekend button is pressed, apply weekend charge to the rate
    if (isWeekend) {
        rate = rate * weekendMulti;
    }
    // Return the fee
    let fee = rate * hours;
    return fee > 25 ? max : fee;
};

// When calculate button is pressed
const buttonPressed = () => {
    // Turn user input into variables for calculations
    const hoursInput = document.getElementById("hours").value;
    const hours = parseFloat(hoursInput);
    const weekendChecked = document.getElementById("weekend").checked;
    // Calculate the fees
    const fees = calculateParkingFees(hours, weekendChecked);
    const tax = fees * 0.13;
    const total = fees + tax;

    // Update the DOMs, displaying fees after everything is inputted
    document.getElementById("parkingFees").textContent = `Parking Fees: $${fees.toFixed(2)}`;
    document.getElementById("tax").textContent = `Tax: $${tax.toFixed(2)}`;
    document.getElementById("total").textContent = `Total: $${total.toFixed(2)}`;
};

// Event listener, checks if button was pressed or not
document.getElementById("calcButton").addEventListener("click", buttonPressed);
