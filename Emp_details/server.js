const express = require("express");
const mysql = require("mysql2");
const cors = require("cors");

const app = express();
app.use(express.json()); // To parse JSON request body
app.use(cors()); // Enable CORS for frontend requests

// MySQL Connection
const db = mysql.createConnection({
    host: "localhost",
    user: "root",  // Change if needed
    password: "loki",  // Add password if required
    database: "employee_db",
    port: 3306     // Ensure MySQL is on port 3306
});

db.connect(err => {
    if (err) {
        console.error("MySQL Connection Error:", err);
        return;
    }
    console.log("MySQL Connected...");
});

// TEST Route (to check if backend is working)
app.get("/", (req, res) => {
    res.send("Server is running...");
});

// ✅ Add Employee Route
app.post("/addEmployee", (req, res) => {
    console.log("Received Data:", req.body); // Debugging

    const { name, designation, mandal, opening_balance, closing_balance } = req.body;

    if (!name || !designation || !mandal) {
        return res.status(400).json({ message: "Missing required fields" });
    }

    const sql = `INSERT INTO employees (name, designation, mandal, opening_balance, closing_balance) VALUES (?, ?, ?, ?, ?)`;

    db.query(sql, [name, designation, mandal, opening_balance, closing_balance], (err, result) => {
        if (err) {
            console.error("Database Error:", err);
            res.status(500).json({ message: "Database error" });
        } else {
            res.json({ message: "Employee added successfully!" });
        }
    });
});

// Start Server
app.listen(3000, () => {
    console.log("Server running on port 3000");
});
