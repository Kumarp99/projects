document.getElementById("employeeForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // Prevents page reload

    const formData = new FormData(event.target);
    const jsonData = Object.fromEntries(formData.entries());

    console.log("Sending Data:", jsonData); // Debugging

    const response = await fetch("http://localhost:3000/addEmployee", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(jsonData)
    });

    const result = await response.json();
    console.log("Server Response:", result); // Debugging
    alert(result.message);
});
