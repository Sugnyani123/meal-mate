// Load Razorpay script dynamically
const razorpayScript = document.createElement('script');
razorpayScript.src = "https://checkout.razorpay.com/v1/checkout.js";
document.head.appendChild(razorpayScript);

// Function to call Razorpay
function payNow(amount, name) {
    const options = {
        key: "rzp_test_CX1BYqR3wg86hG", // Replace with your Razorpay key
        amount: amount, // in paise
        currency: "INR",
        name: "Meal Mate",
        description: "Food Order Payment",
        handler: function (response) {
            alert("Payment successful! ID: " + response.razorpay_payment_id);
        }
    };
    const rzp = new Razorpay(options);
    rzp.open();
}