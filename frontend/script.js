async function askQuestion() {
    let question = document.getElementById("question").value;
    let responseElement = document.getElementById("response");

    if (!question) {
        responseElement.innerHTML = "⚠️ Please enter a question.";
        return;
    }

    responseElement.innerHTML = " Asking...";  // Show loading state

    try {
        let response = await fetch("http://127.0.0.1:8000/qa/ask/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: question }),
        });

        let data = await response.json();
        responseElement.innerHTML = `<strong>Answer:</strong> ${data.answer}`;
    } catch (error) {
        responseElement.innerHTML = "Failed to fetch answer. Is the backend running?"; 
    }
}
