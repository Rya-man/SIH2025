async function loadQuiz() {
  const gameID = document.getElementById("gameID").value.trim();
  if (!gameID) return alert("Enter a Game ID");

  try {
    const res = await fetch(`http://127.0.0.1:5000/quiz/${gameID}`);
    const data = await res.json();

    const quizDiv = document.getElementById("quiz");
    quizDiv.innerHTML = "";

    if (data.error) {
      quizDiv.textContent = data.error;
      quizDiv.style.display = "block"; // show error box
      return;
    }

    // Show quiz box only now
    quizDiv.style.display = "block";

    // Display question
    const questionElem = document.createElement("p");
    questionElem.textContent = data.question;
    questionElem.style.fontWeight = "bold";
    quizDiv.appendChild(questionElem);

    // Display options
    data.options.forEach(opt => {
      const btn = document.createElement("button");
      btn.textContent = opt;
      btn.classList.add("option-btn");

      btn.onclick = () => {
        if (opt[0] === data.answer) {
          btn.classList.add("correct");
          showModal("✅ Correct!");
        } else {
          btn.classList.add("wrong");
          showModal(`❌ Wrong! Correct answer is: ${data.answer}`);
        }

        // Disable all buttons after choice
        const allBtns = document.querySelectorAll(".option-btn");
        allBtns.forEach(b => b.disabled = true);
      };

      quizDiv.appendChild(btn);
    });

  } catch (err) {
    const quizDiv = document.getElementById("quiz");
    quizDiv.style.display = "block";
    quizDiv.textContent = "Failed to fetch quiz: " + err;
  }
}

// Show popup modal
function showModal(message) {
  const modal = document.getElementById("resultModal");
  const text = document.getElementById("resultText");
  text.textContent = message;
  modal.style.display = "flex";
}

// Close popup modal
function closeModal() {
  document.getElementById("resultModal").style.display = "none";
}
