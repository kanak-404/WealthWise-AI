const API_URL = "http://127.0.0.1:5000";

// Load summary
fetch(`${API_URL}/summary`)
.then(res => res.json())
.then(data => {

    document.getElementById("total").innerText = data.total_spending;
    document.getElementById("score").innerText = data.financial_health_score + "/100";

    // Prediction
    document.getElementById("prediction").innerText = data.prediction;

    // Categories
    let catList = document.getElementById("categories");
    for (let key in data.category_breakdown) {
        let li = document.createElement("li");
        li.innerText = `${key}: ₹${data.category_breakdown[key]}`;
        catList.appendChild(li);
    }

    // Insights
    let insightsList = document.getElementById("insights");
    data.insights.forEach(insight => {
        let li = document.createElement("li");
        li.innerText = insight;
        insightsList.appendChild(li);
    });
});

// Chatbot
function askAI() {
    let question = document.getElementById("question").value;

    fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("answer").innerText = data.answer;
    });
}

function simulate() {
    fetch(`${API_URL}/simulate`, {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("simulation_result").innerText = data.message;
    });
}